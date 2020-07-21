#!/usr/bin/env python
import datetime 
import time

import gspread

from config import *

# Automation coverage trend
gc = gspread.service_account()
now = datetime.datetime.now()
g = gc.open(SPREADSHEET_NAME)
worksheet = g.worksheet("Automation coverage")

worksheet.insert_rows(
    [[
         now.strftime("%m-%d-%y"), 
         "='PQI Metrics'!B29", 
         "='PQI Metrics'!C29", 
         "='PQI Metrics'!D29",
         "=B2/sum(B2:D2)"
    ]], row=2,
    value_input_option='USER_ENTERED'
)

worksheet.update('A30', 'Last update: ' + now.strftime("%Y-%m-%d %H:%M"))
