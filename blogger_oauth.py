import json
import os
import pickle
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define escopos da API do Blogger
SCOPES = ['https://www.googleapis.com/auth/blogger']

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
        creds = flow.run_local_server(port=8080)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('blogger', 'v3', credentials=creds)
    return service

# Substitua pelo seu Blog ID
BLOG_ID = "483973688844725319"

def post_to_blogger(title, content):
    try:
        service = get_service()
        post = {
            "title": title,
            "content": content
        }
        service.posts().insert(blogId=BLOG_ID, body=post, isDraft=False).execute()
        return True
    except Exception as e:
        print(f"Erro ao publicar: {e}")
        return False