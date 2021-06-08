#!/usr/bin/env python
from typing import ItemsView
import requests 
import pprint
import json
import os
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable

info_type = ['MINOR', 'MAJOR', 'CRITICAL', 'BLOCKER']

# creats table by adding filed names, and row while iterating the list 
def create_table(table, field_name, rows):
    counter = 1
    for f, r in zip(field_name, rows):
        print(table)
        tablename = table + str(counter) #due to reports being different sizes, made it so it will just create a new table for each info for the time being 
        tablename = PrettyTable()
        tablename.field_names = f
        tablename.add_row(r)
        counter += 1
        print(tablename)


# pulls info with api, and specifying specifically which data we want with the tag
def info_type_issues(issue):
  URL = 'http://172.17.0.1:9000/api/issues/search?pageSize100&severities='+ str(issue) +'&componentKeys=org.sonarqube:' + os.environ["APP_NAME"]
  get_request = requests.get(URL, auth=HTTPBasicAuth('admin','admin'))
  data = get_request.json()
  #pprint.pprint(data)
  issues = data["issues"]
  return issues

def pull_keys(issue):
    head = []
    for x in info_type_issues(issue):
        item = x.keys()
        head.append(list(item))
        num = len(head)
    return head, issue
        
def pull_values(issue):
    list1 = []
    for x in info_type_issues(issue):
        item_values = x.values()
        list1.append(list(item_values))
    return list1

def save_value(value):
    value = value
    return value

for issue in info_type:
    if pull_keys(issue) == None:
        print("no " + issue +" issues found")
    else:
        print("\n" + issue + " Page Report")
        result1 = pull_keys(issue)
        array_list = result1[0]
        type_of_issue = result1[1]
        result2 = pull_values(issue)
        rows = result2
        create_table(type_of_issue,array_list, rows)