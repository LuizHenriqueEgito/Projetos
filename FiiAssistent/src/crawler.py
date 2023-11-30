import requests
from typing import List, Dict
from bs4 import BeautifulSoup
from src.configs import (
    HEADERS,
    dict_index_strong,
)

# faz a requisição para cada FII
def make_response(fii_name: str) -> float:
    fii = fii_name.lower()
    url = f'https://statusinvest.com.br/fundos-imobiliarios/{fii}'
    response = requests.get(url, headers=HEADERS)
    text_response = response.text
    soup = BeautifulSoup(text_response, 'html.parser')
    return soup

# Busca o preço
def request_strong(soup):
    list_elements = soup.find_all('strong', class_='value')
    return list_elements

# formata os valores encontrados
def format_values(value):
    value = value.string.strip()
    value = value.replace(',', '.')
    if '%' in value:
        value = value.replace('%', '')
    if '-' in value:
        return None
    value = float(value)
    return value

# pega o preço do FII desejado
def get_price(
        list_elements: List[str],
        dict_index_strong: Dict[str, int] = dict_index_strong
        ):
    price = list_elements[dict_index_strong['price']]
    price = format_values(price)
    return price

def make_request_price(fii_name: str):
    soup = make_response(fii_name=fii_name)
    list_element = request_strong(soup)
    price = get_price(list_elements=list_element)
    return price
