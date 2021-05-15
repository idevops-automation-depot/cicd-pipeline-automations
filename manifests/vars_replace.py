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
#for specfic version use this context
#'http://vault.idevops.io/v1/kv/data/idevopsio/{environment}/{app_name}?version={vault_version}'.format(vault_version="6", app_name="crmservice",environment="production"),

yamlfile=open(os.path.dirname(os.path.abspath(__file__)) + "/deployment.template.yml","r").read()
yamlfile=yamlfile.replace("-=TAG=-",os.environ['TAG'])
print(yamlfile)
yamlfilewrite=open(os.path.dirname(os.path.abspath(__file__)) + "/deployment.template.yml","w")
yamlfilewrite.write(yamlfile)
yamlfilewrite.close()

vars_return = json.loads(r.data.decode('utf-8'))
j = vars_return["data"]["data"]
f_path = os.path.dirname(os.path.abspath(__file__)) + "/deployment.template.yml"
f = open(f_path, 'r')
new_lines = []
for line in f:
    for json_var in j:
        json_with_extra_stuff = "-=" + json_var + "=-"
        line = line.replace(json_with_extra_stuff, j[json_var])
    new_lines.append(line)
new_lines = "".join(new_lines)
f_path = os.path.dirname(os.path.abspath(__file__)) + "/deployment.yml"
test = open(f_path, "w")
test.write(new_lines)
test.close()
print("Yaml values replaced.. Success")