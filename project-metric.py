#!/usr/bin/env python3
import sys, requests
token, url = sys.argv[1], sys.argv[2]
payload = {'ps': 500}
projects = requests.get(url + '/api/projects/search', params=payload, auth=(token, ''))
metrics = 5
for project in projects.json()['components']:
    print(project['name'] + ',', end='')
    payload = {'component': project['key'], 'metricKeys': 'bugs,code_smells,coverage,duplicated_lines_density,vulnerabilities'}
    measures = requests.get(url + '/api/measures/component', params=payload)
    for index in range(0, metrics):
        measure = measures.json()['component']['measures']
        try:
            print(measure[index]['metric'] + ':' + measure[index]['value'] + ',', end='')
        except IndexError:
            pass
    print()
