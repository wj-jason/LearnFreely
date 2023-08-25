import gspread
import re

'''
SET UP PROCESS:

1. create new service account using google sheets api (might need google drive api)
2. add email associated with service account to users of sheet
3. create json key
4. mv /path/to/json/key /other/path/to/repo/key.json <- idk if this is best practice lol

ensure time is synced, if error run: sudo hwclock -s
'''

sa = gspread.service_account(filename="hours/key.json")
sh = sa.open("Logbook")

worksheet = sh.worksheet('Form Responses 1')

# hour_tracker = "hours.csv"
# log = "update_log.txt"

# combine session + prep time
total = worksheet.col_values(4)[1:] + worksheet.col_values(6)[1:]

def extract_numeric(value):
    numeric_part = ''.join(re.findall(r'[\d.]+', value))
    return float(numeric_part) if numeric_part else 0.0

cleaned_time = sum([extract_numeric(value) for value in total])
