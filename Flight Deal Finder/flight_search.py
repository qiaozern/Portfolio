import os
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.environ("TEQUILA_API_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_codes(self, city_name):
        """return IATA Code to the spreadsheet"""
        # code = "TESTING"
        # return code
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        
        query = {
            "term": city_name,
            "location_types": "city"
        }
        
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/locations/query",
            headers=headers,
            params=query
        )
        result = response.json()['locations']
        code = result[0]['code']
        return code
    
    def check_flight(self, origin_city, destination_city, from_date, to_date):
        """return destination and price"""
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        
        query = {
            "fly_from": origin_city,
            "fly_to": destination_city,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query
        )
        
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flight found for {flight_data.destination_city}.")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_airport=data['route'][0]["flyFrom"],
            origin_city=data['route'][0]["cityFrom"],
            destination_airport=data['route'][0]["flyTo"],
            destination_city=data['route'][0]["cityTo"],
            out_date=data['route'][0]['local_departure'].split("T")[0],
            return_date=data['route'][1]['local_departure'].split("T")[0]
        )
        
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        
        return flight_data