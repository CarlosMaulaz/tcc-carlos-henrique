import requests
import pathlib
import os
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

# A função recebe um URL api.* de um user do gitHub e retorna a URL do repositório desse User

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

# Recebe uma Array de url's de contribuidores dos repositórios e retorna uma lista de objetos Contruibutor
def get_contributors(url_contributors):
    contributors_list = []
    for url_contributor in url_contributors:
        resposta = requests.get(url_contributor).json()
        for resposta_contributors in resposta:
            id = resposta_contributors['id']
            login = resposta_contributors['login']
            contributions = resposta_contributors['contributions']
            # print(id)
            # print(login)
            # print(contributions)
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

def save_csv_contributors_list(contributors_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\contributors_list.csv"), "w")
    f.write("ID")
    f.write(";")
    f.write("login")
    f.write(";")
    f.write("contribuicao")
    f.write("\n")

    for contribuidores in contributors_list:
        f.write(str(contribuidores.id))
        f.write(";")
        f.write(contribuidores.login)
        f.write(";")
        f.write(str(contribuidores.contributions))
        f.write("\n")

    f.close()

