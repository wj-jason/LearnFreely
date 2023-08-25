import gspread

# ensure time is synced 
# sudo hwclock -s
sa = gspread.service_account()
sh = sa.open("Logbook")

wks = sh.worksheet('Form Responses 1')

# Fetch all values from column D (index 3)
column_d_values = wks.col_values(4)  

# Print all entries from column D starting from row 2
for value in column_d_values[1:]: 
    print(value)
