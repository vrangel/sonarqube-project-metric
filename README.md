# SonarQube Projects & Metrics 
Usage: `project-metric.py <sonarqube_admin_token> <sonarqube_url>`

# Description
Get some metrics in every project in SonarQube specified by the `<sonarqube_url>` parameter. The metrics are:
- Bugs
- Code Smell
- Test Coverage (%)
- Duplicated Lines (%)
- Vulnerabilities

# Requirements
- Python 3
- Requests (https://github.com/requests/requests)
