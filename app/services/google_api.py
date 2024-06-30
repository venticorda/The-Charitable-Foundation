from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.services.constants import (
    COLUMN_COUNT,
    FORMAT,
    ROW_COUNT,
    SHEET_ID,
)

TITLE = "Лист1"
SHEET_TYPE = "GRID"
SPREADHEET_PROPERTIES = {
    "properties": {"title": "", "locale": "ru_RU"},
    "sheets": [
        {
            "properties": {
                "sheetType": SHEET_TYPE,
                "sheetId": SHEET_ID,
                "title": "TITLE",
                "gridProperties": {"rowCount": ROW_COUNT, "columnCount": COLUMN_COUNT},
            }
        }
    ],
}

PERMISSIONS_BODY = {"type": "user", "role": "writer", "emailAddress": settings.email}

UPDATE_BODY = {"majorDimension": "ROWS", "values": []}

TABLE_VALUES_HEADER = [
    ["Отчёт от", ""],
    ["Топ проектов по скорости закрытия"],
    ["Название проекта", "Время сбора", "Описание"],
]

NOW_DATE_TIME = datetime.now().strftime(FORMAT)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:

    service = await wrapper_services.discover("sheets", "v4")
    spreadsheet_body = SPREADHEET_PROPERTIES
    spreadsheet_body["properties"]["title"] = f"Отчёт на {NOW_DATE_TIME}"
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheetid = response["spreadsheetId"]
    return spreadsheetid


async def set_user_permissions(spreadsheetid: str, wrapper_services: Aiogoogle) -> None:
    service = await wrapper_services.discover("drive", "v3")
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid, json=PERMISSIONS_BODY, fields="id"
        )
    )


async def spreadsheets_update_value(
    spreadsheetid: str, projects: list, wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover("sheets", "v4")
    table_values = TABLE_VALUES_HEADER
    table_values[0][1] = NOW_DATE_TIME

    for project in projects:
        duration = project.close_date - project.create_date
        new_row = [project.name, str(duration), project.description]
        table_values.append(new_row)

    update_body = UPDATE_BODY
    update_body["values"] = table_values
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range="A1:C100",
            valueInputOption="USER_ENTERED",
            json=update_body,
        )
    )
