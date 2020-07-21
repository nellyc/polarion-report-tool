import yaml
import sys
import os
import google_api as gapi


import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# [CHANGE NEEDED] Adjust yamls to your needs
with open(os.path.join(PROJECT_ROOT, 'example_team.yaml')) as f:
    team_list = yaml.full_load(f)
with open(os.path.join(PROJECT_ROOT, 'example_field_dicts_list.yaml')) as f:
    field_dicts_list = yaml.full_load(f)
with open(os.path.join(PROJECT_ROOT, 'example_field_dicts.yaml')) as f:
    field_dicts = yaml.full_load(f)
# Put your Polarion URL here, including project, this is used to create hyperlinks to test runs
POLARION_FULL_URL = 'https://my.polarion.com/polarion/#/project/MYPROJECT/'

if len(sys.argv) != 2:
    raise IndexError("You must provide the spreadsheet name to work with")

SPREADSHEET_NAME = sys.argv[1]

g = gapi.GoogleSpreadSheetAPI(SPREADSHEET_NAME, "Dashboard configuration")
PRODUCT = g.get_cell_value(2, 1)
VERSION = g.get_cell_value(2, 4)
PLANNED_IN = g.get_cell_value(2,5)


CRITICAL = 'critical'
H_M_L = '(high medium low)'
ANY_IMPORTANCE = '(critical high medium low)'

#statuses
PLANNED = '*'
ATTEMPTED = '@any'
NOT_RUN = '@null'
PASSED = 'passed'
FAILED = 'failed'
BLOCKED = 'blocked'

AUTOMATED = 'automated'
NOT_AUTOMATED = 'notautomated'
MANUAL_ONLY = 'manualonly'
