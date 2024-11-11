import csv
import requests

def get_zip_code(city=None, state=None, zip_code=None):
    if zip_code:
        # Validate and retrieve information for the zip code
        response = requests.get(f'http://api.zippopotam.us/us/{zip_code}')
        
        if response.status_code == 200:
            data = response.json()
            return data['post code']
        else:
            return "Invalid zip code"

    elif city and state:
        # Find zip codes for city and state
        response = requests.get(f'http://api.zippopotam.us/us/{state}/{city}')
        
        if response.status_code == 200:
            data = response.json()
            zip_codes = [place['post code'] for place in data['places']]
            return zip_codes
        else:
            return "No zip code found for the specified city and state"

    else:
        return "Please provide either a zip code or both city and state."

# Example usage
print(get_zip_code(city="Los Angeles", state="CA"))
print(get_zip_code(zip_code="90210"))
