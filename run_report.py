#!/usr/bin/env python
import datetime 
import time

from pylarion.test_run import TestRun  
from pylarion.work_item import TestCase, Requirement  
from pylarion.document import Document  

from config import *
from helpers import *

# Test runs execution status per team
g = gapi.GoogleSpreadSheetAPI(SPREADSHEET_NAME, "Polarion test run")

# Test runs execution status per plan and run properties
row_number = 3
for curr in field_dicts_list:
    g.update_sheet(row_number,5, find_number_of_TCs_per_status_and_run_fields(run_fields_dict=field_dicts[curr], status=PLANNED))
    g.update_sheet(row_number,6, find_number_of_TCs_per_status_and_run_fields(run_fields_dict=field_dicts[curr], status=PASSED))
    g.update_sheet(row_number,7, find_number_of_TCs_per_status_and_run_fields(run_fields_dict=field_dicts[curr], status=NOT_RUN))
    row_number += 1

now = datetime.datetime.now()
g.update_sheet(50, 1, 'Last update: ' + now.strftime("%Y-%m-%d %H:%M"))
