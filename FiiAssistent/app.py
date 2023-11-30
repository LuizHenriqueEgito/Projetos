from src.crawler import make_request_price
from src.email import format_email
from src.calculation import caculate_for_all_fiis

def handler():
    response = format_email()
    print(response)
    if not response:
        return {200: 'Nothing to send'}
    return {200: 'Email sent'}


if __name__ == '__main__':
    debug = handler()