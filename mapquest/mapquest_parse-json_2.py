import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = ""
dest = ""
key = "m1EAJciU24VbAnfGJ0PdRiAABbPTGyJ2"


while orig == "" and dest == "":
    orig = input("Give your starting point as eg 'Grimbergen, Belgium'")
    dest = input("Give your destination point as eg 'Grimbergen, Belgium'")


url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 

print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")


