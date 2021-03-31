import requests
import json

access_token = 'MDFjY2Q2NDQtYTk0Ny00OTdmLWE5MzUtN2NkNzkzODMwYmIzNGE3YTU0N2QtMzk2_PF84_consumer'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
