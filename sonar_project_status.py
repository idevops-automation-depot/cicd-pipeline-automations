

#!/usr/bin/env python
from typing import ItemsView
import requests 
import pprint
import json
import os
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable



info_type = ['MINOR', 'MAJOR', 'CRITICAL', 'BLOCKER']

def create_table(table, field_name, rows, lengths):
    tablename = table + str(lengths)
    tablename = PrettyTable()
    tablename.field_names = field_name
    for row in rows:
        tablename.add_row(row)
    print(tablename)

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
        head = list(item)
        head.sort(key = len)
        num = len(head)
        return head, num, issue
        

def pull_values(issue):
    list1 = []
    for x in info_type_issues(issue):
        item_values = x.values()
        list1.append(list(item_values))
        list1.sort(key = len)
    return list1

def save_value(value):
    value = value
    return value

for issue in info_type:
    if pull_keys(issue) == None:
        print("no " +issue +" issues found")
    else:
        print("\n" + issue + " Page Report")
        result1 = pull_keys(issue)
        array_list = result1[0]
        length_of_array = result1[1]
        type_of_issue = result1[2]
        result12 = save_value(length_of_array)
        result2 = pull_values(issue)
        rows = result2
        create_table(type_of_issue,array_list, rows, length_of_array)