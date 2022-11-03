import requests
import pathlib
import os
from github import Github

# Token de acesso para autenticação de acesso à API
g = Github("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")
github_api_url = 'https://api.github.com'




'''

Classes 

'''

class User:
    def __init__(self, login, id):
        self.login = login
        self.id = id


class Repository:
    def __init__(self, id, name, full_name, owner_id, owner_login):
        self.id = id
        self.name = name
        self.full_name = full_name
        self.owner_id = owner_id
        self.owner_login = owner_login


class Contributor:
    def __init__(self, repos_id, id, login, contributions):
        self.repos_id = repos_id
        self.id = id
        self.login = login
        self.contributions = contributions

class Commit:
    def __init__(self, repos_id, sha, author_name, author_email, author_date, commiter_name, commiter_email, commiter_date, tree_sha):
        self.repos_id = repos_id
        self.sha = sha
        self.author_name = author_name
        self.author_email = author_email
        self.author_date = author_date
        self.commiter_name = commiter_name
        self.commiter_email = commiter_email
        self.commiter_date = commiter_date
        self.tree_sha = tree_sha

class Files:
    def __init__(self, tree_sha, name):
        self.tree_sha = tree_sha
        self.name = name

'''

Funções para a extração de dados

'''

def save_csv_contributors_list(contributors_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\contributors_list.csv"), "w")
    f.write("repos_id")
    f.write(";")
    f.write("id")
    f.write(";")
    f.write("login")
    f.write(";")
    f.write("contribuicao")
    f.write("\n")

    for contributor in contributors_list:
        f.write(str(contributor.repos_id))
        f.write(";")
        f.write(str(contributor.id))
        f.write(";")
        f.write(contributor.login)
        f.write(";")
        f.write(str(contributor.contributions))
        f.write("\n")

    f.close()

def save_csv_repository_list(repository_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\repository_list.csv"), "w")
    f.write("id")
    f.write(";")
    f.write("name")
    f.write(";")
    f.write("full_name")
    f.write(";")
    f.write("owner_id")
    f.write(";")
    f.write("owner_login")
    f.write("\n")

    for repository in repository_list:
        f.write(str(repository.id))
        f.write(";")
        f.write(repository.name)
        f.write(";")
        f.write(repository.full_name)
        f.write(";")
        f.write(str(repository.owner_id))
        f.write(";")
        f.write(repository.owner_login)
        f.write("\n")

    f.close()

def save_csv_commit_list(commit_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\commit_list.csv"), "w")
    f.write("repos_id")
    f.write(";")
    f.write("sha")
    f.write(";")
    f.write("author_name")
    f.write(";")
    f.write("author_email")
    f.write(";")
    f.write("author_date")
    f.write(";")
    f.write("commiter_name")
    f.write(";")
    f.write("commiter_email")
    f.write(";")
    f.write("commiter_date")
    f.write(";")
    f.write("tree_sha")
    f.write(";")
    f.write("\n")

    for commit in commit_list:
        f.write(str(commit.repos_id))
        f.write(";")
        f.write(commit.sha)
        f.write(";")
        f.write(commit.author_name)
        f.write(";")
        f.write(commit.author_email)
        f.write(";")
        f.write(commit.author_date)
        f.write(";")
        f.write(commit.commiter_name)
        f.write(";")
        f.write(commit.commiter_email)
        f.write(";")
        f.write(commit.commiter_date)
        f.write(";")
        f.write(commit.tree_sha)
        f.write(";")
        f.write("\n")

    f.close()

def save_csv_file_list(file_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\file_list.csv"), "w")
    f.write("commit_tree_sha")
    f.write(";")
    f.write("name")
    f.write("\n")

    for file in file_list:
        f.write(file.tree_sha)
        f.write(";")
        f.write(file.name)
        f.write("\n")

    f.close()
def get_user(user_name):
    r = requests.get(github_api_url + '/users'+ '/' + user_name).json()
    login = r['login']
    id = r['id']
    usuario = User(login, id)
    return usuario

def get_repos (user_name):
    repos_list = []
    response = requests.get(github_api_url + '/users' + '/' + user_name + '/repos').json()
    for r in response:
        id = r['id']
        name = r['name']
        full_name = r['full_name']
        owner_login = r['owner']['login']
        owner_id = r['owner']['id']
        repos_list.append(Repository(id, name, full_name, owner_id, owner_login))
    return repos_list

def get_contributors (repos_list):
    contributors_list = []
    for repos in repos_list:
        response = requests.get(github_api_url + '/repos' + '/' + repos.full_name).json()
        repos_id = response['id']
        response = requests.get(github_api_url + '/repos' + '/' + repos.full_name + '/contributors').json()
        for r in response:
            id = r['id']
            login = r['login']
            contributions = r['contributions']
            contributors_list.append(Contributor(repos_id, id, login, contributions))
    return contributors_list

def get_commit (repos_list):
    commit_list = []
    for repos in repos_list:
        response = requests.get(github_api_url + '/repos' + '/' + repos.full_name).json()
        repos_id = response['id']
        response = requests.get(github_api_url + '/repos' + '/' + repos.full_name + '/commits').json()
        for r in response:
            sha = r['sha']
            author_name = r['commit']['author']['name']
            author_email = r['commit']['author']['email']
            author_date = r['commit']['author']['date']
            commiter_name = r['commit']['committer']['name']
            commiter_email = r['commit']['committer']['email']
            commiter_date = r['commit']['committer']['date']
            tree_sha = r['commit']['tree']['sha']
            commit_list.append(Commit(repos_id, sha, author_name, author_email, author_date, commiter_name, commiter_email, commiter_date, tree_sha))

    return commit_list

def get_commit_files (commit_list):
    for commit in commit_list:
        files_list = []
        repos_full_name = g.get_repo(commit.repos_id).full_name
        response = requests.get(github_api_url + '/repos' + '/' + repos_full_name + '/git/trees/' + commit.tree_sha).json()
        for r in response['tree']:
            print(r['type'])
            tipo = r['type']
            print(type(tipo))
            if tipo == "blob":
                name = r['path']
                tree_sha = commit.tree_sha
                files_list.append(Files(tree_sha, name))

            if tipo == "tree":
                get_tree_files(commit.tree_sha, response['url'])

    return files_list



def get_tree_files (commit_tree_sha, tree_url):
    files_list = []
    response = requests.get(tree_url).json()
    for r in response['tree']:
        tipo = r['type']
        if tipo == "blob":
            name = r['path']
            files_list.append(Files(commit_tree_sha, name))

        if tipo == "tree":
            files_list.append(get_tree_files(commit_tree_sha, response['url']))
    return files_list



repositorios = get_repos('CarlosMaulaz')
contribuidores = get_contributors(repositorios)
# repositorios = [repositorios[0], repositorios[1]]
commits = get_commit(repositorios)
files_do_commit = get_commit_files(commits)

save_csv_repository_list(repositorios)
save_csv_contributors_list(contribuidores)
save_csv_commit_list(commits)
save_csv_file_list(files_do_commit)