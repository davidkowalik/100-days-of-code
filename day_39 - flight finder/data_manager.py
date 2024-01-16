import requests


SHEETY_TOKEN = "Bearer x3gnnp2UPh8LhYHz*9PB#pM4DMMhm^B!T7PtutY9CLiXsiSsLQW9$wK^"
SHEETY_ENDPOINT = "https://api.sheety.co/d24005cafc5956c7349822e7aa5b146e/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        
        self.headers = {
            "Authorization": SHEETY_TOKEN
        }

        self.data = {}

    def get_sheet_data(self):
        self.r = requests.get(url= SHEETY_ENDPOINT, headers=self.headers)
        self.r.raise_for_status()
        self.data = self.r.json()
        return self.data

    def update_price(self, object_id, price):
        endpoint = f"{SHEETY_ENDPOINT}/{object_id}"
        body = {
            "price":{
                "lowestPrice": price 
            }
        }

        self.r = requests.put(url= endpoint, json=body, headers=self.headers)
        self.r.raise_for_status()
    

    def update_sheet(self, sheet_data):
        for item in sheet_data['prices']:
            endpoint = f"{SHEETY_ENDPOINT}/{item['id']}"
            body = {
                "price": item
            }

            self.r = requests.put(url= endpoint, json=body, headers=self.headers)
            self.r.raise_for_status()
        print("\nSheet has been updated!\n")