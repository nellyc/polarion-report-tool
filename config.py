import bugzilla
import yaml
import sys
import os
import google_api as gapi


if len(sys.argv) != 2:
    raise IndexError("You must provide the spreadsheet name to work with")

SPREADSHEET_NAME = sys.argv[1]

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
