import polyline
import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:5000/route/v1/driving/-68.035987,46.971436;-69.799986,44.86147')
json_response = response.json()

route = json_response['routes'][0]
pprint(json_response)
pprint(polyline.decode(route['geometry']))