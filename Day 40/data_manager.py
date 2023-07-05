from pprint import pprint
import requests, os

SHEETY_PRICES_ENDPOINT="https://api.sheety.co/a6604531c6e5d07f06602644d6224317/copyOfFlightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
            
            
object = DataManager()
destination = object.get_destination_data()
updated_destination = object.update_destination_codes()
# print(pandas.DataFrame(destination))
print(updated_destination)