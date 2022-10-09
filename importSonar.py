from sonarqube import SonarCloudClient
sonar = SonarCloudClient(sonarcloud_url="https://sonarcloud.io", token='1bda9a037facea77fc3cd5e6e0e6ff05acded5cf')

projetctKey = "CarlosMaulaz_tcc-carlos-henrique"

# Check da conexão
result = sonar.auth.check_credentials()
print(result)

branches = sonar.project_branches.search_project_branches(project=projetctKey)

print(type(branches))
print(branches)

#projects = list(sonar.projects.search_projects())



#task = sonar.ce.get_task()