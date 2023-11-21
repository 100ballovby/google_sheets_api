import os
import time
import asyncio
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials

# Если modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of the spreadsheet.
SPREADSHEET_ID = "1LvAhR--WwYOYDcOFtucTMke6QO0aiW2B_l6vxXjt4jI"  # это надо достать из ссылки на гугл таблицу после d/ и до /edit
RANGE_NAME = "A14:H"  # это диапазон ячеек с названиями и ценами

# файл, в который сейчас пишутся изменения
CHANGE_LOG_FILE = "change_log.txt"

# функция получения данных из таблицы
async def get_values():
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "здесь_название_ключа_из_google_cloud", SCOPES
    )

    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    return values


async def main():
    # берем текущие значения из таблицы
    current_values = await get_values()

    # открываем лог
    with open(CHANGE_LOG_FILE, "a+") as change_log:
        # собираем данные из чендж лога
        previous_values = []

        # переходим в начало и читаем данные
        change_log.seek(0)
        if os.path.exists(CHANGE_LOG_FILE):
            previous_values = change_log.readlines()
            previous_values = [
                value.strip() for value in previous_values
            ]
            previous_values = [value.split(",") for value in previous_values]

        # возврат в конец файла, чтобы добавить новые данные.
        change_log.seek(0, os.SEEK_END)

        # сравниваем текущие результаты со старыми
        for row in current_values:
            if row not in previous_values:
                # новая строка
                change_log.write(",".join(row) + "\n")

    # ждем час перед тем, как опросить таблицу
    time.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())

