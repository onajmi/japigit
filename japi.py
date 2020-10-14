import json
import requests

url = "https://www.alphavantage.co/query"

def get_stock_data(symbol):
    params = {'symbol': symbol, 'apikey': '0S9C7DYBPUYKWXC1', 'function': 'TIME_SERIES_DAILY'}
    response = requests.get(url, params)

    return response.json()

def main():
    symbol = input('Enter symbol: (Example: (AAPL/IBM)')

    result = get_stock_data(symbol)

    print('The current price is: ')

    for i in result['Time Series (Daily)']['2020-10-08']:
        print(i, result['Time Series (Daily)']['2020-10-08'][i])

    continue_program = input("Do you want to continue (y/n)")

    if (continue_program == 'y'):
        main()
    else:
        exit()

main()
print('Stock Quotes retrieved successfully!')