import gspread
import re
import os
from dotenv import load_dotenv
load_dotenv()

# ensure time is synced, if error run: sudo hwclock -s
sa = gspread.service_account()
sh = sa.open(os.getenv("PAIR_OPEN"))
worksheet = sh.worksheet(os.getenv("PAIR_WORKSHEET"))

'''
worksheet.col_values(2)[2:]: Math
worksheet.col_values(3)[2:]: Chemistry
worksheet.col_values(4)[2:]: Physics
worksheet.col_values(5)[2:]: Biology
worksheet.col_values(6)[2:]: English
worksheet.col_values(7)[2:]: Science

worksheet.col_values(8)[2:]: Other

Science 1206     -> SN1
Chemistry 3200   -> CN3
IB English 4283  -> EI4

First char:          First letter of subject
Second character:    A for AP, I for IB, N for None
Third character:     Course level (4 for AP/IB)
'''
col_range = [2, 3, 4, 5, 6, 7]


total = {
    'M':[],
    'C':[],
    'P':[],
    'B':[],
    'E':[],
    'S':[]
}

for column in col_range:
    for entry in worksheet.col_values(column)[2:]:
        if entry:
            # not AP or IB
            if len(entry) > 2:
                col_key = worksheet.col_values(column)[1][0]
                total[col_key].append(f'{col_key}N{entry[-1]}')
            # AP or IB
            else:
                col_key = worksheet.col_values(column)[1][0]
                total[col_key].append(f'{col_key}{entry[0]}4')

# print(total)
