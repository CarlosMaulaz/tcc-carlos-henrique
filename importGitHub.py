import requests
from github import Github

# First create a Github instance:

# using an access token
g = Github("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")


# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
    print(repo)


# Listando todos os arquivos de um repositório
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)





# Definir função que pega todos os contribuidores de um repositório

def getContributors(urlContributors):
    linkContributors = repo.contributors_url
    resposta = requests.get(linkContributors).json()
    print("Os contribuidores do repositório são:")
    for contributors in resposta:
        id = contributors['id']
        login = contributors['login']
        print(login)
        print(id)

getContributors(repo.contributors_url)


urlUserPaulo = "https://api.github.com/users/paulossjunior"

def getReposUrlFromUser(userURL):
    resposta = requests.get(userURL).json()
    print(resposta['repos_url'])
    respostaRepositorios = requests.get(resposta['repos_url']).json()
    for repositorios in respostaRepositorios:
        print(repositorios["contributors_url"])




getReposUrlFromUser(urlUserPaulo)

