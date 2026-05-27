import os
from google.oauth2.service_account import Credentials
import gspread

KEY_PATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")
SHEET_ID = os.environ.get("SHEET_ID", "여기에_스프레드시트_ID")

creds = Credentials.from_service_account_file(KEY_PATH, scopes=["https://www.googleapis.com/auth/spreadsheets"])
gc = gspread.authorize(creds)
sh = gc.open_by_key(SHEET_ID).sheet1

print("첫 행:", sh.row_values(1))
sh.update("A1", [["GitHub Actions 자동화 성공"]])
print("완료")
