from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def main():
    """Deletes all unstarred emails from Gmail."""
    creds = None
    # Load existing token if available
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    while True:
        print("Fetching unstarred emails...")
        results = service.users().messages().list(userId='me', q='-is:starred', maxResults=500).execute()
        messages = results.get('messages', [])

        if not messages:
            print("✅ No unstarred emails found.")
            return

        print(f"Found {len(messages)} unstarred emails. Moving to Trash...")
        for msg in messages:
            service.users().messages().trash(userId='me', id=msg['id']).execute()
            print("deleted:", msg['id'], msg)

        print("🗑️ Done! 500 unstarred emails moved to Trash.")

print("🗑️ Done! all unstarred emails moved to Trash.")

if __name__ == '__main__':
    main()
