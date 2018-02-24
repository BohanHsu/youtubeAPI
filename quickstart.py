import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "client_secret.json"

SCOPE = ['https://www.googleapis.com/auth/youtube.force-ssl']

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPE)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
    results = service.channels().list(
        **kwargs
    ).execute()
    print results
    #print('This channels ID is %s. Its title is %s, and it has %s views' %
    #     (results['item'][0]['id'],
    #      results['item'][0]['snippet']['title'],
    #      results['item'][0]['statistics']['viewCount']))

if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    channels_list_by_username(service,
            part='snippet,contentDetails,statistics',
            forUsername='GoogleDevelopers')

