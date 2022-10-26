import requests
from sonarqube import SonarCloudClient

sonar = SonarCloudClient(sonarcloud_url="https://sonarcloud.io", token='1bda9a037facea77fc3cd5e6e0e6ff05acded5cf')

def get_project_issues(project_id):
    url = 'https://sonarcloud.io/api/issues/search'
    query = {'componentKeys' : project_id}
    r = requests.get(url, params=query)
    issues_json = r.json()
    print(issues_json)
















'''
url = 'https://sonarcloud.io/api//measures/component_tree'
query = {'component': 'keyJabref4.2', 'metricKeys': 'sqale_index', 'ps': 100, 'p': 1}
r = requests.get(url, params=query)
metrics_dict = r.json()

print(metrics_dict)
'''
'''
print("##################################")
url = 'https://sonarcloud.io/api/project_analyses/search'
query = {'project': 'brave_brave-core'}
r = requests.get(url, params=query)
metrics_dict = r.json()
print(metrics_dict)
'''

#print(resposta)

#projects = list(sonar.projects.search_projects())





#task = sonar.ce.get_task()