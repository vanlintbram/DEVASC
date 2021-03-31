import requests

access_token = 'MDFjY2Q2NDQtYTk0Ny00OTdmLWE5MzUtN2NkNzkzODMwYmIzNGE3YTU0N2QtMzk2_PF84_consumer'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vMDBiNmRlZjAtNjRjZC0xMWViLWFmNjAtZTEyYTE3ZmExMDdh'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id}
res = requests.get(url, headers=headers, params=params)
print(res.json())
