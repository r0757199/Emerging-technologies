import urllib.parse
import requests
import base64
from tabulate import tabulate

#General variables
main_api = "https://api.spotify.com/v1/artists?"
url_token = "https://accounts.spotify.com/api/token"
clientId = "xxxxxxxxxx"
clientSecret = "xxxxxxxxx"
headers = {}
data = {}

#Making a base64 code for authorization
message = f"{clientId}:{clientSecret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')

#Request authorization
headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"
r = requests.post(url_token, headers=headers, data=data)
token = r.json()['access_token']

#Output of data requested
while True:
    Artistname = input("What's the name of the Artist? (or type 'q' or 'quit'): ")
    if Artistname == "quit" or Artistname == "q":
        break

    search_url = "https://api.spotify.com/v1/search?"
    url = search_url + urllib.parse.urlencode({"query": Artistname, "type": "artist"})
    artist_info = requests.get(url,headers={'Authorization': "Bearer " + token}).json()

    artisten = []
    for artist in artist_info["artists"]["items"]:
        artisten.append([artist["id"], artist["name"], artist["genres"], artist["popularity"]])
    print(tabulate(artisten, headers=["id","name","genres","popularity"]))
