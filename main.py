import importGitHub
import importSonar

# Obtendo dados do SonarCloud

# Keys de projetos
projetctKey = "CarlosMaulaz_tcc-carlos-henrique"
brave_key = "brave_brave-core"

# Check da conexão
result = importSonar.sonar.auth.check_credentials()
print(result)

importSonar.get_project_issues(projetctKey)

'''

# Obtendo dados no GitHub

# -------------Lista de Users para teste-------------------
urlUserLeds = 'https://api.github.com/users/leds'
urlUserPaulo = "https://api.github.com/users/paulossjunior"
urlReposLeds = "https://api.github.com/users/LEDS/repos"

repository_url = importGitHub.get_repos_url_from_user(urlUserPaulo)
contributors_url = importGitHub.get_contributors_url_from_repos(repository_url)
contributors = importGitHub.get_contributors(contributors_url)

# Abrindo um arquivo csv e escrevendo um cabeçario

f = open("Lista de contribuidores.csv", "w")
f.write("ID")
f.write(",")
f.write("login")
f.write(",")
f.write("contribuição")
f.write("\n")

for contribuidores in contributors:
    print("passei por aqui")
    f.write(str(contribuidores.id))
    f.write(",")
    f.write(contribuidores.login)
    f.write(",")
    f.write(str(contribuidores.contributions))
    f.write("\n")

f.close()


# Prints de conferencia

# print(repository_url)

# for contri_url in contributors_url:
#     print(contri_url)



'''

