import datetime  
from pylarion.test_run import TestRun  
from pylarion.work_item import TestCase, Requirement  
from pylarion.document import Document  

from config import *

def get_number_of_reqs_by_planned_in(planned_in=PLANNED_IN, product=PRODUCT):
    reqNumber = Requirement.get_query_result_count("""
        SQL:(SELECT REQ.C_PK FROM LUCENE_QUERY('WorkItem', 
        'project.id: %s AND type:(requirement) AND PLAN:(%s/%s)', 'id') REQ 
        WHERE NOT EXISTS (SELECT TEST.C_PK FROM WORKITEM TEST, STRUCT_WORKITEM_LINKEDWORKITEMS LINK WHERE LINK.FK_WORKITEM = REQ.C_PK AND LINK.FK_P_WORKITEM = TEST.C_PK AND LINK.C_ROLE = 'verifies'))
    """ % (product, product, planned_in))
    return reqNumber

def get_number_of_reqs_by_planned_in_with_linked_work_items(planned_in=PLANNED_IN, product=PRODUCT):
    reqNumber = Requirement.get_query_result_count(""" 
        SQL:(SELECT REQ.C_PK FROM LUCENE_QUERY('WorkItem', 
        'project.id:%s AND type:(requirement) AND PLAN:(%s/%s)','id') REQ 
        WHERE EXISTS (SELECT TEST.C_PK FROM WORKITEM TEST, STRUCT_WORKITEM_LINKEDWORKITEMS LINK WHERE LINK.FK_WORKITEM = REQ.C_PK AND LINK.FK_P_WORKITEM = TEST.C_PK AND LINK.C_ROLE = 'verifies'))
    """ % (product, product, planned_in))
    return reqNumber

def testcase_approved_automated(importance, approved, automated, product=PRODUCT):
    if approved:
        approved_str = 'AND status:approved'
    else:
        approved_str = 'AND NOT status:approved'
    if automated:
        automated_str = 'AND caseautomation.KEY:automated'
    else:
        automated_str = 'AND NOT caseautomation.KEY:automated'   
    
    query = """ 
        project.id:%s AND 
        caseimportance.KEY:%s  
        AND NOT status:inactive
        AND type:testcase 
    """ % (product, importance)

    query += approved_str + ' ' + automated_str
    return TestCase.get_query_result_count(query)

def automation_coverage(automation, importance, product=PRODUCT):
    return TestCase.get_query_result_count(""" 
        project.id:%s AND 
        caseimportance.KEY:%s  
        AND NOT status:inactive
        AND type:testcase 
        AND caseautomation.KEY:%s
    """ % (product, importance, automation))

def find_number_of_TCs_per_status(status='*', planned_in=PLANNED_IN, product=PRODUCT):
    testrun_list = TestRun.search(query='plannedin.KEY:'+planned_in, project_id=product)
    num_of_tests = 0
    for run in testrun_list:    
        query = '(TEST_RECORDS:(' + product + '/' + run.test_run_id + ',' + status +') )'
        num_of_tests += TestCase.get_query_result_count(query)
    return num_of_tests

def find_number_of_TCs_per_status_and_run_fields(
    run_fields_dict, status='*', planned_in=PLANNED_IN, product=PRODUCT):
    query = 'plannedin.KEY:'+planned_in
    for key, value in run_fields_dict.iteritems():
        query += ' AND ' + key + ':' + value 
    testrun_list = TestRun.search(query=query, project_id=product)
    num_of_tests = 0
    for run in testrun_list:
        query = '(TEST_RECORDS:(' + product + '/' + run.test_run_id + ',' + status +') )'
        num_of_tests += TestCase.get_query_result_count(query)
    return num_of_tests


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
g.update_sheet(44,6, find_number_of_TCs_per_status(status='passed'))
g.update_sheet(44,6, find_number_of_TCs_per_status(status='failed'))
g.update_sheet(44,7, find_number_of_TCs_per_status(status='blocked'))

# Test runs execution status per plan and run properties
field_dict = {
    'env_tier': 'tier1',
    'env_os.KEY': 'rhcos',
    'env_storage.KEY': 'nfs',
}
g.update_sheet(5,11, find_number_of_TCs_per_status_and_run_fields(run_fields_dict=field_dict, status='*'))
g.update_sheet(5,13, find_number_of_TCs_per_status_and_run_fields(run_fields_dict=field_dict, status='@null'))
g.update_sheet(5,12, find_number_of_TCs_per_status_and_run_fields(run_fields_dict=field_dict, status='passed'))
field_dict = {
    'env_tier': 'tier1',
    'env_os.KEY': 'rhcos',
    'env_storage.KEY': 'ocs-storagecluster-ceph-rbd',
}
g.update_sheet(6,11, find_number_of_TCs_per_status_and_run_fields(run_fields_dict=field_dict, status='*'))
g.update_sheet(6,13, find_number_of_TCs_per_status_and_run_fields(run_fields_dict=field_dict, status='@null'))
g.update_sheet(6,12, find_number_of_TCs_per_status_and_run_fields(run_fields_dict=field_dict, status='passed'))
