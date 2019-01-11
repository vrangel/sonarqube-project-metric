# SonarQube Projects & Metrics 
Usage: `project-metric.py [ <admin_user> <password> | <admin_token> ] <url>`

# Description
Get some metrics in every project in SonarQube specified by the `<url>` parameter. The metrics are:
- Bugs
- Code Smell
- Test Coverage (%)
- Duplicated Lines (%)
- Vulnerabilities
- Lines of Code (ncloc)
- Technical Debt (sqale_index) *
- Reliability remediation effort *
- Security remediation effort *

\* These measures are stored in minutes, but an 8-hour day is assumed when values are shown in days

# Requirements
- Python 3
- Requests (https://github.com/requests/requests)
