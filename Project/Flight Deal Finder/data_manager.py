import requests

SHEETY_PRICE_ENDPOINT = "https://api.sheety.co/879bdcad49840cbf7a00035acd256fc9/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(f"{SHEETY_PRICE_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
            