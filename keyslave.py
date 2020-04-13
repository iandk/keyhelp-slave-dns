import requests 
import time
import os
import configparser



HOSTNAME = "HOSTNAME"
ENDPOINT = "https://" + HOSTNAME + "/api/v1/domains"
headers = {
    'X-API-Key': 'APIKEY'
    }

while True:
    print('\n')
    print('###')
    print('New run')
    print('###')
    print('\n')
    response = requests.get(ENDPOINT,headers=headers) 
    domains = response.json()
    print(response)



    # Clear file
    if not os.path.exists(HOSTNAME):
        os.makedirs(HOSTNAME)
    zoneFile = open(HOSTNAME + "/" + HOSTNAME + '_slave.db','w')
    zoneFile.write('# AUTO GENERATED!')
    zoneFile.write('\n')
    zoneFile.write('\n')
    zoneFile.close()


    for domain in domains:
        if not domain['is_dns_disabled'] and not domain['is_system_domain'] and not domain['is_subdomain'] and not domain['is_disabled']:
            print(domain['domain'])
            zoneFile = open(HOSTNAME + "/" + HOSTNAME + '_slave.db','a')
            zoneFile.write('zone ' + domain['domain'] + ' {' + '\n')
            zoneFile.write('    type slave;' + '\n')
            zoneFile.write('    HOSTNAMEs { ' + HOSTNAME + '; }' '\n')
            zoneFile.write('    file ' + domain['domain'] + '.db' '\n')
            zoneFile.write('} ' + '\n')

            zoneFile.write('\n')
            zoneFile.close()
    time.sleep(2)


