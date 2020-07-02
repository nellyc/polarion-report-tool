#!/usr/bin/env python
import datetime 

from pylarion.test_run import TestRun  
from pylarion.work_item import TestCase, Requirement  
from pylarion.document import Document  

import gspread

from config import *
from helpers import *

g = gapi.GoogleSpreadSheetAPI(SPREADSHEET_NAME, "PQI Metrics")

# Requirements coverage 
g.update_sheet(2, 1, get_number_of_reqs_by_planned_in())
g.update_sheet(3, 1, get_number_of_reqs_by_planned_in_with_linked_work_items())

# Automation coverage and approved
g.update_sheet(22, 2, testcase_approved_automated(importance=CRITICAL, approved=True, automated=False))
g.update_sheet(22, 3, testcase_approved_automated(importance=CRITICAL, approved=True, automated=True))
g.update_sheet(22, 4, testcase_approved_automated(importance=CRITICAL, approved=False, automated=False))
g.update_sheet(22, 6, testcase_approved_automated(importance=CRITICAL, approved=False, automated=True))
g.update_sheet(23, 6, testcase_approved_automated(importance=H_M_L, approved=True, automated=False))
g.update_sheet(23, 3, testcase_approved_automated(importance=H_M_L, approved=True, automated=True))
g.update_sheet(23, 4, testcase_approved_automated(importance=H_M_L, approved=False, automated=False))
g.update_sheet(23, 6, testcase_approved_automated(importance=H_M_L, approved=False, automated=True))

# Automation coverage
g.update_sheet(27,2, automation_coverage(AUTOMATED, CRITICAL))
g.update_sheet(27,3, automation_coverage(NOT_AUTOMATED, CRITICAL))
g.update_sheet(27,4, automation_coverage(MANUAL_ONLY, CRITICAL))
g.update_sheet(28,2, automation_coverage(AUTOMATED, H_M_L))
g.update_sheet(28,3, automation_coverage(NOT_AUTOMATED, H_M_L))
g.update_sheet(28,4, automation_coverage(MANUAL_ONLY, H_M_L))

# Test runs execution status per plan
g.update_sheet(44,2, find_number_of_TCs_per_status(status=PLANNED))
g.update_sheet(44,3, find_number_of_TCs_per_status(status=ATTEMPTED))
g.update_sheet(44,4, find_number_of_TCs_per_status(status=NOT_RUN))
g.update_sheet(44,5, find_number_of_TCs_per_status(status=PASSED))
g.update_sheet(44,6, find_number_of_TCs_per_status(status=FAILED))
g.update_sheet(44,7, find_number_of_TCs_per_status(status=BLOCKED))

# Automation coverage trend
gc = gspread.service_account()
now = datetime.datetime.now()
g = gc.open(SPREADSHEET_NAME)
worksheet = g.worksheet("Automation coverage")

worksheet.insert_rows(
    [[
         now.strftime("%m-%d-%y"), 
         automation_coverage(AUTOMATED, ANY_IMPORTANCE), 
         automation_coverage(NOT_AUTOMATED, ANY_IMPORTANCE), 
         automation_coverage(MANUAL_ONLY, ANY_IMPORTANCE),
         "=B2/sum(B2:D2)"
    ]], row=2,
    value_input_option='USER_ENTERED'
)
