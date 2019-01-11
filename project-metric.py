#!/usr/bin/env python3
import sys, requests
usage = 'Usage: projects.py [ <user> <password> | <token> ] <url>'
if  len(sys.argv) == 2 and sys.argv[1] in ['-h', '-H', '--help']:
    sys.exit(usage)
elif len(sys.argv) == 3: # admin token and sonarqube url
    user_token, password, url = sys.argv[1], '', sys.argv[2]
elif len(sys.argv) == 4: # admin user, password and sonarqube url
    user_token, password, url = sys.argv[1], sys.argv[2], sys.argv[3]
else:
    sys.exit('Syntax error. ' + usage)
if url.endswith('/'):
    url = url[:-1]
payload = {'ps': 500}
projects = requests.get(url + '/api/projects/search', params=payload, auth=(user_token, password))
for project in projects.json()['components']:
    payload = {'component': project['key'], 'metricKeys': 'bugs,code_smells,coverage,duplicated_lines_density,vulnerabilities,ncloc,sqale_index,security_remediation_effort,reliability_remediation_effort'}
    metrics = requests.get(url + '/api/measures/component', params=payload).json()['component']['measures']
    if len(metrics) > 0:
        print(project['name'] + ',', end='')
    else:
        print(project['name'], end='')
    for index in range(0, len(metrics)):
        if index == len(metrics) -1:
            print(metrics[index]['metric'] + ':' + metrics[index]['value'], end='')
        else:
            print(metrics[index]['metric'] + ':' + metrics[index]['value'] + ',', end='')
    print()
