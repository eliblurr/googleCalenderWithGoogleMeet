from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import os.path, datetime, json

SCOPES = ['https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar']

def authenticate():
    'returns credentials'
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(host='localhost')

        # manually add refresh_token to new json object derived from creds.to_json() as temp[by me]
        temp = json.loads(creds.to_json())
        temp.update({'refresh_token':temp['token']})
        temp = json.dumps(temp)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            # token.write(creds.to_json())
            token.write(temp)

    return creds

def service():
    'returns service'
    credentials = authenticate()
    return build('calendar', 'v3', credentials=credentials)

def get_calendars(calendarId=None):
    page_token = None
    if calendarId:
        return service().calendarList().get(calendarId=calendarId).execute()
    return service().calendarList().list(pageToken=page_token).execute()

def create_calendar():
    pass

def get_events(calendarId=None): 
    page_token = None
    return service().events().list(calendarId='primary', pageToken=page_token).execute()

conferenceDataVersion = 1
supportsAttachments = True
sendNotifications = True
maxAttendees = 10
calendarId = 'primary'
sendUpdates = 'all'
prettyPrint = True

def create_events(event):
    return service().events().insert(
        calendarId='primary', 
        conferenceDataVersion=conferenceDataVersion, 
        supportsAttachments = supportsAttachments,
        sendNotifications = sendNotifications,
        maxAttendees = maxAttendees,
        sendUpdates = sendUpdates,
        prettyPrint = prettyPrint,
        body=event
    ).execute()
