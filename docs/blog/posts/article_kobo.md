---
date: 
  created: 2025-05-18
authors:
  - darc
categories:
  - Enquetes
---

# KOBO

Cela vous est-il déjà arrivé d’avoir la flemme de vous rendre sur le site de [Kobotoolbox](https://kc.kobotoolbox.org/) pour télécharger vos données issues de votre campagne de collecte?

Si oui, voici un **tips** qui vous fera gagner énormément de temps.

Pour cela on utilisera la première version de l’API de Kobotoolbox. Parlons d’abord de ce que c’est une API. Une API (application programming interface ou « interface de programmation d'application ») est une interface logicielle qui permet de « connecter » un logiciel ou un service à un autre logiciel ou  service afin d'échanger des données et des fonctionnalités (il y’a certains lecteurs dès qu’ils ont vu #programming, ils sont passés à autre chose 😆).

<!-- more -->

Concrètement, on va connecter le serveur de #Kobotoolbox à un logiciel (ici Microsoft excel) pour recevoir de manière automatique les données collectées.

Il faut d’abord se connecter sur votre compte #Kobotoolbox et écrire sur la barre de l’URL :

   [Kobotoolbox](https://kc.kobotoolbox.org/api/v1/data)

Cet URL va nous permettre d’accéder à la fenêtre de programmation de l’API.

Il faut maintenant faire clique gauche sur la flèche à droite de GET et sélectionner json

Une nouvelle page s'ouvre, dans celle-ci vous aurez l’ensemble des formulaires que vous avez déployé

A ce niveau, moi j'ai trois formulaires déployés dont l’id est propre à chacun en plus il y a la description et le titre de chacun de ces formulaires mais aussi l’URL menant à chacun des formulaires.

Il faut copier l’URL du formulaire cible (dont on veut récupérer les données de manière automatique), ici moi je copie l’URL du projet : Test_api__V1

    https://kc.kobotoolbox.org/api/v1/data/1964678?format=json

    Ensuite ouvrir le logiciel Microsoft excel 

    Puis se rendre sur le menu data ou donnée ( en fonction de la langue du système)

    Cliquez sur From web ou à partir du web

Dans la nouvelle fenêtre qui s’ouvre, il faut collé l’URL qui a été auparavant copié à partir de la page de l’API. Mais en écrivant à la place de ?format=json : 

    .XLSX et cliquer sur OK

Après cela une fenêtre permettant de voir les données de notre formulaire cible s’ouvre, faut sélectionner la feuille (avec les caractéres alphanumériques mélangés) et cliquer sur LOAD 

La magie devrait s'opérer 🎉

Sinon, si un message d’erreur apparaît, il frauda juste se rendre sur votre compte Kobotoolbox et naviguer à partir du formulaire (dont vous voulez récupérer les données) vers PARAMÈTRES PUIS Partage et s’assurer que soit cochez les cases :

    N’importe qui peut afficher ce formulaire 

    N’importe qui peut afficher les soumissions de ce formulaire

Essayez d'actualiser votre logiciel Excel à partir du menu Data ou Donnée et le tour devrait être joué. J’espère que vous y êtes parvenu. Sinon contactez moi, je serai ravie de vous aiguiller.

Qui suis je?

Abdou Aziz Darc, un féru de géomatique qui aime partager ses connaissances.