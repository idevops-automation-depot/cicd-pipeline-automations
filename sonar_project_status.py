

#!/usr/bin/env python
from typing import ItemsView
import requests 
import pprint
import json
import os
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable



info_type = ['MINOR', 'MAJOR', 'CRITICAL', 'BLOCKER']

def create_table(table, field_name, rows):
    #print(table)
    table = PrettyTable()
    table.field_names = field_name
    print(field_name)
    print(rows)
    for row in rows:
        table.add_row(row)
    print(table)

def info_type_issues(issue):
  URL = 'http://172.17.0.1:9000/api/issues/search?pageSize100&severities='+ str(issue) +'&componentKeys=org.sonarqube:' + os.environ["APP_NAME"]
  get_request = requests.get(URL, auth=HTTPBasicAuth('admin','admin'))
  data = get_request.json()
  #pprint.pprint(data)
  issues = data["issues"]
  return issues

def pull_keys(issue):
    for x in info_type_issues(issue):
        item = x.keys()
        print("printing items \n\n\n\n\n\n\n")
        print(item)
        head = list(item)
        num = (len(head))
        return head, num, issue
        break

def pull_values(issue):
    list1 = []
    for x in info_type_issues(issue):
        item_values = x.values()
        list1.append(list(item_values))
    print(list1)    
    return list1

for issue in info_type:
    if pull_keys(issue) == None:
        print("no " +issue +" issues found")
    else:
        print("\n" + issue + " Page Report")
        result1 = pull_keys(issue)
        array_list = result1[0]
        type_of_issue = result1[2]
        result2 = pull_values(issue)
        rows = result2
        create_table(type_of_issue,array_list, rows)