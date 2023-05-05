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

texts = get_paragraph_texts('https://zh.wikipedia.org/wiki/%E7%BE%8E%E5%9B%BD%E7%9F%AD%E6%AF%9B%E7%8C%AB')
print(texts)
print(len(texts))

# print(" ".join(texts)
# with open('out.json','r') as f:
#     texts = json.load(f)
cnt = 0
for s in texts:
    print(len(s))
    cnt += len(s)
print(cnt)

