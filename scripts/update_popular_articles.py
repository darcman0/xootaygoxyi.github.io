from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests
import yaml

SITE_URL = "https://darcman0.goatcounter.com"
API_URL = f"{SITE_URL}/api/v0/stats/hits"
DOCS_DIR = Path("docs")
OUTPUT_FILE = DOCS_DIR / "assets" / "data" / "popular-articles.json"
LIMIT = 100
POPULAR_LIMIT = 2

# Fenêtre d'analyse : 7 jours glissants (1 semaine)
DAYS_WINDOW = 7


def slugify(title: str) -> str:
    """Reproduit exactement le slug utilisé par Material et main.py."""
    slug = title.lower().strip()
    slug = re.sub(r"['’\"”«»]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"[^\w-]", "", slug, flags=re.UNICODE)
    return slug.strip("-")


def read_front_matter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    data = yaml.safe_load(content[3:end])
    return data if isinstance(data, dict) else {}


def get_markdown_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def article_index() -> dict[str, dict]:
    index = {}
    for path in sorted((DOCS_DIR / "blog" / "posts").glob("*.md")):
        meta = read_front_matter(path)
        title = meta.get("title") or get_markdown_title(path)
        if not title:
            continue

        slug = meta.get("slug") or slugify(str(title))
        route = f"/blog/{slug}/"

        index[route] = {
            "title": str(title),
            "url": route,
            "image": meta.get("image", ""),
            "date": str(meta.get("date", {}).get("created", ""))
            if isinstance(meta.get("date"), dict)
            else str(meta.get("date", "")),
            "categories": meta.get("categories", []),
        }
    return index


def normalize_path(value: str) -> str:
    if value.startswith("http://") or value.startswith("https://"):
        value = urlparse(value).path
    value = unquote(value)
    if not value.startswith("/"):
        value = "/" + value
    if not value.endswith("/"):
        value += "/"
    return value


def fetch_popular_articles(
    token: str,
    articles: dict[str, dict],
    now: datetime,
    start: datetime,
) -> list[dict]:
    params = {
        "limit": LIMIT,
        "start": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "end": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(API_URL, params=params, headers=headers, timeout=20)
    response.raise_for_status()
    payload = response.json()

    candidates = []
    hits = payload.get("hits", [])
    if isinstance(hits, list):
        for hit in hits:
            path = normalize_path(str(hit.get("path", "")))
            article = articles.get(path)
            if not article:
                continue

            try:
                count = int(hit.get("count", 0))
            except (TypeError, ValueError):
                count = 0

            item = dict(article)
            item["views"] = count
            candidates.append(item)

    candidates.sort(key=lambda item: item["views"], reverse=True)
    popular = candidates[:POPULAR_LIMIT]

    # Compléter avec les articles les plus récents si besoin
    if len(popular) < POPULAR_LIMIT:
        existing_urls = {a["url"] for a in popular}
        for url, article in sorted(
            articles.items(),
            key=lambda x: x[1].get("date", ""),
            reverse=True,
        ):
            if url not in existing_urls:
                item = dict(article)
                item["views"] = 0
                popular.append(item)
            if len(popular) >= POPULAR_LIMIT:
                break

    return popular


def main() -> int:
    token = os.environ.get("GOATCOUNTER_API_TOKEN_POPULAR_ARTICLE")
    if not token:
        print("Erreur : GOATCOUNTER_API_TOKEN_POPULAR_ARTICLE est absent.", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
    # Toujours interroger sur les 7 derniers jours glissants
    start = now - timedelta(days=DAYS_WINDOW)

    print(f"Période d'analyse : {start.date()} → {now.date()} ({DAYS_WINDOW} jours)")

    articles = article_index()
    popular = fetch_popular_articles(token, articles, now, start)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(
            {
                "generated_at": now.isoformat(),
                "period_start": start.isoformat(),
                "period_days": DAYS_WINDOW,
                "articles": popular,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"{len(popular)} article(s) populaire(s) enregistré(s) dans {OUTPUT_FILE}")
    for article in popular:
        print(f"- {article['views']} vue(s) : {article['title']} ({article['url']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())