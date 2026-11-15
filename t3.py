import re
from bs4 import BeautifulSoup

# Votre contenu HTML (la liste nettoyée)
html_content = """
<a class="ent-name" href="/pokedex/terapagos">Terapagos</a><br/> <small><a class="itype normal" href="/type/normal">Normal</a></small></span></div>, 
<div class="infocard"><span class="infocard-lg-img"><a href="/pokedex/pecharunt"><picture><source srcset="https://img.pokemondb.net/sprites/home/normal/2x/avif/pecharunt.avif" type="image/avif"/><img alt="Pecharunt" class="img-fixed img-sprite" loading="lazy" src="https://img.pokemondb.net/sprites/home/normal/2x/pecharunt.jpg"/></picture></a></span><span class="infocard-lg-data text-muted"><small>#1025</small><br/> <a class="ent-name" href="/pokedex/pecharunt">Pecharunt</a><br/> <small><a class="itype poison" href="/type/poison">Poison</a> · <a class="itype ghost" href="/type/ghost">Ghost</a></small></span></div>
"""

soup = BeautifulSoup(html_content, "html.parser")

# Récupérer uniquement les attributs href contenant le mot "pokedex"
urls_pokedex = [lien["href"] for lien in soup.find_all("a", href=re.compile("pokedex"))]

# Affichage des résultats
for url in urls_pokedex:
    print(url)
