#!/usr/bin/env python
import datetime 

from pylarion.test_run import TestRun  
from pylarion.work_item import TestCase, Requirement  
from pylarion.document import Document  

from config import *
from helpers import *

# Test runs execution status per team
g = gapi.GoogleSpreadSheetAPI(SPREADSHEET_NAME, "Polarion test run by team")

def update_data_by_dict(team, field_dict):
    g.update_sheet(row_number, 1, '=HYPERLINK("'+get_test_run_id(run_fields_dict=field_dict)+'","run")')
    g.update_sheet(row_number, 4, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status=PLANNED))
    g.update_sheet(row_number,5, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status=PASSED))
    g.update_sheet(row_number,7, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status=BLOCKED))
    g.update_sheet(row_number,6, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status=FAILED))
    g.update_sheet(row_number,8, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status=NOT_RUN))

row_number = 3
for team in team_list:
    for curr in field_dicts_list:
        update_data_by_dict(team, field_dicts[curr])
        row_number+=1
    row_number+=2
