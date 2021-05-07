#!/usr/bin/env python
import requests 
import pprint
import json
from requests.auth import HTTPBasicAuth



URL = 'http://localhost:9000/api/projects/create?project=org.sonarqube:' +["APP_NAME"] + '&name=' + ["APP_NAME"]


get_request = requests.post(URL, auth=HTTPBasicAuth('admin','admin'))

pprint.pprint(get_request.json())