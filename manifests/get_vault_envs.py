#!/usr/bin/env python
import os
import json
import os
import urllib3
http = urllib3.PoolManager()
r = http.request(
    'GET',
    'http://vault.idevops.io/v1/kv/data/idevopsio/{environment}/{app_name}'.format(app_name=os.environ["APP"],environment=os.environ["ENVIRONMENT"]),
    headers={
        "X-Vault-Token": os.environ['VAULT_TOKEN']
})
vars_return = json.loads(r.data.decode('utf-8'))["data"]["data"]
vars_string = ""
for var in vars_return:
    if "APP_TYPE" in var:
        vars_string +="\nAPP_TYPE=test"
    else:
        vars_string +="\n{key}={values}".format(key=var, values=vars_return[var])
print(vars_string)
