# Xootay Gox Yi

Portfolio personnel d’**Abdou Aziz Darc**, géographe, géomaticien et télépilote basé au Sénégal.

Le site présente des projets, tutoriels et ressources autour de la **géomatique open source**, des systèmes d’information géographique, de la cartographie, de l’imagerie drone et des analyses spatiales.

Site public : [xootaygoxyi.com](https://xootaygoxyi.com/)

## Version stable

La version stable actuellement publiée est [`v1.0.0`](https://github.com/darcman0/xootaygoxyi.github.io/releases/tag/v1.0.0).

## Technologies utilisées

- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) pour la documentation et le thème du site ;
- [GitHub Pages](https://pages.github.com/) pour l’hébergement ;
- [GitHub Actions](https://github.com/features/actions) pour la construction et le déploiement automatiques ;
- Python pour les scripts d’automatisation et les extensions MkDocs ;
- GoatCounter pour les statistiques respectueuses de la vie privée ;
- Giscus pour les commentaires des articles de blog.

## Développement local

Créer ou activer l’environnement Python local, puis installer les dépendances du projet :

```bash
conda activate portfolio
python -m pip install -r requirements.txt
```

Pour prévisualiser le site pendant les modifications :

```bash
mkdocs serve
```

Le site local est alors disponible à l’adresse `http://127.0.0.1:8000/`.

Pour effectuer une vérification complète du build :

```bash
mkdocs build --clean
```

Le dossier `site/` est généré automatiquement et ne doit pas être modifié manuellement ni ajouté au dépôt.

## Publication

Chaque push sur la branche `main` déclenche le workflow GitHub Actions de construction et de déploiement vers GitHub Pages. Avant une publication, il est recommandé de vérifier le build local, le statut Git et les fichiers réellement inclus dans le commit.

```bash
git status --short
git diff --stat
git pull --rebase origin main
git push origin main
```

Les versions stables sont identifiées avec des tags Git, par exemple `v1.0.0`. Une évolution majeure pourra être identifiée plus tard par `v2.0.0`, tandis qu’une amélioration progressive pourra utiliser `v1.1.0`.

## Structure principale

```text
docs/                  Contenu du site MkDocs
  blog/                Articles et ressources du blog
  realisations/        Projets et réalisations
  assets/              Images, CSS, JavaScript et données
overrides/             Personnalisation des templates Material
hooks/                 Extensions de rendu MkDocs
scripts/               Scripts d’automatisation
layouts/               Modèles des cartes sociales
.github/workflows/     Workflows de build, déploiement et statistiques
mkdocs.yml             Configuration principale du site
requirements.txt       Dépendances utilisées par le CI
```

## Règles de contribution au projet

Les modifications doivent être testées localement avant publication. Les pages **Réalisations** et **Publications** sont conservées séparément afin d’éviter toute réorganisation involontaire du contenu existant.

Les secrets et jetons d’API ne doivent jamais être écrits dans le dépôt, les scripts ou les messages de commit. Ils doivent rester configurés dans les secrets GitHub appropriés.

## Licence et contact

Pour toute question, proposition de collaboration ou signalement, consultez la [page Contact](https://xootaygoxyi.com/contact/).
