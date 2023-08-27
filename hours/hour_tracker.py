import gspread
import re
import os
from dotenv import load_dotenv
load_dotenv()

# ensure time is synced, if error run: sudo hwclock -s
sa = gspread.service_account()
sh = sa.open(os.getenv("HOUR_TRACKER_OPEN"))
worksheet = sh.worksheet(os.getenv("HOUR_TRACKER_WORKSHEET"))

# hour_tracker = "hours.csv"
# log = "update_log.txt"

# combine session + prep time
total = worksheet.col_values(4)[1:] + worksheet.col_values(6)[1:]

def extract_numeric(value):
    numeric_part = ''.join(re.findall(r'[\d.]+', value))
    return float(numeric_part) if numeric_part else 0.0

cleaned_time = sum([extract_numeric(value) for value in total])

print(cleaned_time)
