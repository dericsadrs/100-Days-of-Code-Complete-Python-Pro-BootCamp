import requests

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,  
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data["results"])