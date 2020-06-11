#!/usr/bin/env python
import datetime 

from pylarion.test_run import TestRun  
from pylarion.work_item import TestCase, Requirement  
from pylarion.document import Document  

from config import *
from helpers import *

g = gapi.GoogleSpreadSheetAPI(SPREADSHEET_NAME, "PQI Metrics")

# Requirements coverage 
g.update_sheet(2, 1, get_number_of_reqs_by_planned_in())
g.update_sheet(3, 1, get_number_of_reqs_by_planned_in_with_linked_work_items())

# Automation coverage and approved
g.update_sheet(22, 2, testcase_approved_automated("critical", True, False))
g.update_sheet(22, 3, testcase_approved_automated("critical", True, True))
g.update_sheet(22, 4, testcase_approved_automated("critical", False, False))
g.update_sheet(22, 6, testcase_approved_automated("critical", False, True))
g.update_sheet(23, 6, testcase_approved_automated("(high medium low)", True, False))
g.update_sheet(23, 3, testcase_approved_automated("(high medium low)", True, True))
g.update_sheet(23, 4, testcase_approved_automated("(high medium low)", False, False))
g.update_sheet(23, 6, testcase_approved_automated("(high medium low)", False, True))

# Automation coverage 
g.update_sheet(27,2, automation_coverage("automated", "critical"))
g.update_sheet(27,3, automation_coverage("notautomated", "critical"))
g.update_sheet(27,4, automation_coverage("manualonly", "critical"))
g.update_sheet(28,2, automation_coverage("automated", "(high medium low)"))
g.update_sheet(28,3, automation_coverage("notautomated", "(high medium low)"))
g.update_sheet(28,4, automation_coverage("manualonly", "(high medium low)"))

# Test runs execution status per plan
g.update_sheet(44,2, find_number_of_TCs_per_status(status='*'))
g.update_sheet(44,3, find_number_of_TCs_per_status(status='@any'))
g.update_sheet(44,4, find_number_of_TCs_per_status(status='@null'))
g.update_sheet(44,5, find_number_of_TCs_per_status(status='passed'))
g.update_sheet(44,6, find_number_of_TCs_per_status(status='failed'))
g.update_sheet(44,7, find_number_of_TCs_per_status(status='blocked'))

