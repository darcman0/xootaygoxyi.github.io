import os
import yaml
import nbformat
import json


def get_md_metadata(filepath):
    """Lit le front matter d'un fichier .md de manière souple"""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    start = content.find("---")
    if start != -1:
        end = content.find("---", start + 3)
        if end != -1:
            try:
                res = yaml.safe_load(content[start+3:end])
                return res if isinstance(res, dict) else {}
            except:
                return {}
    return {}

def get_ipynb_metadata(filepath):
    """Lit le front matter dans la première cellule contenant des tirets."""
    try:
        nb = nbformat.read(filepath, as_version=4)
        for cell in nb.cells:
            if cell.cell_type in ["raw", "markdown"]:
                source = cell.source
                start = source.find("---")
                if start != -1:
                    end = source.find("---", start + 3)
                    if end != -1:
                        try:
                            parsed = yaml.safe_load(source[start+3:end])
                            if isinstance(parsed, dict) and "title" in parsed:
                                return parsed
                        except:
                            pass
    except:
        return {}
    return {}

def get_items(docs_dir, subfolder):
    """Filtre les brouillons et extrait les métadonnées."""
    folder = os.path.join(docs_dir, subfolder)
    items = []
    if not os.path.exists(folder):
        return items

    for filename in sorted(os.listdir(folder)):
        if filename in ["index.md", ".pages"]:
            continue
        if filename.startswith("_"):
            continue

        filepath = os.path.join(folder, filename)
        meta = {}

        if filename.endswith(".md"):
            meta = get_md_metadata(filepath)
            meta["_file"] = filename.replace(".md", "")
            meta["_notebook"] = False
        elif filename.endswith(".ipynb"):
            meta = get_ipynb_metadata(filepath)
            meta["_file"] = filename.replace(".ipynb", "")
            meta["_notebook"] = True
        else:
            continue

        if meta and meta.get("title"):
            items.append(meta)

    items.sort(key=lambda x: str(x.get("date", "") or ""), reverse=True)
    return items

def get_blog_title(filepath):
    """Récupère le premier titre Markdown d'un article."""
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
    return "Article sans titre"


def slugify_blog_title(title):
    """Produit le slug exact utilisé par le plugin blog de Material for MkDocs."""
    import re

    slug = title.lower().strip()
    
    # 1. Supprimer les apostrophes et guillemets (ex: l'ONU -> lonu)
    slug = re.sub(r"['’\"”«»]", "", slug)
    
    # 2. Remplacer les espaces par des tirets
    slug = re.sub(r"\s+", "-", slug)
    
    # 3. Supprimer les caractères spéciaux autres que lettres, chiffres, tirets et accents
    slug = re.sub(r"[^\w-]", "", slug, flags=re.UNICODE)
    
    return slug.strip("-")


def get_latest_blog_posts(docs_dir, limit=3):
    """Retourne les articles du blog triés du plus récent au plus ancien."""
    posts_dir = os.path.join(docs_dir, "blog", "posts")
    posts = []

    if not os.path.exists(posts_dir):
        return posts

    for filename in os.listdir(posts_dir):
        if not filename.endswith(".md") or filename.startswith("_"):
            continue

        filepath = os.path.join(posts_dir, filename)
        meta = get_md_metadata(filepath)
        date = meta.get("date", {})

        if isinstance(date, dict):
            date = date.get("created", "")

        if not date:
            continue

        # Material utilise le titre du front matter pour générer le slug.
        # Le titre Markdown reste une solution de secours pour les anciens articles.
        title = meta.get("title") or get_blog_title(filepath)
        posts.append({
            "title": title,
            "image": meta.get("image", ""),
            "description": meta.get("description", ""),
            "categories": meta.get("categories", []),
            "date": str(date),
            "url": f"blog/{slugify_blog_title(title)}/",
        })

    posts.sort(key=lambda post: post["date"], reverse=True)
    return posts[:limit]


def render_latest_blog_posts(posts):
    """Génère les cartes HTML des derniers articles."""
    cards = []

    for post in posts:
        categories = " · ".join(post["categories"])
        image = post.get("image", "")

        image_html = ""
        if image:
            image_html = f'''<img
                class="latest-post-image"
                src="{image}"
                alt="Illustration de : {post['title']}"
                loading="lazy"
            >'''

        cards.append(f"""
<div class="latest-post-card">
    {image_html}
    <div class="latest-post-card-content">
        <p class="latest-post-date">{post['date']} · {categories}</p>
        <h3>{post['title']}</h3>
        <a href="{post['url']}" class="md-button">Lire l'article →</a>
    </div>
</div>
""")

    return "<div class=\"latest-posts-grid\">" + "".join(cards) + "</div>"


