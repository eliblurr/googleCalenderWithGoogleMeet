from service import service, create_events, get_events, get_calendars
from fastapi import FastAPI, Request
import random, string

app = FastAPI()

event = {
  'start': {
    'dateTime': '2022-05-25T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'end': {
    'dateTime': '2022-05-25T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles',
  },
  'summary': 'Example Event',
  'description': 'A chance to hear more about Google\'s developer products.',
  'colorId':5,
  'status': 'confirmed',
  'transparency':'opaque',
  'visibility':'private',
  'location': '800 Howard St., San Francisco, CA 94103',
  'attendees': [
    {
      'displayName': 'John Carter',
      'email': 'johnCarter@example.com',
      'optional': False,
      'organizer': True,
      'responseStatus':'accepted'
    },
    {
      'displayName': 'Mary Jane Watson',
      'email': 'mj.Watson@example.com',
      'optional': True,
      'organizer': False,
      'responseStatus':'accepted'
    },
  ],
  
  # 'recurrence': [
  #   'RRULE:FREQ=DAILY;COUNT=2'
  # ],
  
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },

  # "hangoutLink": string,
  "conferenceData": {
    "createRequest": {
      "requestId": f'ID_{random.choices(string.ascii_uppercase + string.digits, k=15)}',
      "conferenceSolutionKey": {
        "type": 'hangoutsMeet'
      },
      "status": {
        "statusCode": 'success'
      }
    },
  }

}

# @app.get("/")
# async def root(request:Request, code=None):
#   print(request, code)
#   return {"message": "Hello World"}

@app.get("/")
async def root():
  return {"message": create_events(event)}

