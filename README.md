# Recommendation des films - comment peut-on améliorer les prédictions? 

## Introduction 
Ce projet est réalisé par Olivier PINATEL et Dariia HARYFULLINA pour le cours python pour la data science - ENSAE 2023 dispensé par Lino Galiana. 

L'objectif du projet est de travailler les connaissances acquises dans notre cours tout en les appliquant à un domaine qui nous passionne tous les deux - le cinéma. Nous nous sommes donc décidés à réproduire le fonctionnement des algroithmes de prédiction et essayer de tester si l'ajout des récompenses prestigieuses (les Oscars, les Césars, le Festival de Cannes et le Festival de Venise) améliore ou non la prédiction pour certains films. 

Nous pensons que les films qui sont recompensés dans ce type de concours ont des carcatéristiques similaires entre eux, sans pour autant que cela se reflète dans leur contenu ou leur genre, car la sélection se fait avec un certain nombre de critères similaires.

## Les étapes du projet 
### Etape 1 - récupération des données 
Nous avons décidé d'utiliser à la fois une API - The movie data base, ou TMDB, pour récupérer une base de données conséquente et exhaustive des 10 000 films les plus populaires. Nous avons récupéré une clé pour 

Nous avons completé cette base par une étape de web scrapping sur Wikipédia des tables qui rescencent les nominations aux différentes catégories pour les compétitions de cinéma prestigieuses - les Oscars, les Césars et les festivals - Cannes et Venise. Les catégories concernées sont la meilleure cinématographie, le meilleur film et le meilleur réalisteur pour les Oscars, le meilleur réalisateur et le meilleur film pour les Césars, la palme d'or le grand prix et le prix du jury pour les Cannes, et lion d'or, lion d'argent et le grand prix du jury pour Venise. 
### Etape 2 - nettoyage et fusion 
Après avoir finaliser la partie récupération, nous sommes passés à l'étape du nettoyage des données. En effet, les bases récupérées sur l'API 

En ce qui concerne les tables scrappées sur Wikipédia, le nettoyage a été particulièrement laborieux. En particulier, le format différent de chaque table et page sur Wikipédia nous a forcés à reprendre chaque catégorie pour chaque compétition une à une, et supprimer certaines données manuellement. Nous avons également créé des variables binaires (award_mains et award_fest) dans cette partie pour enregistrer la nomination dans l'une des catégories et pouvoir l'exploiter dans nos analyses. 

Après avoir finalisé le nettoyage, nous avons joint les deux bases en utilisant le titre de film et l'année de la parution pour les deux tables, pour retrouver une seule et unique base finale sur laquelle nous travaillons pour la visualisation des données et la modélisation. 
### Visualisation 
Dans la partie visualisation, en plus de quelques statistiques descriptives de notre dataset, nous avons decidé de travailler avec les wordcloud (nuages de mots) et essayer de suivre une évolution temporelle des budgets de films, ou leur notes moyennes. L'analyse se faisait selo le genre, la nomination dans l'une des catégories de compétitions cinématographiques, la décennie ou l'année. Nous avons également analysé plusieurs synopsis en réalisant des nuages de mots et comprendre la différence entre plusieurs genres en ce termes pour mieux préparer l'étape de la modélisation. 
### Modélisation et construction des algorithmes 

## Navigation dans le dépôt 
Cette partie a pour objectif de décrire la structure de notre dépôt git pour mieux s'y retrouver. 
Voici la liste des dossiers et la description des fichiers pour comprendre notre cheminement. 
* API 
* wiki_scrap
* visualiser
* cleaning_data
* modeliser

## Documentation et références 
