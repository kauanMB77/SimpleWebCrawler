import requests
from bs4 import BeautifulSoup
import re

def extract_words(url: str) -> list[str]:
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve webpage: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    words = re.findall(r"\b\w+\b", text)

    return list(set(words))

if __name__ == "__main__":
    url = input("Insira o URL do site: ")
    path = input("Insira o path para salvar: ")
    words = extract_words(url)

    with open(path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')