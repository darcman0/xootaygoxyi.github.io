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


def slugify(title: str) -> str:
    """Reproduit le slug utilisé par Material pour les titres du blog."""
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug, flags=re.UNICODE)
    slug = re.sub(r"[\s_-]+", "-", slug)
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
    """Récupère le premier titre H1 lorsqu'il n'existe pas dans le YAML."""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def get_last_update() -> datetime:
    """
    Lit la date de la dernière génération dans le JSON existant.
    Si le fichier est absent ou illisible, remonte 90 jours en arrière
    pour couvrir toute la période de publication du blog.
    """
    if not OUTPUT_FILE.exists():
        return datetime.now(timezone.utc) - timedelta(days=90)
    try:
        data = json.loads(OUTPUT_FILE.read_text(encoding="utf-8"))
        generated_at = data.get("generated_at", "")
        if generated_at:
            return datetime.fromisoformat(generated_at)
    except (json.JSONDecodeError, ValueError):
        pass
    return datetime.now(timezone.utc) - timedelta(days=90)


def article_index() -> dict[str, dict]:
    """Indexe les articles par leur URL publique exacte."""
    index = {}
    for path in sorted((DOCS_DIR / "blog" / "posts").glob("*.md")):
        meta = read_front_matter(path)
        title = meta.get("title") or get_markdown_title(path)
        if not title:
            continue

        route = f"/blog/{slugify(str(title))}/"
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

    # GoatCounter peut renvoyer les caractères accentués encodés dans l'URL.
    value = unquote(value)

    if not value.startswith("/"):
        value = "/" + value
    if not value.endswith("/"):
        value += "/"
    return value


def extract_hits(payload: dict) -> list[dict]:
    hits = payload.get("hits", [])
    if not isinstance(hits, list):
        raise RuntimeError("La réponse GoatCounter ne contient pas une liste 'hits'.")
    return hits


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
    for hit in extract_hits(payload):
        path = normalize_path(str(hit.get("path", "")))
        article = articles.get(path)
        if not article:
            continue

        count = hit.get("count", 0)
        try:
            count = int(count)
        except (TypeError, ValueError):
            count = 0

        item = dict(article)
        item["views"] = count
        candidates.append(item)

    candidates.sort(key=lambda item: item["views"], reverse=True)
    popular = candidates[:POPULAR_LIMIT]

    # Fallback : compléter avec les articles les plus récents si on n'a pas
    # assez de données de vues pour atteindre POPULAR_LIMIT.
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
        print(
            "Erreur : GOATCOUNTER_API_TOKEN_POPULAR_ARTICLE est absent.",
            file=sys.stderr,
        )
        return 1

    now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
    start = get_last_update().replace(minute=0, second=0, microsecond=0)

    print(f"Période de collecte : {start.date()} → {now.date()}")

    articles = article_index()
    popular = fetch_popular_articles(token, articles, now, start)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(
            {
                "generated_at": now.isoformat(),
                "period_start": start.isoformat(),
                "period_days": (now - start).days,
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
        print(f"- {article['views']} vues : {article['title']} ({article['url']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())