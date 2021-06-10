#!/usr/bin/env python
import requests 
import pprint
import json
import os
from requests.auth import HTTPBasicAuth

#creates a a project with project name and project key, project key will have to be the same on sonar_scan 
URL = 'http://172.17.0.1:9000/api/projects/create?project=org.sonarqube:' +os.environ["APP_NAME"] + '&name=' + os.environ["APP_NAME"]
get_request = requests.post(URL, auth=HTTPBasicAuth('admin','admin'))
pprint.pprint(get_request.json())