import yaml
import sys
import os
import google_api as gapi

# # [CHANGE NEEDED] Add the relevant information for you report
cfg_path = os.path.expanduser('~/.gapi/personal_cfg.yml')

with open(cfg_path, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# [CHANGE NEEDED] Adjust yamls to your needs
with open('example_team.yaml') as f:
    team_list = yaml.load(f)
with open('example_field_dicts_list.yaml') as f:
    field_dicts_list = yaml.load(f)
with open('example_field_dicts.yaml') as f:
    field_dicts = yaml.load(f)

if len(sys.argv) != 2:
    raise IndexError("You must provide the spreadsheet name to work with")

SPREADSHEET_NAME = sys.argv[1]

g = gapi.GoogleSpreadSheetAPI(SPREADSHEET_NAME, "Dashboard configuration")
PRODUCT = g.get_cell_value(2, 1)
VERSION = g.get_cell_value(2, 4)
PLANNED_IN = g.get_cell_value(2,5)

