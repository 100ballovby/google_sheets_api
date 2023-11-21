import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://docs.google.com/spreadsheets/d/1LvAhR--WwYOYDcOFtucTMke6QO0aiW2B_l6vxXjt4jI/edit"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1LvAhR--WwYOYDcOFtucTMke6QO0aiW2B_l6vxXjt4jI"
SAMPLE_RANGE_NAME = "A14:H"

CREDENTIALS_FILE = 'файл_json_из_google_cloud'


def main():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

    if not creds:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "файл_json_из_google_cloud", SCOPES
            )
            creds = flow.run_local_server(port=0)

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        brand = ''
        for row in values:
            if len(row) <= 1:
                continue
            elif row[0]:
                brand = row[0]
                prices = row[3:]
            else:
                row[0] = brand
                row.extend(prices)
            print(f"{row}")
    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
