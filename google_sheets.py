import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError


class GoogleSheet:

    def __init__(self):

        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        self.SPREADSHEET_ID = "1u_0wUfEmh6wbpoafa2PbhBO7roTFx9rrE5227w0WrUY"

        credentials = None
        if os.path.exists("token.json"):
            credentials = Credentials.from_authorized_user_file("token.json", self.SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self.SCOPES)
                credentials = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(credentials.to_json())

        self.credentials = credentials
        self.service = build("sheets", "v4", credentials=self.credentials)
        self.sheets = self.service.spreadsheets()

    async def get_empty_row(self):

        result = self.sheets.values().get(spreadsheetId=self.SPREADSHEET_ID, range="Лист1!A:K").execute()
        print(result["values"])
        empty_row = len(result["values"]) + 1
        return empty_row

    async def insert_data(self, data: dict):

        name = data.get("name")
        city = data.get("city")
        level_nn = data.get("level_neuro_network")
        skills_python = data.get("skills_python")
        free_lessons = data.get("free_lessons")
        get_solve = data.get("get_solve")
        actual_topic = data.get("actual_topic")
        kind_work = data.get("kind_work")
        salary = data.get("salary")
        goals = data.get("goals")
        phone = data.get("phone")

        body = {
            "values": [
                [
                    name,
                    city,
                    level_nn,
                    skills_python,
                    free_lessons,
                    get_solve,
                    actual_topic,
                    kind_work,
                    salary,
                    goals,
                    phone
                ]
            ]
        }

        empty_row = await self.get_empty_row()
        print(f"Пустых строк: {empty_row}")

        service = build("sheets", "v4", credentials=self.credentials)
        sheets = service.spreadsheets()
        sheets.values().update(spreadsheetId=self.SPREADSHEET_ID, range=f"Лист1!A{empty_row}:K{empty_row}",
                               valueInputOption="USER_ENTERED", body=body).execute()
