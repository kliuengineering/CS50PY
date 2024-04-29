import sys
import requests
import json


def RequestBitcoinPrice():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        return response.json()
    except requests.RequestException:
        sys.exit("API cannot be requested, exit program...")


def GetBitcoinValue(data):
    category = data[ "bpi" ]
    currency = category[ "USD" ]
    rate_float = currency[ "rate_float" ]
    return rate_float


def main():
    try:
        argv = float( sys.argv[1] )
        # print( json.dumps( RequestBitcoinPrice(), indent=4 ) )
        value = GetBitcoinValue( RequestBitcoinPrice() )
        print(f"${value * argv :,}")

    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")


if __name__ == "__main__":
    main()
