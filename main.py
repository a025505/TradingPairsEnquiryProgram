import json
import requests # Please install requests package in your environment
import CONSTANTS as C
import support_data as SD

# GET DATA
def getData(pairing):
    # Whitebit
    request = C.WHITEBIT_V1_PUBLIC_TICKER_MARKET_SINGLE + pairing
    baseUrl = C.WHITEBIT_BASE_URL

    # preparing request URL
    completeUrl = baseUrl + request

    try:
        x = requests.get(completeUrl)
        x.raise_for_status()
        result = json.loads(json.dumps(x.json()))
        print("\nWhiteBit Listing"
              + "\nCurrent Pairing: " + pairing
              + "\nHighest Bid (Now): \t" + result['result']['bid']
              + "\nLowest Ask (Now): \t" + result['result']['ask']
              + "\nLatest Deal Price: \t" + result['result']['last'])
        # print(x.text)
    except Exception as e:
        print("WhiteBit Error: " + e)

# Menu
def menu():
    menuText = "\n1. Trade Update Data\n2. Check Account\n3. Exit\n"
    print(menuText)

    options = ['1', '2', '3']

    selection = input("Please select an option: ")
    if selection not in options:
        print("Error Selection!")
    else:
        print("\nYou have selected option: " + selection + "\n")
        if selection == '1':
            while True:
                for key in SD.dict_pairing:
                    print(str(key) + ". " + SD.dict_pairing[key])
                print(str(len(SD.dict_pairing) + 1) + ". Exit")
                value = input("Please select the pairing options: ")
                if value == str(len(SD.dict_pairing) + 1):
                    break
                try:
                    pairings = SD.dict_pairing[int(value)]  # Get data from the dictionary
                    getData(pairings)
                    print()
                except Exception as e:
                    print(e)
        elif selection == '2':
            print("Not implemented yet.")
        elif selection == '3':
            exit()


def main():
    print("Trading Bot (Testing Sample)")
    while True:
        menu()


if __name__ == '__main__':
    main()
