import requests

def get_bybit_listings():
    url = "https://api.bybit.com/v2/public/symbols"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [coin['name'] for coin in data['result']]
    return []

if __name__ == "__main__":
    listings = get_bybit_listings()
    print("Bybit New Listings:", listings)
