from pathlib import Path
import re

import yaml


BLOG_POST_TEMPLATE = "blog-post.html"


def read_front_matter(path):
    """Lit le front matter YAML d'un article Markdown."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}

    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    if not match:
        return {}

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return {}

    return data if isinstance(data, dict) else {}


def as_list(value):
    """Transforme une valeur de métadonnée en liste normalisée."""
    if isinstance(value, list):
        values = value
    elif value:
        values = [value]
    else:
        values = []

    return {
        str(item).strip().casefold()
        for item in values
        if str(item).strip()
    }


def get_title(path, metadata):
    """Récupère le titre du front matter ou du premier titre Markdown."""
    title = metadata.get("title")
    if title:
        return str(title).strip()

    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass

    return path.stem.replace("-", " ").strip().capitalize()


def get_date(metadata):
    """Récupère la date de création dans les formats utilisés par le blog."""
    value = metadata.get("date", "")
    if isinstance(value, dict):
        value = value.get("created", "")
    return str(value or "")


def build_post(path):
    metadata = read_front_matter(path)
    return {
        "path": path,
        "title": get_title(path, metadata),
        "date": get_date(metadata),
        "categories": as_list(metadata.get("categories")),
        "tags": as_list(metadata.get("tags")),
        "draft": bool(metadata.get("draft", False)),
    }


def find_related_posts(current_path, limit=2):
    """Sélectionne les articles les plus proches du courant."""
    posts_dir = current_path.parent
    current = build_post(current_path)
    candidates = []

    for path in sorted(posts_dir.glob("*.md")):
        if path == current_path or path.name.startswith("_"):
            continue

        post = build_post(path)
        if post["draft"] or not post["date"]:
            continue

        shared_categories = current["categories"] & post["categories"]
        shared_tags = current["tags"] & post["tags"]
        score = (len(shared_categories) * 3) + len(shared_tags)

        candidates.append((score, post["date"], post))

    # Les catégories sont prioritaires. En cas d'égalité, l'article le plus récent passe devant.
    candidates.sort(key=lambda item: (-item[0], item[1]), reverse=False)

    # Pour les articles de même score, le tri par date doit être décroissant.
    candidates.sort(key=lambda item: item[1], reverse=True)
    candidates.sort(key=lambda item: item[0], reverse=True)

    return [item[2] for item in candidates[:limit]]


def has_existing_recommendations(markdown):
    """Évite de doubler une section déjà écrite manuellement."""
    return bool(
        re.search(
            r"(?im)^##\s+(?:À lire ensuite|Pour poursuivre)\s*$",
            markdown,
        )
    )


def render_related_posts(posts):
    if len(posts) < 2:
        return ""

    links = "\n".join(
        f"- [{post['title']}]({post['path'].name})"
        for post in posts
    )

    return (
        "\n\n## À lire ensuite\n\n"
        
        f"{links}\n"
    )


def on_page_markdown(markdown, **kwargs):
    """Ajoute automatiquement deux articles liés aux pages du blog."""
    page = kwargs.get("page")

    if not page or page.meta.get("template") != BLOG_POST_TEMPLATE:
        return markdown

    if has_existing_recommendations(markdown):
        return markdown

    source_path = Path(page.file.abs_src_path)
    if source_path.parent.name != "posts":
        return markdown

    related_posts = find_related_posts(source_path)
    return markdown.rstrip() + render_related_posts(related_posts)