def get_popular_blog_posts(docs_dir, limit=2):
    """Lit le classement généré chaque semaine par GoatCounter."""
    data_file = os.path.join(
        docs_dir,
        "assets",
        "data",
        "popular-articles.json",
    )

    if not os.path.exists(data_file):
        return []

    try:
        with open(data_file, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return []

    articles = data.get("articles", [])
    if not isinstance(articles, list):
        return []

    return articles[:limit]


def render_popular_blog_posts(posts):
    """Génère les cartes des articles les plus consultés."""
    if not posts:
        return "<p><em>Le classement sera disponible après les premières consultations.</em></p>"

    cards = []

    for post in posts:
        categories = post.get("categories", [])
        if isinstance(categories, list):
            categories = " · ".join(str(category) for category in categories)
        else:
            categories = str(categories)

        image = post.get("image", "")
        image_html = ""
        if image:
            image_html = f'''<img
                class="latest-post-image"
                src="{image}"
                alt="Illustration de : {post.get('title', 'Article')}"
                loading="lazy"
            >'''

        
        cards.append(f"""
<div class="latest-post-card popular-post-card">
    {image_html}
    <div class="latest-post-card-content">
        <p class="latest-post-date">{post.get('date', '')} · {categories}</p>
        <h3>{post.get('title', 'Article sans titre')}</h3>
        <a href="{post.get('url', '#')}" class="md-button">Lire l'article →</a>
    </div>
</div>
""")

    return '<div class="latest-posts-grid popular-posts-grid">' + "".join(cards) + "</div>"


def define_env(env):
    docs_dir = env.conf["docs_dir"]

    @env.macro
    def render_latest_posts(limit=3):
        posts = get_latest_blog_posts(docs_dir, limit)
        return render_latest_blog_posts(posts)
    
    @env.macro
    def render_popular_posts(limit=2):
        posts = get_popular_blog_posts(docs_dir, limit)
        return render_popular_blog_posts(posts)



    @env.macro
    def render_projects():
        items = get_items(docs_dir, os.path.join("realisations", "projects"))
        return _render_cards(items, "projects")

    @env.macro
    def render_apps():
        items = get_items(docs_dir, os.path.join("realisations", "apps"))
        return _render_cards(items, "apps")

def _render_cards(items, section):
    """Génère la grille de cartes au format propre."""
    if not items:
        return "<p><em>Aucun élément pour l'instant.</em></p>"

    if section == "projects":
        type_badge = '<span style="font-size:0.75rem;font-weight:600;padding:2px 8px;border-radius:12px;background:#e6f1fb;color:#185fa5">🗺️ Projet terrain</span>'
    else:
        type_badge = '<span style="font-size:0.75rem;font-weight:600;padding:2px 8px;border-radius:12px;background:#d4edda;color:#155724">🐍 App & Script</span>'

    status_colors = {
        "terminé":  ("#d4edda", "#155724", "✓ Terminé"),
        "en cours": ("#fff3cd", "#856404", "⟳ En cours"),
        "idée":     ("#e2e3e5", "#383d41", "✦ Idée"),
    }

    cards = []
    for item in items:
        title = item.get("title", "")
        description = item.get("description", "")
        tags = item.get("tags", [])
        status = item.get("status", "")
        image = item.get("image", "") or ""
        file_slug = item.get("_file", "")
        notebook = item.get("_notebook", False)

        # Images
        if image:
            img_html = f'<img src="{image}" alt="{title}" style="width:100%; height:180px; object-fit:cover; border-radius:4px; margin-bottom:0.75rem;">'
        elif notebook:
            img_html = '<img src="../../assets/images/placeholder-notebook.png" alt="Notebook" style="width:100%; height:180px; object-fit:cover; border-radius:4px; margin-bottom:0.75rem;">'
        else:
            img_html = '<img src="../../assets/images/placeholder-project.png" alt="Projet" style="width:100%; height:180px; object-fit:cover; border-radius:4px; margin-bottom:0.75rem;">'

        # Badges
        sc = status_colors.get(status.lower()) if status else None
        status_badge = f'<span style="font-size:0.75rem;font-weight:600;padding:2px 8px;border-radius:12px;background:{sc[0]};color:{sc[1]}">{sc[2]}</span>' if sc else ""
        notebook_badge = '<span style="font-size:0.75rem;font-weight:600;padding:2px 8px;border-radius:12px;background:#f3e8ff;color:#6b21a8;margin-left:4px">📓 Notebook</span>' if notebook else ""
        badges = f"{type_badge} {status_badge}{notebook_badge}"

        tags_str = " ".join([f"<code>{t}</code>" for t in tags]) if tags else ""
        href = f"{section}/{file_slug}/"
        
        # Structure HTML pure sans "markdown" dans la div
        card = f"""
<div class="project-card">
    {img_html}
    <div class="card-content">
        <p style="margin-bottom:0.5rem;">{badges}</p>
        <strong style="display:block; margin-bottom:0.5rem; font-size:1.1rem;">{title}</strong>
        <p style="font-size:0.9rem; margin-bottom:0.5rem;">{description}</p>
        <p style="margin-bottom:1rem;">{tags_str}</p>
        <a href="{href}" class="md-button">En savoir plus →</a>
    </div>
</div>
"""
        cards.append(card)

    return '<div class="grid">' + "\n".join(cards) + "</div>"
