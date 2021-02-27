from boto.route53.record import ResourceRecordSets
import os
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

config.load_kube_config()
v1 = client.CoreV1Api() #Access k8s API
ret = v1.list_service_for_all_namespaces(watch=False) #Get list of services to search
for i in ret.items:
    if i.metadata.name == os.environ['service_name']: #Compare metadata name to declared service name, and...
        new_ip = i.status.load_balancer.ingress[0].ip #Save IP for that service to variable (is a str by default)

result = dns.resolver.resolve(os.environ['domainName'], 'A') #DNS resolver to get current IP
for ipval in result:
    old_ip = ipval.to_text() # IP, converted to string, saved to variable

    if old_ip == new_ip: #Compares the two IPs-as-strings
        print('{domain_name} is current. Address is: {new_ip}'.format(domain_name=os.environ['domainName'], new_ip=new_ip))
        sys.exit(0)

    else:
        print('Updating {domain_name}: {old_ip} -> {new_ip}'.format(domain_name=s.environ['domainName'], old_ip=old_ip, new_ip=new_ip))

        change_set = ResourceRecordSets(conn, os.environ['hosted_zone_id'])
        changes1 = change_set.add_change("DELETE", os.environ['domainName'], "A", ttl=60) #Deleting old record...
        changes1.add_value(old_ip) #...by passing in the old DNS IP
        change_set.commit()

        changes2 = change_set.add_change("UPSERT", os.environ['domainName'], "A", ttl=60) #Upserting new record...
        changes2.add_value(new_ip) #... by passing in new, service IP
        change_set.commit()