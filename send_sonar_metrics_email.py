#!/usr/bin/env python3

import sys, requests, smtplib
from email.message import EmailMessage

TOKEN = sys.argv[1]
URL = sys.argv[2]
LOGIN = sys.argv[3]
PASSW = sys.argv[4]
FROMADDR = sys.argv[5]
TOADDR = sys.argv[6]

if URL.endswith('/'):
    URL = URL[:-1]

file = open('attachment.txt', 'w')
projects = requests.get(URL + '/api/projects/search', params={'ps': 500}, auth=(TOKEN, ''))
for project in projects.json()['components']:
    payload = {
        'component': project['key'],
        'metricKeys': 'bugs,code_smells,coverage,duplicated_lines_density,vulnerabilities,ncloc,sqale_index,security_remediation_effort,reliability_remediation_effort'
    }
    metrics = requests.get(URL + '/api/measures/component', params=payload).json()['component']['measures']
    if len(metrics) > 0:
        file.write(project['name'] + ',')
    else:
        file.write(project['name'])
    metrics_length = len(metrics)
    for index in range(0, metrics_length):
        if index == metrics_length -1:
            file.write(metrics[index]['metric'] + ':' + metrics[index]['value'])
        else:
            file.write(metrics[index]['metric'] + ':' + metrics[index]['value'] + ',')
    file.write('\n')
file.close()

msg = EmailMessage()
msg['Subject'] = 'SonarQube Metrics'
msg['From'] = FROMADDR
msg['To'] = TOADDR
msg.set_content('''\
Get some metrics in every project in SonarQube. The metrics are:

Bugs
Code Smell
Test Coverage (%)
Duplicated Lines (%)
Vulnerabilities
Lines of Code (ncloc)
Technical Debt (sqale_index)*
Reliability remediation effort*
Security remediation effort*

*These metrics are stored in minutes, but an 8-hour day is assumed when values are shown in days.
''')

with open('attachment.txt', 'r') as f:
    msg.add_attachment(f.read(), filename='metrics.txt')

server = smtplib.SMTP('smtp-mail.outlook.com')
server.starttls()
server.login(LOGIN, PASSW)
server.send_message(msg)
server.quit()
