from boto.route53.record import ResourceRecordSets
import os
import subprocess
from kubernetes import client, config
import dns.resolver
import sys
import boto

# os.environ['domainName'] # Domain name variable
# os.environ['service_name'] # Name of service saved to env variable
# os.environ['hosted_zone_id'] # Route53 zone ID
# os.environ['aws_access_key_id']
# os.environ['aws secret_access_key']


conn = boto.connect_route53(os.environ['aws_access_key_id'], os.environ['aws secret_access_key']) #establish connection to R53, pass in keys)
zone = conn.get_zone(os.environ['domainName']) #Get zone for domain in question

config.load_kube_config() #loading kubeconfig file to access k8s api
v1 = subprocess.run('kubectl get --all-namespaces ingress', capture_output=True, text=True) #running command to get ingress based on the k8s config file , capturing output to work with it
lines = v1.stdout.splitlines() #splitting the resulting string into a list of two long strings
newDict = {k: v for k, v in zip(lines[0].split(), lines[1].split())} # creating a dictionary out of those two long strings, by splitting on whitespaces
new_ip = newDict.get('ADDRESS') # assigning the value matching the key 'ADDRESS' to variable

result = dns.resolver.resolve(os.environ['domainName'], 'A') #DNS resolver to get current IP
for ipval in result:
    old_ip = ipval.to_text() # IP, converted to string, saved to variable

    if new_ip:

        if old_ip == new_ip: #Compares the two IPs-as-strings
            print('{domain_name} is current. Address is: {new_ip}'.format(domain_name=os.environ['domainName'], new_ip=new_ip))
            sys.exit(0)

        else:
            print('Updating {domain_name}: {old_ip} -> {new_ip}'.format(domain_name=s.environ['domainName'], old_ip=old_ip, new_ip=new_ip))

            change_set = ResourceRecordSets(conn, os.environ['hosted_zone_id']) # declaring what set we are about to be changing
            changes1 = change_set.add_change("DELETE", os.environ['domainName'], "A", ttl=60) #Deleting old record...
            changes1.add_value(old_ip) #...by passing in the old DNS IP
            change_set.commit()

            changes2 = change_set.add_change("UPSERT", os.environ['domainName'], "A", ttl=60) #Upserting new record...
            changes2.add_value(new_ip) #... by passing in new, service IP
            change_set.commit()
    else:
        print('There is no ingress IP found.')
        sys.exit(0)