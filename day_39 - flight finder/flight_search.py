from flight_data import FlightData
import requests
import json

KIWI_API_KEY = "Sd96RqlbmuAgIwX7_yWHTq1z4B1v3rwJ"
KIWI_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com"
MINIMAL_STAY = 5
MAXIMAL_STAY = 14

class FlightSearch:
    
    def __init__(self) -> None:
        self.kiwi_endpoint = KIWI_SEARCH_ENDPOINT
        self.headers = {
            "apikey":KIWI_API_KEY
        }
        self.data = {}

    def search_flights(self,origin_city_code, destination_city_code, from_time, to_time):
        endpoint = f"{KIWI_SEARCH_ENDPOINT}/v2/search"
        request_body = {
            "fly_from":origin_city_code,
            "date_from":from_time,
            "date_to":to_time,
            "fly_to":destination_city_code,
            "nights_in_dst_from":MINIMAL_STAY,
            "nights_in_dst_to":MAXIMAL_STAY,
            "curr":"PLN",
            "max_stopovers":0,
            "limit": 10,
            "locale":"pl"
        }
        
        r = requests.get(url=endpoint, params=request_body, headers=self.headers)
        r.raise_for_status()
        
        try:
            data = r.json()["data"][0]
        except IndexError:
            print(f"No flights found from {origin_city_code} to {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            departure_city_name=data["route"][0]["cityFrom"],
            departure_airport_code=data["route"][0]["flyFrom"],
            countryTo=data["countryTo"]["name"],
            countryFrom=data["countryFrom"]["name"],
            arrival_city_name=data["route"][0]["cityTo"],
            arrival_airport_code=data["route"][0]["flyTo"],
            outbound_date=data["route"][0]["local_departure"].split("T")[0],
            inbound_date=data["route"][1]["local_departure"].split("T")[0],
            flight_url=data["deep_link"]
        )
        print(f"{flight_data.arrival_city_name}: {flight_data.price}PLN")
        return flight_data
    
    def search_airtport(self, city):
        endpoint = f"{KIWI_SEARCH_ENDPOINT}/locations/query" 
        request_body = {
            "term":city,
        }
        r = requests.get(url=endpoint, params=request_body, headers=self.headers)
        r.raise_for_status()
        return r.json()