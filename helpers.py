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
    for key, value in run_fields_dict.items():
        query += ' AND ' + key + ':' + value 
    testrun_list = TestRun.search(query=query, project_id=product)
    num_of_tests = 0
    for run in testrun_list:
        query = '(TEST_RECORDS:(' + product + '/' + run.test_run_id + ',' + status +') )'
        num_of_tests += TestCase.get_query_result_count(query)
    return num_of_tests

def find_number_of_TCs_per_status_and_run_fields_and_team(
    team, run_fields_dict, status='*', planned_in=PLANNED_IN, product=PRODUCT):
    query = 'plannedin.KEY:'+planned_in
    for key, value in run_fields_dict.items():
        query += ' AND ' + key + ':' + value 
    testrun_list = TestRun.search(query=query, project_id=product)
    num_of_tests = 0
    for run in testrun_list:
        query = '(TEST_RECORDS:(' + product + '/' + run.test_run_id + ',' + status + ')) AND casecomponent.KEY:(' + team + ')'
        num_of_tests += TestCase.get_query_result_count(query)
    return num_of_tests

def get_test_run_id(run_fields_dict, planned_in=PLANNED_IN, product=PRODUCT):
    query = 'plannedin.KEY:'+planned_in
    for key, value in run_fields_dict.items():
        query += ' AND ' + key + ':' + value 
    testrun_list = TestRun.search(query=query, project_id=product)
    # There is an assumption here that there is only 1 test run with such values
    # Adjust if your case is different 
    if testrun_list:
        run_id = testrun_list[0].test_run_id
        return POLARION_FULL_URL + 'testrun?id=' + run_id
    return ''
