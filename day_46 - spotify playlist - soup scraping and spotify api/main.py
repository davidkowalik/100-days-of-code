import requests
from bs4 import BeautifulSoup
import base64
import webbrowser
from urllib.parse import urlencode

DATE = "2022-08-16"
BASE_BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'
CLIENT_ID = 'c0c7c5d769104bb8ae0333dcc57aba0e'
CLIENT_SECRET = '7856f194446a42d0a1bf67766f8a9c6c'
ID_SECRET = f"{CLIENT_ID}:{CLIENT_SECRET}"
ID_SECRET_BYTES = ID_SECRET.encode('ascii')
CODE = "AQBu5o4zT0pR_5z8BehDDZoQeBt1Yu7ryCKJEOe85ZqoEyJwE-FKq4fbNzBh5xxpIR3EpQ2Zb7CnA9fUO8B3zZBBE1Lv0hP_jQKMabnFBILP3QaXnk4RsLJ6hArIDN5q9lWW5F_IwrbLeB9MmCUJ67nOCsZu0uC7kh2qS49X-uxHzzjTSrVyCKMnN75sK9mhiZthofN_3RHWiU-lWYxS9EUJ4BlgQHvIpYHtXM_nNXgsvnXGY-H8134NXp1fmHwP7lsCiv8XaJV10g"



def refresh_spotify_token():
    headers = {
        'Authorization':('Basic ' + str(base64.b64encode(ID_SECRET_BYTES).decode("ascii"))),
        'Content-Type':'application/x-www-form-urlencoded'
    }

    body = {
        'grant_type':'authorization_code',
        'code':CODE,
        "redirect_uri": "https://localhost:8888",
    }

    request = requests.post(OAUTH_TOKEN_URL, params=body, headers=headers)
    print(request.json())
    token_data = request.json()
    token = f"{token_data['token_type']} {token_data['access_token']}"
    with open('token.txt', 'w') as file:
        file.write(token)


def spotify_autorization():
    global CODE
    auth_headers = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": "https://localhost:8888",
        "scope": "user-library-read user-read-private user-read-email playlist-modify-private playlist-modify-public"
    }

    # r = requests.get(url=OAUTH_AUTHORIZE_URL, headers=auth_headers)
    # print(r.text)
    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
    CODE = input("Paste autorization code:\n")
    print('\n\n')

def create_new_playlist(user_id, list_date, header):
    endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    body = {
        "name": f"{list_date} hits",
        "description": f"List of top100 songs from {list_date}",
        "public": False
    }

    r = requests.post(url = endpoint, json=body, headers=header)
    print(r.json())
    return r.json()['id']

def search_track(track: str, header: dict) -> str:
    endpoint= "https://api.spotify.com/v1/search"

    body={
        "q":track,
        "type":["track"],
        'limit':5
    }

    r = requests.get(url = endpoint, params=body, headers=header)
    r.raise_for_status()
    return r.json()['tracks']['items'][0]['uri']

def add_item_to_playlist(playlist_id: str, uris: str, header):
    endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    
    body={
        "uris":uris
    }

    r = requests.post(url=endpoint, json=body, headers=header)
    r.raise_for_status()
    print("\nadd_item_to_playlist requests output:\n")
    print(r.json())


# # -----------------------------------------------------------------------------------------------------------------
# # BILBOARD 
# # -----------------------------------------------------------------------------------------------------------------
# # playlist_date = input("Witch date You woudl like to travel to? Type the date in this format: YYYY-MM-DD\n")
# playlist_date = "2022-07-16"

bilboard_web_data = requests.get(f"{BASE_BILLBOARD_URL}{DATE}").text

soup = BeautifulSoup(bilboard_web_data, 'html.parser')
# # 2 ways of selecting heading3 containgin song title, both working correctly 
# songs = soup.find_all(name ='h3', id='title-of-a-story', class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
songs = soup.select("li ul li h3")

songs_tiles = [song.getText().strip() for song in songs]
print(songs_tiles)


# # -----------------------------------------------------------------------------------------------------------------
# # SPOTIFY 
# # -----------------------------------------------------------------------------------------------------------------

# spotify_autorization()
# refresh_spotify_token()
# TOKEN = "Bearer BQCc5BMxPlMA8Mg8E-xuK5VRYE951Job88COtWV-gyS5Lcml9bJomUg-LCnZKPbMv6Y22d0R_hFnmadbTa0DyiX1aNOIxThg01TVjHQtUMfwZlQXkQlkuMea_WYAqkl0uJIbgOalVfS4IOciHgqAnho5bkP6dygB_H4M_WlX7UWZUOAtlYbxa9P2QBnzRKNWn7ege4shLlN1qZCiGPk2ZkPvMTM8_RxF5Dl59ESCQmmEXxmNtHs0ZJ7uG_aTZw"

with open('token.txt', 'r') as token_file:
    TOKEN = token_file.readline()
    print(TOKEN)

user_headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

user_params = {
    "limit": 50
}

# response = requests.get(url='https://api.spotify.com/v1/me/tracks', headers=header)

# print(response.json())

r = requests.get("https://api.spotify.com/v1/me", params=user_params, headers=user_headers)
r.raise_for_status()
print(r.json())

user_id = r.json()['id']
print(user_id)


print("\nCreating new playlist: \n")

playlist_id = create_new_playlist(user_id=user_id, list_date=DATE, header=user_headers)
print(playlist_id)


track_uris_list = []
uris_str = ""
for song in songs_tiles:
    track = search_track(track=song, header=user_headers)
    track_uris_list.append(track)
    uris_str = uris_str + track + ","

add_item_to_playlist(playlist_id=playlist_id, uris=track_uris_list, header=user_headers)