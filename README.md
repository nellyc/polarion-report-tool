# polarion-report-tool

This tool will allow you to create a Quality dashboard for your product with Polarion status.

## Currently the tool supports:
1. fetching requirements coverage
![alt text](https://github.com/nellyc/polarion-report-tool/blob/master/images/reqs.png) 

2. fetching approved/automated coverage
![alt text](https://github.com/nellyc/polarion-report-tool/blob/master/images/approved_automated.png) 

3. fetching automation coverage
![alt text](https://github.com/nellyc/polarion-report-tool/blob/master/images/automated.png) 

4. fetching test run status by field
![alt text](https://github.com/nellyc/polarion-report-tool/blob/master/images/test_run_by_field.png)

5. fetching test run status by field & team
![alt text](https://github.com/nellyc/polarion-report-tool/blob/master/images/test_run_by_field_and_team.png) 

6. execution status by version
![alt text](https://github.com/nellyc/polarion-report-tool/blob/master/images/execution_by_version.png)

7. Automation coverage trend
![alt text](https://github.com/nellyc/polarion-report-tool/blob/master/images/automation_trend.png)

## Requires:
1. Copy the example xls template to your google drive, and update the 'Dashboard configuration' tab with your product data
2. Enable interaction with Google spreadsheet, follow the steps in https://developers.google.com/sheets/api/quickstart/python and after, steps in here https://gspread.readthedocs.io/en/latest/oauth2.html#oauth-credentials (until step 6). Name the Json from step 3 as 'google_api_secret.json'

    Create .gapi directory under ~/. with: $ mkdir ~/.gapi

    place the google_api_secret.json under ~/.gapi/google_api_secret.json

    Ensure you give 'Edit' permissions in your copied spreadsheet, to the 'client' in this json file
3. pylarion
4. update example_team.yaml, example_field_dicts.yaml & example_field_dicts_list.yaml with the parameters you want to get the reports for

## Usage:
1. executing python3 'polarion_report.py "YOUR TEMPLATE - Quality Dashboard"' will: 
   - fetch requirements coverage
   - fetch approved/automated coverage
   - fetch current automation coverage
   - update current automation coverage on the automation coverage trend table & graph
2. executing python3 'run_report.py "YOUR TEMPLATE - Quality Dashboard"'
   will populate a table of test runs with number of executed/failed/passed tests & a calculation of the quality of the execution, by the defined fields (from the yamls)
3. executing python3 'run_report_by_team.py "YOUR TEMPLATE - Quality Dashboard"'
   will populate a table of test runs with number of executed/failed/passed tests & a calculation of the quality of the execution, by the defined fields & defined teams (from the yamls)
   




