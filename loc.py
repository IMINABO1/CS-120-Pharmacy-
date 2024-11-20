from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')

# print(f"API Key: {api_key}")

def get_nearby_pharmacies(api_key, location, radius=5000):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    if isinstance(location, tuple):
        location_param = f"{location[0]},{location[1]}"
    else:
        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}"
        geocode_response = requests.get(geocode_url)
        geocode_data = geocode_response.json()
        if geocode_data['status'] == 'OK':
            location_param = geocode_data['results'][0]['geometry']['location']
            location_param = f"{location_param['lat']},{location_param['lng']}"
        else:
            raise ValueError("Invalid location or zip code.")

    params = {
        "key": api_key,
        "location": location_param,
        "radius": radius,
        "type": "pharmacy",
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["status"] == "OK":
        pharmacies = [
            {
                "name": place["name"],
                "address": place.get("vicinity"),
                "location": place["geometry"]["location"]
            }
            for place in data["results"]
        ]
        return pharmacies
    else:
        raise Exception(f"Error fetching pharmacies: {data['status']}")

api_key = API_KEY
zip_code = "71245"
latitude_longitude = (40.7128, -74.0060)

pharmacies = get_nearby_pharmacies(api_key, zip_code)

for pharmacy in pharmacies:
    print(f"Name: {pharmacy['name']}, Address: {pharmacy['address']}, Location: {pharmacy['location']}")
