import importGitHub
import importSonar

# ----------- Obtendo dados do SonarCloud --------------------

# Keys de projetos
projetctKey = "CarlosMaulaz_tcc-carlos-henrique"
brave_key = "brave_brave-core"

# Check da conexão
result = importSonar.sonar.auth.check_credentials()
print(result)

issue_list = importSonar.get_project_issues(brave_key)
component_list = importSonar.get_project_components(brave_key)
rules_list = importSonar.get_project_rules(brave_key)
users_list = importSonar.get_project_users(brave_key)

importSonar.save_csv_issue_list(issue_list)
importSonar.save_csv_component_list(component_list)
importSonar.save_csv_rules_list(rules_list)
importSonar.save_csv_users_list(users_list)


# ------------- Obtendo dados no GitHub ---------------------

# ------------- Lista de Users para teste ----------------------

urlUserLeds = 'https://api.github.com/users/leds'
urlUserPaulo = "https://api.github.com/users/paulossjunior"
urlReposLeds = "https://api.github.com/users/LEDS/repos"

# --------------------------------------------------------------

repository_url = importGitHub.get_repos_url_from_user(urlUserPaulo)
contributors_url = importGitHub.get_contributors_url_from_repos(repository_url)
contributors = importGitHub.get_contributors(contributors_url)
importGitHub.save_csv_contributors_list(contributors)



