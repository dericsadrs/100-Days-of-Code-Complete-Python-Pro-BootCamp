import requests


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "65X2BoAkkPc6hR0olRo6OTi41JkoOAu9"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
   def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code



# object_flight_search = FlightSearch()
# iata_code = object_flight_search.get_destination_code("Paris")

# print(iata_code)