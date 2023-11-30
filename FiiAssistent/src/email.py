from src.calculation import caculate_for_all_fiis
from settings import threshold_variance

def filter_email(threshold: float = threshold_variance) -> bool:
    result_all_fii = caculate_for_all_fiis()
    fiis_filter = [item for item in result_all_fii if (
    item[list(item.keys())[0]]['delta_price'] <= -threshold or
    item[list(item.keys())[0]]['delta_price'] > threshold
)]
    return fiis_filter


def format_email():
    fiis_filter = filter_email()
    msg = []
    for item in fiis_filter:
        nome, detalhes = list(item.items())[0]
        mensagem = f"fii: {nome} |\t avg price: {detalhes['avg_price']} |\t current price: {detalhes['current_price']} |\t delta price: {detalhes['delta_price']:.2f}"
        msg.append(mensagem)
    msg = '\n'.join(msg)
    return msg
