import requests
from requests.auth import HTTPBasicAuth

CLIENT_ID = "xxx"
CLIENT_SECRET = "yyy"

token_resp = requests.post(
    "https://bitbucket.org/site/oauth2/access_token",
    data={"grant_type": "client_credentials"},
    auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
)
token_resp.raise_for_status()
access_token = token_resp.json()["access_token"]
