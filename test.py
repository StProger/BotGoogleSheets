import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1u_0wUfEmh6wbpoafa2PbhBO7roTFx9rrE5227w0WrUY"


def main():

    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        sheets.values().update(spreadsheetId=SPREADSHEET_ID, range="Лист1!A:B",
                               valueInputOption="USER_ENTERED", body={"values":[["3", "2"]]}).execute()

        #result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Лист1!A:D").execute()
        # print(result)
        # for row in result["values"]:
        #     print(row)
        # print(len(result) + 1)

    except HttpError as ex:
        print(ex)


if __name__ == '__main__':
    main()

