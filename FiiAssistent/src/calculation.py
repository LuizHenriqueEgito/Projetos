from src.crawler import make_request_price
from typing import List
from settings import fiis_average_price


list_fiis_names = list(fiis_average_price.keys())

def calculate_variance(fii_name: str):
    avg_price = fiis_average_price[fii_name]
    current_price = make_request_price(fii_name=fii_name)
    delta_price = round(
        ((current_price - avg_price) / avg_price),
        2
    )
    return {
        fii_name: {
            'avg_price': avg_price,
            'current_price': current_price,
            'delta_price': delta_price 
        }
    }


def caculate_for_all_fiis(
        list_fiis_names: List[str] = list_fiis_names
        ):
    all_fiis = [
        calculate_variance(fii_name=fii_name) for fii_name in list_fiis_names
        ]
    return all_fiis
