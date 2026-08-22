# Journal des modifications

Ce fichier présente les principales évolutions du portfolio Xootay Gox Yi.

## Version 1.0.0

Date : 22 août 2026

Cette première version stable correspond au commit `94fe42f` et au tag Git `v1.0.0`.

Le site présente le travail d’Abdou Aziz Darc dans les domaines de la géomatique, des SIG, de la cartographie, de l’imagerie drone et des analyses spatiales au Sénégal.

La page d’accueil contient maintenant des cartes pour les articles récents et les articles les plus consultés. Les images, les dates, les catégories et les boutons ont été harmonisés pour rendre la présentation plus claire.

Le blog utilise les fonctionnalités de MkDocs Material pour les catégories, les archives, la pagination et le flux RSS. Les articles disposent également de métadonnées et de cartes de partage adaptées aux réseaux sociaux.

GoatCounter est utilisé pour suivre les consultations. Un workflow GitHub Actions met à jour chaque semaine la liste des articles populaires.

L’animation de particules est disponible sur toutes les pages. Elle peut être activée ou désactivée, et le choix est conservé dans le navigateur. Le site respecte aussi la préférence système de réduction des mouvements.

Le formulaire Contact possède un champ honeypot contre les robots et une validation de l’adresse e-mail. Le sitemap et le fichier robots.txt sont publiés automatiquement avec le site.

Le projet est construit avec MkDocs Material, Python et GitHub Actions. Le site est hébergé sur GitHub Pages. Les dépendances sont mises en cache dans le workflow de déploiement.

## Changements à venir

Les petites corrections validées du formulaire d’abonnement du blog et la protection contre les déploiements simultanés seront ajoutées dans le prochain commit global, après une dernière vérification locale.

## Convention de versionnement

Une version `v1.0.1` correspondra à une correction mineure. Une version `v1.1.0` pourra contenir une nouvelle fonctionnalité sans refonte importante. Une version `v2.0.0` sera réservée à une évolution majeure du site.

La version stable actuelle est disponible sur [GitHub](https://github.com/darcman0/xootaygoxyi.github.io/releases/tag/v1.0.0).
