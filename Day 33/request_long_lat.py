import requests

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,  
    "formatted" : 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
data_results = data["results"]
sunrise = data_results["sunrise"].split("T")[1].split(":")[0]
sunset = data_results["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)