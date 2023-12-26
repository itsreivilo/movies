Nous avons décidé de scrapper les bases de données sur les différents prix cinématographiques sur wikipédia - Oscar (Academy awards), César, Festival de Cannes et festival de Venise et les nettoyer après les avoir récupéré. 
Nous voulons récupérer ue base de données unique à la fin qui aura la forme suivante: {Name, Year, Dir_or_prod, Studio, Award_mains, Awards_mains_cat, Award_fest, Win} 
* La colonne Name sera le nom du film
* La colonne Year est l'année de sortie
* La colonne Dir_or_prod est le réalisateur ou le producteur du film
* La colonne Studio est le studio de production (si mentionné)
* La colonne Award_mains est la variable qui enregistre si le film a été nominé ou a gagné à la compétition plus "mainstream", plus commune telle que Academy Awards ou le prix César. La variable prendra la valeur 0 si le film n'a pas été nominé ni a gagné, 1 s'il a été nominé et 2 s'il a gagné.
* Award_mains_cat enregistre la catégorie dans laquelle le film a été nominé/qu'il a remporté
* De même que pour Award_mains, Award_fest enregistre si le film a été nominé ou a gagné dans la compétition d'un des grands festivals - Cannes et Venise. 