import requests, bs4, pandas as pd


url ="https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020"

content = requests.get(url, headers={"User-Agent": "Python for data science tutorial"}).content

page = bs4.BeautifulSoup(content, "html.parser")

table = page.find("table", {"class" : "wikitable sortable"})


rows = table.find_all("tr")
columns= table.find_all("th")

print(rows[1].text.strip())

text={}

for row  in rows:
    cells = row.find_all("td")
    elements = [ele.text.strip() for ele in cells]
    if len(cells)>0:
        text[elements[0]] = elements[1:]
    else:
        pass

df = pd.DataFrame.from_dict(text, orient = "index")
df.to_csv("df.csv", sep=",")
print(df)