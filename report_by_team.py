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
    g.update_sheet(row_number, 4, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status='*'))
    g.update_sheet(row_number,5, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status='passed'))
    g.update_sheet(row_number,7, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status='blocked'))
    g.update_sheet(row_number,6, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status='failed'))
    g.update_sheet(row_number,8, find_number_of_TCs_per_status_and_run_fields_and_team(team, run_fields_dict=field_dict, status='@null'))

team_list = [
    'Storage',
    'Virt SSP Guest_Support Fencing',
    'Network',
    'OCP_console',
]
field_dict_tier1_rhcos_nfs = {
    'env_tier': 'tier1',
    'env_os.KEY': 'rhcos',
    'env_storage.KEY': 'nfs',
}
field_dict_tier1_rhcos_ocs = {
    'env_tier': 'tier1',
    'env_os.KEY': 'rhcos',
    'env_storage.KEY': 'ocs-storagecluster-ceph-rbd',
}
field_dict_tier1_rhcos_hpp = {
        'env_tier': 'tier1',
        'env_os.KEY': 'rhcos',
        'env_storage.KEY': 'hostpath-provisioner',
    }
field_dict_tier2_rhcos = {
    'env_tier': 'tier2',
    'env_os.KEY': 'rhcos',
}

row_number = 3
for team in team_list:
    update_data_by_dict(team, field_dict_tier1_rhcos_nfs)
    row_number+=1
    update_data_by_dict(team, field_dict_tier1_rhcos_ocs)
    row_number+=1
    update_data_by_dict(team, field_dict_tier1_rhcos_hpp)
    row_number+=1
    update_data_by_dict(team, field_dict_tier2_rhcos)
    row_number+=3
  