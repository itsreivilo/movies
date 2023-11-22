# !pip install -q lxml à executer 
import bs4
import lxml
import pandas
import urllib

from urllib import request
#Enregistrement des URL à scrapper dans notre projet (listes des nominés et gagnants des grand prix du cinéma - oscar, césar, cannes et venise)
url_academy_bf = 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'
url_academy_bd = 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Director'
url_academy_bc = 'https://en.wikipedia.org/wiki/Academy_Award_for_Best_Director'
url_cesar_bf = 'https://en.wikipedia.org/wiki/C%C3%A9sar_Award_for_Best_Film'
url_cesar_bd = 'https://en.wikipedia.org/wiki/C%C3%A9sar_Award_for_Best_Director'
url_palme_or = 'https://en.wikipedia.org/wiki/Palme_d%27Or'
url_cannes_jury = 'https://en.wikipedia.org/wiki/Jury_Prize_(Cannes_Film_Festival)'
url_cannes_gp = 'https://en.wikipedia.org/wiki/Grand_Prix_(Cannes_Film_Festival)'
url_lion_or = 'https://en.wikipedia.org/wiki/Golden_Lion'
url_lion_argent = 'https://en.wikipedia.org/wiki/Silver_Lion'
url_venice_gj = 'https://en.wikipedia.org/wiki/Grand_Jury_Prize_(Venice_Film_Festival)'


#fonction qui prend en ergument le URL et qui ressort le data_frame avec les tableaux correspondants 

def scrapper_wiki(url): 
    