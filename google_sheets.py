from all_tokens import GOOGLE_TOKEN

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = '1f1L2icOsMcy3wkmnw7v5FFQnhZkhqmf2CgmqQ6XjIOs'
READ_RANGE = "Вакансии!A2:E"
WRITE_RANGE = "Заявки!A2:C"

from faker import Faker #не забыть убрать
fake = Faker('ru_RU')
import random


creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
if os.path.exists("token.json"):
  creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
  if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())
  else:
    flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
    creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
  with open("token.json", "w") as token:
    token.write(creds.to_json())


def read_table():
  service = build("sheets", "v4", credentials=creds)
  sheet = service.spreadsheets()
  result = (
      sheet.values()
      .get(spreadsheetId=SPREADSHEET_ID, range=READ_RANGE)
      .execute())

  values = result.get("values", [])

  if not values:
    return("No data found.")
    
  else:
    return(values)

def add_requests(rows):
  service = build("sheets", "v4", credentials=creds)
  sheet = service.spreadsheets()
  body = {'values' : rows}
  sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=WRITE_RANGE, valueInputOption="RAW", body=body).execute()


rows = []
for i in range(20):
  rows.append(["+7(012)-312-31 23", fake.name(), str(random.randint(1,30))])

print(read_table())