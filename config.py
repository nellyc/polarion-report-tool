import bugzilla
import yaml
import sys
import os
import google_api as gapi

# # [CHANGE NEEDED] Add the relevant information for you report
cfg_path = os.path.expanduser('~/.gapi/personal_cfg.yml')

if len(sys.argv) != 2:
    raise IndexError("You must provide the spreadsheet name to work with")

SPREADSHEET_NAME = sys.argv[1]
# with open(cfg_path, 'r') as ymlfile:
#     cfg = yaml.load(ymlfile)
#     USER = cfg['bugzilla']['user']
#     PASSWORD = cfg['bugzilla']['password']

g = gapi.GoogleSpreadSheetAPI(SPREADSHEET_NAME, "Dashboard configuration")

PRODUCT = g.get_cell_value(2, 1)
VERSION = g.get_cell_value(2, 4)
PLANNED_IN = g.get_cell_value(2,5)
# # The version flag should contain only x and y releases:

# [CHANGE NEEDED] List here all the teams you want to sample, for example:
team1 = "virt"
team2 = "storage"
team3 = "network"
team4 = "infra"

all_team = [team1, team2, team3]

severity = {
    "urgent": 1,
    "high": 2,
    "medium": 3,
    "low": 4,
    "unspecified": 5
}

BUGS_BY_TEAM = {
    team1: [],
    team2: [],
    team3: [],
}

# [CHANGE NEEDED] Add *ALL* the product components exist in Bugzilla for your
# product
COMPONENTS = {
    'Documentation': [],
    'Release': [],
    'Installation': [],
    'Virtualization': [],
    'Networking': [],
    'Storage': [],
    'Providers': [],
    'RFE': [],
    'V2V': [],
    'Guest Support': [],
    'SSP': [],
}

