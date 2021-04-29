#!/usr/bin/env python
import os
import json
import os
import urllib3
http = urllib3.PoolManager()
#os.environ["VAULT_DNS"] = "http://vault.idevops.io/v1/kv/data/"
r = http.request('GET','{vault_dns}{vault_path}'.format(vault_dns=os.environ["VAULT_DNS"],vault_path=os.environ["VAULT_PATH"]),headers={"X-Vault-Token": os.environ['VAULT_TOKEN']})
vars_return = json.loads(r.data.decode('utf-8'))["data"]["data"]
temp_secrets = open("tmp_secrets", "w")
for var in vars_return:
        temp_secrets.write("export {key}='{values}' \n".format(key=var, values=vars_return[var]))
temp_secrets.close()
