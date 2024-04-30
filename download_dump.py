import requests

url = "https://dumps.wikimedia.org/tewiki/20240420/tewiki-20240420-pages-meta-current.xml.bz2"

r = requests.get(url)

with open('data/tewiki_latest.bz2', 'wb') as f:
    f.write(r.content)
