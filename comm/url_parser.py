from bs4 import BeautifulSoup
import requests
import json

def get_paragraph_texts(url: str):
    html: str = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    pes = soup.findAll('p')
    texts: list[str] = []
    for e in pes:
        texts.append(e.get_text())
    return texts