#!/usr/bin/env python
import requests 
import pprint
import json
import os
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable


table = PrettyTable()
# must be one of: [INFO, MINOR, MAJOR, CRITICAL, BLOCKER]


info_type = ['MINOR', 'MAJOR', 'CRITICAL', 'BLOCKER']

for info_type_items in info_type:
    URL = 'http://localhost:9000/api/issues/search?pageSize100&severities='+ info_type_items +'&componentKeys=org.sonarqube:' + os.environ["APP_NAME"]

    get_request = requests.get(URL, auth=HTTPBasicAuth('admin','admin'))

    data = get_request.json()

#pprint.pprint(data)

    issues = data["issues"]

    for x in issues:
        item = x.keys()
        header = (list(item))
        break

    listfoo = []
    for y in issues:
        item2 = y.values()
        listfoo.append(list(item2))
        


    #print (listfoo)
    print("total number of items " + str(len(listfoo)) + " for " + info_type_items )
    table.field_names = header 
    for z in listfoo:
        table.add_row(z)
        listfoo = []
    print(table)
