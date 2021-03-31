import requests

access_token = 'MDFjY2Q2NDQtYTk0Ny00OTdmLWE5MzUtN2NkNzkzODMwYmIzNGE3YTU0N2QtMzk2_PF84_consumer'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vNTRlN2FhOTAtOTIzNi0xMWViLWE4NWYtNjdkNjE0Y2Y4YmRm'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())
