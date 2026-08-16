---
date: 
  created: 2025-04-10
  updated: 2026-08-16

authors:
  - darc
categories:
  - Terrain
  - Drone

description: Retour d'expérience sur la cartographie d'environ 7000 hectares de reboisements de mangrove pour WeForest dans le Sine-Saloum et la Casamance. 
---

# Cartographier près de 3 000 ha de mangroves pour WeForest : retour de terrain

Entre juillet 2025 et janvier 2026, j'ai participé à la cartographie aérienne d'environ 7 000 hectares de reboisements de mangrove dans les îles du Sine-Saloum et en Casamance pour le compte de WeForest, via Earth Géomatique. 750 sites, plusieurs types de drones, des conditions de terrain extrêmes. Voici ce que j'en retiens.

![Vue aérienne d'un site de mangrove pris par drone](https://assets.xootaygoxyi.com/assets/blog/mangroves_we_forest_terrain/DJI_20250711100605_0001_V.JPG){ .img-center }



<!-- more -->

---

## Le projet en chiffres

|Dénomination | Description| 
|------|------|
| Surface totale | ~7 000 ha |
| Nombre de sites | 750 |
| Résolution orthophoto | 2 cm |
| Drones utilisés | DJI Air 2s, Mavic 3 Entreprise, Mavic 3 Mini Pro |
| Planification de vol | Mission Planner |
| Outil de suivi terrain | QField |
| Logiciel de traitement | Agisoft Metashape Professional |
| Gain de temps traitement | −20% grâce à l'automatisation |

---

## Les défis du terrain

### Accessibilité des sites

Le Sine-Saloum est un archipel de bolongs, de chenaux et de mangroves denses. Certains sites ne sont accessibles qu'en pirogue, avec du matériel drone à protéger de l'humidité et des éclaboussures. À cela s'ajoutait une contrainte propre à l'objet cartographié : sur l'ensemble des 750 sites (300 environs été localisé dans le Sine-Saloum), les jeunes pousses de mangrove devaient être visibles et non recouvertes d'eau au moment du vol, ce qui imposait de ne travailler qu'en marée basse.

**Solution :** Sacs de protection pour les batteries et les télécommandes, certains étanches et d'autres non, mais les batteries étaient systématiquement mises en sécurité dans ces sacs. Chaque mission était calée sur les horaires de marée basse du site, avec en plus une contrainte de lumière : on cherchait à toujours voler en présence de soleil, donc on débutait très tôt et on terminait bien avant le coucher du soleil, le tout en restant dans la fenêtre de marée basse disponible.


### Couverture nuageuse

En saison des pluies, la couverture nuageuse peut invalider des orthophotos entières, car les ombres créent des discontinuités radiométriques inutilisables pour la détection de changement.

**Solution :** Planification des vols par fenêtres météo (application Nautide + observation locale). 

### Autonomie batterie sur zones étendues

Un site de 10–15 ha nécessite 2 à 3 batteries consécutives. La gestion des rotations de batteries en terrain isolé, sans accès à l'électricité, est un défi logistique réel, d'autant plus qu'on était 3 télépilotes à faire tourner du matériel en parallèle.

**Solution :** Chaque télépilote disposait de près de 8 batteries, ce qui donnait de la marge pendant la journée. Le groupe électrogène permettait de recharger la moitié des batteries sur place, en complément des powerbanks de 20 000 mAh pour les téléphones et les radiocommandes.

---

## Planification des vols avec Mission Planner

Les plans de vol ont été préparés avec Mission Planner, en tenant compte des contraintes de marée basse et d'accès en pirogue propres à chaque site : chaque mission ne pouvait se faire que sur la fenêtre de marée basse disponible ce jour-là, avec pour objectif de rester dans les heures de soleil. Chaque mission était ajustée site par site (altitude, recouvrement, orientation des bandes de vol) selon la forme et la densité de la mangrove à couvrir.

---

## L'organisation des 300 sites avec QField

QField a été central dans la gestion de la mission. Voici notre workflow :

1. **Préparation dans QGIS** : Pour les 300 sites, avec attributs (ID site, surface estimée, statut, date prévue, commentaires)
2. **Synchronisation sur QField** : chaque télépilote pouvait renseigner les sites qu'il a survoler et voir ce qui on déja été survolée à partir de son téléphone en temps réelle
3. **Sur le terrain** : remplissage du statut (volé / à re-voler / problème technique), ajout de photos géolocalisées
4. **Chaque soir** : traitement de toutes les images de la journée et export des orthophotos, pour repérer rapidement les sites à re-voler avant de quitter la zone
5. **Synchronisation en fin de journée** : mise à jour de la base centrale via QFieldCloud

---

## Le traitement dans Metashape

Pour gagner du temps sur 300 lots d'images, j'ai mis en place un traitement par lot (batch process) dans Metashape, configuré comme une chaîne unique appliquée automatiquement à chaque chunk : un premier alignement des photos, un recalage par référence, un second alignement affiné à partir des points-clés conservés, puis la construction du MNT et de l'orthomosaïque, le tout projeté directement en UTM 28N (EPSG:32628).

Deux réglages ont fait une vraie différence sur ce terrain : le filtre anti-fantôme (ghosting filter) sur l'orthomosaïque, pour limiter les artefacts causés par le mouvement des palétuviers sous le vent entre deux prises de vue, et la double passe d'alignement, qui améliore nettement la précision sur les zones à faible texture comme les tannes de mangrove denses.

Appliqué via le batch processing de Metashape sur des dossiers organisés par site, ce traitement a réduit le temps de traitement moyen de **20%** en éliminant les étapes manuelles répétitives entre chaque lot.

---

## Ce que j'ai appris

!!! success "Ce qui a bien fonctionné "
    - QField pour le suivi en temps réel des 300 sites : indispensable
    - Caler chaque vol sur la marée basse tout en restant dans la fenêtre de soleil : lumière rasante, mangroves encore humides donc contraste maximal
    - Recouvrement frontal/latéral à 80%/70% : moins de trous dans les zones denses

!!! warning "Ce que je referais différemment "
    - Nous n'avons utilisé ni GCP ni RTK sur cette mission : prévoir au moins des GCP même sur des zones plates aurait amélioré la précision verticale
    - Documenter les sites problématiques dès le terrain plutôt qu'en post-traitement
    - Utiliser systématiquement le Mavic 3 Entreprise plutôt que l'Air 2s pour les zones critiques : son obturateur mécanique et sa meilleure stabilité face aux vents forts, fréquents sur zone, donnaient des orthophotos de meilleure qualité

---

*Mission réalisée avec Earth Géomatique pour WeForest, Sénégal, 2025.*