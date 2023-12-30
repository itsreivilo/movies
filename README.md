# Recommendation des films - comment peut-on améliorer les prédictions? 

## Introduction 
Ce projet est réalisé par Olivier PINATEL et Dariia HARYFULLINA pour le cours python pour la data science - ENSAE 2023 dispensé par Lino Galiana. 

L'objectif du projet est de travailler les connaissances acquises dans notre cours tout en les appliquant à un domaine qui nous passionne tous les deux - le cinéma. Nous nous sommes donc décidés à réproduire le fonctionnement des algroithmes de prédiction et essayer de tester si l'ajout des récompenses prestigieuses (les Oscars, les Césars, le Festival de Cannes et le Festival de Venise) améliore ou non la prédiction pour certains films. 

Nous pensons que les films qui sont recompensés dans ce type de concours ont des carcatéristiques similaires entre eux, sans pour autant que cela se reflète dans leur contenu ou leur genre, car la sélection se fait avec un certain nombre de critères similaires.

## Les étapes du projet 
### Etape 1 - récupération des données 
Nous avons décidé d'utiliser à la fois une API - The movie data base, ou TMDB, pour récupérer une base de données conséquente et exhaustive des 10 000 films les plus populaires. Pour cela, nous nous sommes inscrits afin de recevoir une clé nous permettant de faire des requêtes à l'API de TMDB. Grâce à cette clé, nous avons pu récupérer les numéros d'identification des 10 000 films les plus populaires sur le site, puis à partir de ces numéros, nous avons pu pour chaque film récupérer les informations propres au film. 

Nous avons completé cette base par une étape de web scrapping sur Wikipédia des tables qui rescencent les nominations aux différentes catégories pour les compétitions de cinéma prestigieuses - les Oscars, les Césars et les festivals - Cannes et Venise. Les catégories concernées sont la meilleure cinématographie, le meilleur film et le meilleur réalisteur pour les Oscars, le meilleur réalisateur et le meilleur film pour les Césars, la palme d'or le grand prix et le prix du jury pour les Cannes, et lion d'or, lion d'argent et le grand prix du jury pour Venise. 

### Etape 2 - nettoyage et fusion 
Après avoir fini la récupération, nous sommes passés à l'étape du nettoyage des données. En effet, la base récupérée grâce à l'API le nécessitait. Tout d'abord, nous avons remarqué qu'un certain nombre de films apparaissaient plusieurs fois (les enlever tous nous a amené à obtenir une base d'environ 9 200 films uniques). Nous avons aussi pu enlever un certain nombre de variables qui ne nous intéressaient pas pour notre projet (comme le lien des affiches de chaque film). Certaines variables étaient encodées en dictionnaire, nous avons donc extrait de celles ci uniquement les informations qui nous intéressaient, grâce aux regular expressions. Nous nous sommes donc retrouvé avec une base d'environ 9 200 filmsavec pour chacun une vingtaine de variables (dont certaines que nous n'allons finalement probablement pas utiliser, mais dont nous aurions pu avoir besoin pour pousser le projet plus loin).

En ce qui concerne les tables scrappées sur Wikipédia, le nettoyage a été particulièrement laborieux. En particulier, le format différent de chaque table et page sur Wikipédia nous a forcés à reprendre chaque catégorie pour chaque compétition une à une, et supprimer certaines données manuellement. Nous avons également créé des variables binaires (award_mains et award_fest) dans cette partie pour enregistrer la nomination dans l'une des catégories et pouvoir l'exploiter dans nos analyses. 

Après avoir finalisé le nettoyage, nous avons joint les deux bases en utilisant le titre de film et l'année de la parution pour les deux tables, pour retrouver une seule et unique base finale sur laquelle nous travaillons pour la visualisation des données et la modélisation. 

### Visualisation 
Dans la partie visualisation, en plus de quelques statistiques descriptives de notre dataset, nous avons decidé de travailler avec les wordcloud (nuages de mots) et essayer de suivre une évolution temporelle des budgets de films (qui nous permet de mieux visualiser la base de façon générale), et de leur notes moyennes (qui nous est plus utile pour notre projet spécifique). L'analyse se faisait selon le genre, la nomination dans l'une des catégories de compétitions cinématographiques, la décennie ou l'année, ainsi que selon le pays de production et la langue du film. Nous avons également analysé plusieurs synopsis en réalisant des nuages de mots pour comprendre la différence entre plusieurs genres en ce termes pour mieux préparer l'étape de la modélisation. 

### Modélisation et construction des algorithmes 
Notre projet était donc de construire un algorithme de recommandation de films, et plus particulièrement de s'intéresser aux variables correspondant aux prix reçu par le film. Nous souhaitions observer si cette variable pouvait aider à affiner la recommendation. Pour cela, nous avons choisi de nous restreindre à un algorithme "Item-Item", puisque nous n'avons récupéré que les informations liées aux films, et pas du point de vue des utilisateurs (ce qu'un même utilisateur a aimé par exemple). En suivant, et en adaptant la méthode que nous avons trouvé dans un des articles listé plus bas, nous avons ainsi pu construire un algorithme recommendant un certain nombre de film, en fonction soit d'un film, soit d'un mot clé (un genre, un réalisateur, un thème...). Puis nous avons construit un même algorithme, qui lui prennait en compte les prix reçus par un film, afin de pouvoir comparer les recommandations faites suivant les deux méthodes. Bien que loin d'être parfait, nous avons pu obtenir un résultat plutôt satisfaisant, et nous avons aussi pu définir des points qui pourraient être améliorés, ou plus poussées afin d'obtenir un meilleur résultat.



## Navigation dans le dépôt 
Cette partie a pour objectif de décrire la structure de notre dépôt git pour mieux s'y retrouver. 
Voici la liste des dossiers et la description des fichiers pour comprendre notre cheminement. 
* API - *Comprend la partie correspondant à la récupération des données à partir de l'API de TMDB dans le fichier recuperation_API*
* wiki_scrap - *Compren la partie correspondant au scrapping des pages wikipedia de certaines récompenses cinématographiques dans le fichier 1_fonction_scrapping*
* cleaning_data - *Comprend le nettoyage des deux bases, et la fusion en une seule et unique base, qui se trouve dans ce même dossier*
    * le fichier 1_cleaning_API représente la partie nettoyage de la base de données récupérée grâce à l'API
    * 2_cleaning_wiki est l'étape de nettoyage des tables récupérées sur Wikipédia
    * 3_merge_all est le fichier qui permet de lier les deux bases de données en une seule
* visualiser - *Comprend la partie visualisation, avec les statistiques descriptives, les nuages de mots et les différents histogrammes dans le fichier data_vis_avecfix*
* modeliser - *Comprend la partie modélisation avec le fichier modelisation_1 qui reprend l'article de python.plainenglish (Build your first reco system) et modelisation_avec_machine_learning (non abouti car trop complexe)*


## Documentation et références 
[What are today’s top recommendation engine algorithms?](https://itnext.io/what-are-the-top-recommendation-engine-algorithms-used-nowadays-646f588ce639)
[Recommendation system](https://www.nvidia.com/en-us/glossary/data-science/recommendation-system/)
[Introduction to recommender systems](https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada)
[Build your first reco system](https://python.plainenglish.io/tmdb-streamlit-build-your-own-movie-recommendation-system-f2ffbca63d11)

