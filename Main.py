from __future__ import print_function
import os.path
import json
from datetime import datetime

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def fetch_all_messages(service, query):
    all_messages = []
    next_page_token = None

    while True:
        response = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=100,
            pageToken=next_page_token
        ).execute()

        all_messages.extend(response.get('messages', []))
        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    return all_messages

def read_job_emails():
    service = get_gmail_service()
    query = 'subject:applied OR subject:application OR subject:"thank you for applying"'
    messages = fetch_all_messages(service, query)

    job_data = []
    for msg in messages:
        email = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = email['payload'].get('headers', [])

        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), 'No Subject')
        snippet = email.get('snippet', 'No Content')

        timestamp = int(email.get('internalDate', 0)) / 1000
        date = datetime.fromtimestamp(timestamp).strftime('%a, %d %b %Y')

        job_data.append({
            "subject": subject,
            "snippet": snippet,
            "date": date
        })

    with open("applied_jobs.json", "w", encoding='utf-8') as f:
        json.dump(job_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved {len(job_data)} jobs to applied_jobs.json")

if __name__ == '__main__':
    read_job_emails()
