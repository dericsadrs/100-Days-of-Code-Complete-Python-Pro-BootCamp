#
# Created on Sat Jun 03 2023
# Created by Software Engineer Deric San Andres
#

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, times_visited, places_visited):
    travel_log.append({
    "country": country,
    "visits": times_visited,
    "cities" : places_visited
    })


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
dict[1] = 4

print(dict.keys())