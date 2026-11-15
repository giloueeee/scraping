import requests, bs4,re, os, pandas as pd
from urllib.parse import urljoin
from pathlib import Path


def page_content_extr(url):

    content = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"}).content

    page = bs4.BeautifulSoup(content, "html.parser")
    return page


def url_extraction(cards):

    for card in cards:
        card_url = card.find("a", { "class" : "ent-name"}).get("href")
        card_name = card.find("a", { "class" : "ent-name"}).text.strip()

        full_url = urljoin("https://pokemondb.net", card_url)
        dico[card_name] = {"url" : full_url}
        
def rows_cols_extr(table, card):
        rows = table.find_all("td")
        cols = table.find_all("th")

        if card not in dico_table.keys():
            dico_table[card] = {}
            for i, col in enumerate(cols):
                dico_table[card][col.text.strip()] = rows[i].text.strip()
        else:
            for i, col in enumerate(cols):
                dico_table[card][col.text.strip()] = rows[i].text.strip()

def  rows_cols_extr_base_stats(table, card):
        raw_ext = table.find_all("tr")

        if card not in dico_table.keys():
            dico_table[card] = {}
            for i in range(7):
                row = raw_ext[i].find("td")
                col = raw_ext[i].find("th")
                dico_table[card][col.text.strip()] = row.text.strip()
        else:
            for i in range(7):
                row = raw_ext[i].find("td")
                col = raw_ext[i].find("th")
                dico_table[card][col.text.strip()] = row.text.strip()



if Path("df_pokemon.csv").is_file():
    print("df_pokemon.csv already created")
    pass

else:
    print("df_pokemon not here, creating...")

    page = page_content_extr("https://pokemondb.net/pokedex/national")
    cards = page.find_all("div", {"class" :"infocard"})

    dico = {}
    url_extraction(cards) 

    dico_table = {}

    for i, card in enumerate(dico):   
        print(f"card number {i} out of {len(dico.keys())}")
        card_url = dico[card]["url"]

        info_page = page_content_extr(card_url) 
        image_url = info_page.find("div", {"class" : "grid-col span-md-6 span-lg-4 text-center"})
        image = image_url.find("img").get("src")
        image_extr = requests.get(image)
        if Path("images").is_dir():
            open(f"images\\{card}_image.jpg", "wb").write(image_extr.content)
            print("Création du dossier image")
        else:
            os.makedirs("images")
            open(f"images\\{card}_image.jpg", "wb").write(image_extr.content)
        table_pokedex = info_page.find_all("table" , {"class" :"vitals-table"})[0]
        table_training = info_page.find_all("table" , {"class" :"vitals-table"})[1]
        table_breeding = info_page.find_all("table" , {"class" :"vitals-table"})[2]
        table_stats = info_page.find_all("table" , {"class" :"vitals-table"})[3]

        table = table_pokedex, table_training, table_breeding, table_stats

        rows_cols_extr(table_pokedex, card)
        rows_cols_extr(table_training, card)
        rows_cols_extr(table_breeding, card)
        rows_cols_extr_base_stats(table_stats, card)



    df = pd.DataFrame.from_dict(dico_table, orient = "index")
    print(df)

    df.to_csv("df_pokemon.csv")

