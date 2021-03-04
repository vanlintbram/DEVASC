import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Grimbergen, Belgium"
dest = "Beigem, Belgium"
key = "m1EAJciU24VbAnfGJ0PdRiAABbPTGyJ2"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 

json_data = requests.get(url).json()
print(json_data)

