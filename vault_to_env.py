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

f_path = os.environ["APPLICATION_PATH"] + "/manifests/deployment.template.yml"
f = open(f_path, 'r')
new_lines = []
for line in f:
    for json_var in vars_return:
        json_with_extra_stuff = "-=" + json_var + "=-"
        line = line.replace(json_with_extra_stuff, vars_return[json_var])
    new_lines.append(line)
new_lines = "".join(new_lines)
f_path = os.environ["APPLICATION_PATH"] + "/manifests/deployment.yml"
test = open(f_path, "w")
test.write(new_lines)
test.close()