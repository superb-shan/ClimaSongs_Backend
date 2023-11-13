import requests
import base64

def getSongInfo( song = "Vaseegara" ) :
    client_id = '73e4cf715b8943f5a128be2302bb7674'
    client_secret = '9f1a8376837b4c22b5a48d9609f8a4df'

    # Combine client ID and client secret into a single string
    client_credentials = f"{client_id}:{client_secret}"

    # Base64 encode the client credentials
    client_credentials_b64 = base64.b64encode(client_credentials.encode()).decode()

    # Define the Spotify Accounts service URL
    token_url = 'https://accounts.spotify.com/api/token'

    # Set up the headers
    token_headers = {
        'Authorization': f'Basic {client_credentials_b64}',
    }

    # Set up the data for the token request
    token_data = {
        'grant_type': 'client_credentials',
    }

    # Request the access token
    token_response = requests.post(token_url, headers=token_headers, data=token_data)
    token_data = token_response.json()
    access_token = token_data['access_token']

    # Define the search URL
    search_url = 'https://api.spotify.com/v1/search'

    # Set up the headers for the search request
    search_headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Define the parameters for the search request
    search_params = {
        'q': song,
        'type': 'track',
    }

    # Request the search results
    search_response = requests.get(search_url, headers=search_headers, params=search_params)
    search_data = search_response.json()

    # Extract and print the search results
    # for track in search_data['tracks']['items']:
    #     print(f"Name: {track['name']}")
    #     print(f"Artist: {', '.join([artist['name'] for artist in track['artists']])}")
    #     print(f"Album: {track['album']['name']}")
    #     print(f"Spotify URL: {track['external_urls']['spotify']}")
    #     print(f"Images: {track['album']['images']}")
    #     print(f"Duration: {track['duration_ms']}")
    #     print(f"Popularity: {track['popularity']}")
    #     print(f"Song Preview: {track['preview_url']}")
    #     print()
        # print(track)

    result = []
    for track in search_data['tracks']['items']:
        track_info = {
            "Name": track['name'],
            "Artist": ', '.join([artist['name'] for artist in track['artists']]),
            "Album": track['album']['name'],
            "Spotify URL": track['external_urls']['spotify'],
            "Images": track['album']['images'],
            "Duration": track['duration_ms'],
            "Popularity": track['popularity'],
            "Song Preview": track['preview_url'],

        }
        result.append(track_info)

    # Now 'result' contains a list of dictionaries, where each dictionary represents a track's information.
    return result

# getSongInfo()