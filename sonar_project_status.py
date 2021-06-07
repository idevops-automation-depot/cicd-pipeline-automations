

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
    print("print from create table")
    print(field_name)
    print(len(field_name))
    print(len(rows))
    tablename.field_names = field_name
    #for row in rows:
    #    print(row)
    #print(rows)
    tablename.add_row(rows)
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
        print("print from pull_keys")
        print(head)
        print(num)
    return head, num, issue
        

def pull_values(issue):
    list1 = []
    for x in info_type_issues(issue):
        item_values = x.values()
        list1 = list(item_values)
        #list1.sort(key = len)
        print("print from pull_values")
        print(list1)
        print(len(list1))
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