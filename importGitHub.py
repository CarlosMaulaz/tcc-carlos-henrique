import requests
from github import Github

# Token de acesso para autenticação de acesso à API
g = Github("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")


urlUserLeds = 'https://api.github.com/users/leds'

urlUserPaulo = "https://api.github.com/users/paulossjunior"

urlReposLeds = "https://api.github.com/users/LEDS/repos"

global contributors
contributors = []

'''

Classes 

'''


class Contributor:
    def __init__(self, id, login, contributions):
        self.id = id
        self.login = login
        self.contributions = contributions


'''

Funções para a extração de dados

'''
# A função recebe um URL api.* de um user do gitHub e retorna a URL do repositório


def get_repos_url_from_user(user_url):
    resposta = requests.get(user_url).json()
    return resposta['repos_url']


# A função recebe um URL de um repositório e retorna a lista de contribuidores de todos os projetos

def get_contributors_url_from_repos(repos_url):
    url = []
    resposta_repositorios = requests.get(repos_url).json()
    for repositorios in resposta_repositorios:
        url.append(repositorios["contributors_url"])
    return url


def get_contributors(url_contributors):
    contributors_list = []
    for url_contributor in url_contributors:
        resposta = requests.get(url_contributor).json()
        for resposta_contributors in resposta:
            id = resposta_contributors['id']
            login = resposta_contributors['login']
            contributions = resposta_contributors['contributions']
            print(id)
            print(login)
            print(contributions)
            contributor_aux = Contributor(id, login, contributions)
            # Lógica para adicionar apenas novos IDs
            if contributor_aux not in contributors_list:
                contributors_list.append(contributor_aux)
            '''
            for contributor_for in contributors_list:
                if contributor_for == contributor_aux:
                    aux = aux+1
            contributors_list.append(contributor_aux)
            '''
    return contributors_list


'''    
    resposta = requests.get(url_contributors).json()
    print("Os contribuidores do repositório são:")
    for respostaContributors in resposta:
        id = respostaContributors['id']
        login = respostaContributors['login']
        print(login)
        print(id)
'''

repos = get_repos_url_from_user(urlUserPaulo)

print(repos)

urlsContributors = get_contributors_url_from_repos(repos)

contributors = get_contributors(urlsContributors)
'''
for contribuidores in contributors:
    print(contribuidores.login)
'''
p1 = Contributor(1234, "carlosmaulaz", 23)
contributors.append(p1)
print(contributors[0].id)
