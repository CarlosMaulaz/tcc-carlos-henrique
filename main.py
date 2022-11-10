import importGitHub as Github
import importSonar as Sonar
import importGitLab as Gitlab

'''
# ----------- Obtendo dados do SonarCloud --------------------

# Keys de projetos
projetctKey = "CarlosMaulaz_tcc-carlos-henrique"
brave_key = "brave_brave-core"

# Check da conexão
result = Sonar.sonar.auth.check_credentials()
print(result)

issue_list = Sonar.get_project_issues(brave_key)
component_list = Sonar.get_project_components(brave_key)
rules_list = Sonar.get_project_rules(brave_key)
users_list = Sonar.get_project_users(brave_key)

Sonar.save_csv_issue_list(issue_list)
Sonar.save_csv_component_list(component_list)
Sonar.save_csv_rules_list(rules_list)
Sonar.save_csv_users_list(users_list)

# ------------- Obtendo dados no GitHub ---------------------

# ------------- Lista de Users para teste ----------------------

urlUserLeds = 'https://api.github.com/users/leds'
urlUserPaulo = "https://api.github.com/users/paulossjunior"
urlReposLeds = "https://api.github.com/users/LEDS/repos"

repositorios_github = Github.get_repos('CarlosMaulaz')
contribuidores = Github.get_contributors(repositorios_github)
commits = Github.get_commit(repositorios_github)
# files_do_commit = github.get_commit_files(commits)

Github.save_csv_repository_list(repositorios_github)
Github.save_csv_contributors_list(contribuidores)
Github.save_csv_commit_list(commits)
# github.save_csv_file_list(files_do_commit)

'''
# ------------- Obtendo dados no GitLab ---------------------
list_projects = [21803695]

project_list = Gitlab.get_projects(list_projects)
list_gitlab_commits = Gitlab.get_commits(project_list)
list_gitlab_commits_diff = Gitlab.get_commit_diff(list_gitlab_commits)
print(list_gitlab_commits_diff)

Gitlab.save_csv_project_list(project_list)
Gitlab.save_csv_commit_list(list_gitlab_commits)
Gitlab.save_csv_commit_diff_list(list_gitlab_commits_diff)
