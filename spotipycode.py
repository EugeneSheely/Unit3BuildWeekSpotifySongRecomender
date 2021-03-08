import spotipycode

from spotipycode import SpotifyClientCredentials, SpotifyOauthError
import requests


from spotipycode.oauth2 import SpotifyClientCredentials
from collections import defaultdict



client_id='b52dbed68ad34873a9d11d66dd375c04'
client_secret='15543a1283a84c83bf2bc06451d4d1d7'

sp = spotipycode.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ["b52dbed68ad34873a9d11d66dd375c04"],
                                                               client_secret=os.environ["15543a1283a84c83bf2bc06451d4d1d7"]))



client_id='b52dbed68ad34873a9d11d66dd375c04'
client_secret='15543a1283a84c83bf2bc06451d4d1d7'

def test_spotify_client_credentials_get_access_token(self):
    oauth = SpotifyClientCredentials(client_id='b52dbed68ad34873a9d11d66dd375c04', client_secret='15543a1283a84c83bf2bc06451d4d1d7')
    with self.assertRaises(SpotifyOauthError) as error:
        oauth.get_access_token()
    self.assertEqual(error.exception.error, 'invalid_client')