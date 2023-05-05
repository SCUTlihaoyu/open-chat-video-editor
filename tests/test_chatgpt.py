import sys
import os
# sys.path.append("F:\Workspace\github\open-chat-video-editor")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import openai
import requests
from generator.text.models.chatgpt import ChatGPTModel,URL2TextChatGPTModel

from bs4 import BeautifulSoup
import requests
def get_paragraph_texts(url: str):
    html: str = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    pes = soup.findAll('p')
    texts: list[str] = []
    for e in pes:
        texts.append(e.get_text())
    return texts



organization = "your_organization"
api_key = "your_api_key"
openai.organization = organization
openai.api_key = api_key
openai.Model.list()


def ask(question: str):
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=400,
        stream=False,
        echo=False,
    )

model = URL2TextChatGPTModel("",organization,api_key)
url = "https://zh.wikipedia.org/wiki/%E7%BE%8E%E5%9B%BD%E7%9F%AD%E6%AF%9B%E7%8C%AB"
resp = model.run(url)
print(resp)
zh_sentences = []
en_sentences = []
for item in resp["out_text"]:
    zh_sentences.append(item["zh"])
    en_sentences.append(item["en"])
print(zh_sentences)
print(en_sentences)