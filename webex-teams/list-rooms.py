import requests

access_token = 'MDFjY2Q2NDQtYTk0Ny00OTdmLWE5MzUtN2NkNzkzODMwYmIzNGE3YTU0N2QtMzk2_PF84_consumer'  
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())
