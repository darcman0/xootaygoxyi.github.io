---
date:
  created: 2026-09-05
image: https://upload.wikimedia.org/wikipedia/commons/c/cd/Equal-Earth-Map-150E.jpg
authors:
  - darc
categories:
  - Cartographie
  - Géopolitique
  - SIG
tags:
  - Togo
  - ONU
  - Equal Earth
  - Mercator
  - Sénégal
  - Projections cartographiques
  - EPSG
title: "Equal Earth : le Togo ouvre un débat cartographique à l'ONU"
description: "La résolution portée par le Togo à l'ONU remet Equal Earth et le choix des projections cartographiques au centre du débat sur la représentation de l'Afrique."

---

# Le Togo porte à l'ONU une nouvelle bataille cartographique autour d'Equal Earth

![Carte mondiale Equal Earth](https://upload.wikimedia.org/wikipedia/commons/c/cd/Equal-Earth-Map-150E.jpg){ .img-center }
*Carte mondiale politique en projection Equal Earth. Auteur : Tom Patterson, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Equal-Earth-Map-150E.jpg), image placée dans le domaine public.*

Le 4 septembre 2026, l'Assemblée générale des Nations Unies a adopté la résolution **A/80/L.104**, intitulée *Correct the map: rebalancing global cartographic representation and promoting equitable representation of the world's regions, particularly Africa*. Le texte a été approuvé par **164 voix contre une**, avec **six abstentions** <sup>[1](https://news.un.org/fr/story/2026/09/1159416)</sup> <sup>[2](https://press.un.org/en/2026/ga12779.doc.htm)</sup>. Le texte officiel est disponible dans la bibliothèque numérique des Nations Unies <sup>[7](https://docs.un.org/A/80/L.104)</sup>.
<!-- more -->
Présentée au nom du Groupe des États africains, la résolution encourage un recours plus large aux projections cartographiques équivalentes, notamment à **Equal Earth**, lorsque la comparaison des superficies constitue l'objectif principal de la carte. Elle ne bannit toutefois pas la projection de Mercator et n'impose pas une carte unique aux États, aux écoles ou aux entreprises technologiques.

La précision est importante. L'ONU n'a pas décrété la disparition de Mercator. Elle a accordé un soutien politique à une autre manière de représenter le monde, plus attentive aux superficies relatives et aux effets culturels des choix cartographiques.



---

## Pourquoi la projection de Mercator est-elle contestée ?

La projection de Mercator a été conçue au XVIe siècle pour répondre à un objectif précis : faciliter la navigation maritime. Elle conserve localement les angles et représente les **loxodromies**, c'est-à-dire les trajectoires qui coupent les méridiens sous un angle constant, sous la forme de lignes droites.

Ces propriétés expliquent son intérêt historique pour la navigation et certains usages techniques. En revanche, Mercator déforme fortement les superficies à mesure que l'on s'éloigne de l'équateur. Les régions proches des pôles apparaissent beaucoup plus grandes qu'elles ne le sont réellement.

Le Groenland peut ainsi sembler comparable à l'Afrique sur certaines cartes, alors que la superficie de l'Afrique est environ quatorze fois supérieure <sup>[3](https://www.reuters.com/world/africa/un-approves-resolution-support-map-that-shows-africas-true-size-2026-09-04/)</sup>. Le problème ne vient pas d'une erreur de calcul. Il résulte du compromis mathématique propre à la projection.

Il est impossible de représenter une surface sphérique sur un plan sans déformer au moins une propriété géométrique. La question porte donc sur le choix de la propriété que l'on souhaite préserver et sur l'usage que l'on fait ensuite de la carte.

!!! warning "Une projection n'est jamais neutre"
    Lorsque Mercator devient la représentation dominante dans les manuels scolaires, les atlas, les médias et les interfaces numériques, sa déformation des superficies peut influencer durablement la perception de l'importance relative des régions du monde.

---

## Equal Earth, une projection équivalente pour les cartes mondiales

La projection **Equal Earth** a été conçue en 2018 par les cartographes Bojan Šavrič, Tom Patterson et Bernhard Jenny. Il s'agit d'une projection pseudo-cylindrique équivalente, c'est-à-dire une projection qui conserve les superficies relatives des territoires représentés <sup>[4](https://equal-earth.com/equal-earth-projection.html)</sup> <sup>[5](https://proj.org/operations/projections/eqearth.html)</sup>. La publication scientifique consacrée à sa conception est disponible dans l'*International Journal of Geographical Information Science* <sup>[6](https://doi.org/10.1080/13658816.2018.1504949)</sup>.

Son apparence générale rappelle certaines projections utilisées dans les atlas, notamment la projection de Robinson. Toutefois, Equal Earth s'en distingue par la conservation des aires. Ses parallèles sont droits et ses bords courbés suggèrent la forme sphérique de la Terre.

| Critère | Projection de Mercator | Projection Equal Earth |
|---|---|---|
| Propriété principale | Conservation locale des angles | Conservation des superficies relatives |
| Usage historique | Navigation et cartes à grande échelle | Cartes mondiales et comparaison des territoires |
| Superficies aux hautes latitudes | Fortement agrandies | Représentées selon leur proportion relative |
| Formes et angles | Angles localement conservés, formes globales déformées | Formes et angles déformés selon la position |
| Limite principale | Perception exagérée des régions polaires | Ne convient pas à la navigation ni à tous les usages locaux |

Equal Earth ne constitue donc pas une carte parfaite. Elle répond à une priorité différente. Elle est pertinente lorsque le lecteur doit comparer la taille des continents, des États ou de grands ensembles territoriaux.

Elle ne remplace pas automatiquement une projection conforme, équidistante ou azimutale lorsque l'objectif est de préserver les angles, les distances ou les directions.

![Exemple de projection azimutale équidistante en vue polaire](https://upload.wikimedia.org/wikipedia/commons/e/ec/Azimuthal_equidistant_projection_SW.jpg){ .img-center }
*Une autre famille de projections : l'azimutale équidistante, utile pour préserver les distances depuis un point central. Image : Strebe, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Azimuthal_equidistant_projection_SW.jpg), licence [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).*

---

## Que change Equal Earth pour la représentation du Sénégal ?

Le Sénégal se situe entre environ **12° et 17° de latitude nord**. À l'échelle d'une carte mondiale, cette position reste relativement proche de l'équateur. La déformation des superficies produite par Mercator y est donc moins spectaculaire que dans les régions arctiques.

Elle n'est toutefois pas nulle. Dans une approximation sphérique, le facteur d'agrandissement des superficies augmente avec la latitude selon le carré de la sécante. À la latitude moyenne du Sénégal, l'inflation surfacique se situe dans l'ordre de quelques pour cent. Elle devient plus importante dans la partie nord du pays.

Sur une carte mondiale en Mercator, le Sénégal apparaît donc légèrement agrandi par rapport à sa superficie réelle. L'écart devient surtout visible lorsque le pays est comparé à des territoires situés à des latitudes élevées.

Equal Earth rétablit les proportions relatives des superficies. Le Sénégal occupe alors une part de la carte plus cohérente avec sa superficie réelle, au même titre que les autres pays africains et les autres régions du monde.

| Question cartographique au Sénégal | Mercator | Equal Earth |
|---|---|---|
| Comparer la superficie du Sénégal à celle d'autres pays | Moins adaptée à l'échelle mondiale en raison de l'inflation liée à la latitude | Adaptée, car les superficies relatives sont conservées |
| Représenter les angles et les directions localement | Propriété mieux conservée | Déformation possible selon la position |
| Mesurer précisément des distances ou des surfaces dans le pays | À éviter sans précautions, surtout sur une carte mondiale | À réserver à la visualisation mondiale malgré la conservation des aires |
| Produire une carte scolaire ou thématique mondiale | Possible, mais l'effet de taille doit être expliqué | Pertinente lorsque la superficie constitue le message principal |
| Représenter la navigation et les trajectoires | Historiquement adaptée à certains usages | Non destinée à cet usage |

Autrement dit, Equal Earth ne rend pas le Sénégal plus grand. Elle évite surtout qu'une même règle de projection agrandisse artificiellement certains territoires et en réduise visuellement d'autres dans une comparaison mondiale.

À l'échelle nationale, la différence peut sembler modérée. À l'échelle du planisphère, elle contribue toutefois à une lecture plus équilibrée de l'Afrique.

---

## Ne pas confondre système de coordonnées et projection

Le débat autour d'Equal Earth rappelle une distinction fondamentale en géomatique : un système de coordonnées géographiques n'est pas une projection cartographique.

Un **système de coordonnées géographiques**, ou GCS, décrit la position des objets par latitude et longitude, généralement en degrés. Le système le plus courant est **WGS 84, EPSG:4326**. Il sert à stocker, échanger et localiser les données. Il ne correspond pas à la projection d'affichage d'une carte plane.

Une **projection cartographique** transforme ensuite ces coordonnées géographiques en coordonnées planes. Le résultat est un système de coordonnées projetées, ou PCS, dont les axes sont généralement exprimés en mètres.

Mercator et Equal Earth sont des méthodes de projection. Elles peuvent toutes deux partir du référentiel géodésique WGS 84, tout en produisant des coordonnées planes différentes.

Pour Equal Earth, le système couramment utilisé pour une carte mondiale centrée sur Greenwich est **WGS 84 / Equal Earth Greenwich, EPSG:8857** <sup>[8](https://epsg.io/8857)</sup>. Ses coordonnées sont exprimées en mètres. Il ne faut donc pas remplacer EPSG:4326 par EPSG:8857 en pensant qu'il s'agit simplement d'un autre format de latitude et longitude.

Pour Mercator, plusieurs systèmes existent :

- **EPSG:3395**, WGS 84 / World Mercator, fondé sur une formulation ellipsoïdale ;
- **EPSG:3857**, WGS 84 / Pseudo-Mercator, très utilisé par les fonds de carte web.

Le code EPSG doit donc toujours être vérifié. Le simple nom « Mercator » ne suffit pas à identifier le système réellement utilisé.

---

## Quel CRS choisir pour les données du Sénégal ?

Pour les mesures locales au Sénégal, Equal Earth n'est généralement pas le meilleur choix, même si elle conserve les superficies à l'échelle mondiale.

Une projection UTM adaptée à la zone d'étude est souvent plus pertinente :

| Zone UTM | Code EPSG | Emprise approximative |
|---|---:|---|
| UTM 28N | EPSG:32628 | De 18° Ouest à 12° Ouest |
| UTM 29N | EPSG:32629 | De 12° Ouest à 6° Ouest |

Le choix dépend de la longitude de la zone de travail et de l'emprise du projet. Pour une étude couvrant une grande partie du pays, il peut être préférable d'évaluer une projection nationale ou une projection équivalente adaptée à l'objectif, plutôt que de juxtaposer deux zones UTM sans analyse <sup>[10](https://epsg.io/32628)</sup> <sup>[11](https://epsg.io/32629)</sup>.

Dans QGIS, la bonne pratique consiste à conserver les données sources dans leur CRS documenté, souvent **EPSG:4326**, puis à reprojeter une copie vers le système adapté à la visualisation ou au calcul <sup>[9](https://docs.qgis.org/latest/en/docs/gentle_gis_introduction/coordinate_reference_systems.html)</sup>.

Avec GeoPandas :

```python
import geopandas as gpd

senegal = gpd.read_file("senegal.gpkg")

print(senegal.crs)

senegal_equal_earth = senegal.to_crs("EPSG:8857")

senegal_utm28 = senegal.to_crs("EPSG:32628")
```

La reprojection change les coordonnées utilisées pour dessiner ou mesurer la géométrie. Elle ne change pas la position géographique du Sénégal.

!!! info "Bonne pratique"
    Avant toute mesure de distance ou de superficie, vérifier le CRS de la couche et celui du projet. L'affichage correct d'une géométrie ne garantit pas que le système choisi soit adapté au calcul.

En pratique, le GCS décrit le lien avec la Terre, tandis que le PCS définit la manière de représenter cette géométrie sur un plan. Une même couche peut ainsi être affichée en EPSG:4326, en Mercator ou en Equal Earth sans que le territoire lui-même ait changé.

---

## Le rôle diplomatique du Togo

![Salle de l'Assemblée générale des Nations Unies à New York](https://upload.wikimedia.org/wikipedia/commons/0/05/UN_General_Assembly_hall.jpg){ .img-center }
*La résolution sur la représentation cartographique a été adoptée par l'Assemblée générale des Nations Unies. Photo : Patrick Gruban, recadrage par Pine, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:UN_General_Assembly_hall.jpg), licence [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/).*

Le Togo présente cette résolution comme une initiative en faveur d'une représentation plus équitable du monde, et non comme une attaque contre une tradition cartographique particulière.

Le ministre togolais des Affaires étrangères, Robert Dussey, a présenté la carte comme un outil cognitif qui influence la manière dont les générations apprennent à voir le monde <sup>[1](https://news.un.org/fr/story/2026/09/1159416)</sup> <sup>[2](https://press.un.org/en/2026/ga12779.doc.htm)</sup>.

Cette position inscrit la cartographie dans un débat plus large sur :

- les héritages coloniaux ;
- la production et la diffusion des savoirs ;
- la place de l'Afrique dans les représentations internationales ;
- l'influence des supports scolaires et numériques ;
- le rapport entre choix techniques et rapports de pouvoir.

Pour les promoteurs du texte, corriger les disproportions visuelles de certaines cartes revient à reconnaître que les régions tropicales et équatoriales ne doivent pas apparaître réduites par le seul effet d'une projection conçue pour un autre objectif.

Selon Reuters, le Togo souhaite modifier ses supports scolaires avant la fin de l'année 2026 et encourager d'autres gouvernements, établissements d'enseignement, organisations internationales et entreprises technologiques à utiliser davantage Equal Earth ou d'autres projections équivalentes <sup>[3](https://www.reuters.com/world/africa/un-approves-resolution-support-map-that-shows-africas-true-size-2026-09-04/)</sup>.

Cette orientation pourrait concerner :

- les atlas scolaires ;
- les cartes murales ;
- les plateformes éducatives ;
- les supports institutionnels ;
- les interfaces numériques ;
- les cartes mondiales utilisées dans les médias.

Le vote offre ainsi au Togo une visibilité diplomatique particulière. Un État de taille limitée peut peser sur un débat mondial lorsqu'il porte une question à la fois technique, symbolique et directement liée à l'éducation.

La cartographie devient alors un instrument de diplomatie culturelle et de rééquilibrage des récits géographiques.

---

## Une résolution politique, mais non contraignante

La résolution adoptée par l'Assemblée générale n'a pas de force obligatoire. Elle formule une orientation politique et pédagogique. Elle encourage les acteurs publics et privés à choisir des projections équivalentes lorsque la comparaison des superficies est pertinente, mais elle ne prescrit pas une norme unique <sup>[1](https://news.un.org/fr/story/2026/09/1159416)</sup> <sup>[2](https://press.un.org/en/2026/ga12779.doc.htm)</sup> <sup>[3](https://www.reuters.com/world/africa/un-approves-resolution-support-map-that-shows-africas-true-size-2026-09-04/)</sup>.

Le texte précise également que la représentation cartographique ne règle aucune question de souveraineté, de statut territorial, de délimitation ou de frontières internationalement reconnues.

Cette clarification répond notamment aux préoccupations exprimées par l'Ukraine concernant la représentation de territoires temporairement occupés dans Equal Earth <sup>[2](https://press.un.org/en/2026/ga12779.doc.htm)</sup>.

Les États-Unis ont voté contre le texte, qu'ils ont présenté comme lié à un projet idéologique plus large et comme une distraction par rapport aux priorités centrales de l'Organisation.

Cette opposition rappelle qu'une carte mondiale peut devenir un objet diplomatique sensible dès lors qu'elle est associée à la justice historique, aux réparations ou aux rapports de pouvoir.

La portée du vote doit donc être évaluée avec précision. Il ne transformera pas les pratiques cartographiques du jour au lendemain. Toutefois, il donne une légitimité internationale à une demande portée par le Groupe des États africains et ouvre un espace de discussion sur les cartes utilisées dans l'enseignement et la communication publique.

---

## Ce que cette initiative change pour les géomaticiens

Pour les professionnels de la géomatique, le débat ne doit pas se réduire à l'opposition entre une « mauvaise » projection et une « bonne » projection.

Le choix dépend toujours :

- de l'échelle de travail ;
- de l'emprise géographique ;
- de la variable représentée ;
- du type d'analyse ;
- de la précision recherchée ;
- de la finalité de la carte.

Equal Earth peut être pertinente pour une carte mondiale thématique consacrée :

- aux superficies ;
- à la répartition des ressources ;
- aux émissions de gaz à effet de serre ;
- aux populations ;
- aux grands ensembles territoriaux ;
- aux comparaisons entre continents ou États.

Pour une analyse locale, une carte de navigation, une mesure de distance ou une représentation exigeant la conservation des angles, d'autres projections seront plus adaptées.

L'enjeu principal est donc la **transparence du choix cartographique**. Une carte devrait indiquer sa projection lorsque celle-ci influence l'interprétation du phénomène représenté. Elle devrait également éviter de présenter une projection comme une vision neutre et universelle du monde.

Les outils SIG modernes permettent de changer de projection selon les besoins, à condition de distinguer correctement les données géographiques, le référentiel géodésique, le système de coordonnées, la projection d'affichage, la méthode de mesure et l'objectif de représentation.

Dans cette perspective, la résolution portée par le Togo peut être comprise comme un appel à renforcer la culture cartographique. Elle invite les enseignants, les géomaticiens, les éditeurs et les développeurs à expliquer ce que chaque projection conserve, ce qu'elle déforme et pourquoi elle a été choisie.

---

## Une carte plus juste ne supprime pas les déformations

L'intérêt d'Equal Earth réside dans sa capacité à restituer les proportions relatives des superficies. Sa limite rappelle toutefois qu'aucune projection plane ne peut préserver simultanément toutes les propriétés géométriques d'un globe.

Une carte plus juste du point de vue des superficies peut donc rester déformée en ce qui concerne :

- les formes ;
- les angles ;
- les distances ;
- les directions ;
- les relations locales entre les objets.

Le véritable apport de l'initiative togolaise se situe peut-être dans cette prise de conscience. Elle ne demande pas seulement de remplacer une image par une autre. Elle invite à considérer la carte comme une construction scientifique et sociale, conçue pour un usage précis et porteuse de choix de représentation.

Le vote de l'ONU ne fera pas disparaître Mercator. Il pourrait néanmoins accélérer la diversification des cartes utilisées dans les écoles, les institutions et les plateformes numériques.

Dans ce débat, le Togo défend une idée simple : représenter les superficies avec davantage de fidélité peut contribuer à représenter les régions du monde avec davantage d'équité.

---

## Références

1. [L'ONU soutient la campagne africaine pour redessiner la carte du monde](https://news.un.org/fr/story/2026/09/1159416), ONU Info, 4 septembre 2026.
2. [General Assembly Adopts Text to “Correct the Map”](https://press.un.org/en/2026/ga12779.doc.htm), United Nations Meetings Coverage, 4 septembre 2026.
3. [UN approves resolution in support of map that shows Africa's true size](https://www.reuters.com/world/africa/un-approves-resolution-support-map-that-shows-africas-true-size-2026-09-04/), Reuters, 4 septembre 2026.
4. [Equal Earth projection](https://equal-earth.com/equal-earth-projection.html).
5. [Equal Earth, documentation PROJ](https://proj.org/operations/projections/eqearth.html).
6. [The Equal Earth map projection](https://doi.org/10.1080/13658816.2018.1504949), Šavrič, Patterson et Jenny, *International Journal of Geographical Information Science*, 2019.
7. [Résolution A/80/L.104](https://docs.un.org/A/80/L.104), Bibliothèque numérique des Nations Unies.
8. [EPSG:8857, WGS 84 / Equal Earth Greenwich](https://epsg.io/8857).
9. [Coordinate Reference Systems](https://docs.qgis.org/latest/en/docs/gentle_gis_introduction/coordinate_reference_systems.html), documentation QGIS.
10. [EPSG:32628, WGS 84 / UTM zone 28N](https://epsg.io/32628).
11. [EPSG:32629, WGS 84 / UTM zone 29N](https://epsg.io/32629).

