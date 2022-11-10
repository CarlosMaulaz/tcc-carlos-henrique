import gitlab
import requests
import os
import pathlib

# ##################################### Acesso ao GitLab ##############################################################

# private token or personal token authentication (self-hosted GitLab instance)
gl = gitlab.Gitlab(private_token='glpat-Kabfc97Pa8sxzzhESsd1')

# private token or personal token authentication (self-hosted GitLab instance)
# gl = gitlab.Gitlab(url='https://gitlab.example.com', private_token='glpat-Kabfc97Pa8sxzzhESsd1')


# oauth token authentication
# gl = gitlab.Gitlab('https://gitlab.example.com', oauth_token='my_long_token_here')

gl.auth()

base_api_url = 'https://gitlab.com/api/v4'
project_ch = 'Carlos Henrique Maulaz de Freitas / tcc-carlos-henrique'


class Project:
    def __init__(self, project_id, project_name, project_name_with_name_space, project_path,
                 project_path_with_name_space):
        self.project_id = project_id
        self.project_name = project_name
        self.project_name_with_name_space = project_name_with_name_space
        self.project_path = project_path
        self.project_path_with_name_space = project_path_with_name_space


class Commit:
    def __init__(self, project_id, commit_id, created_at, author_name,
                 author_email, authored_date, committer_name, committer_email, committed_date):
        self.project_id = project_id
        self.commit_id = commit_id
        self.created_at = created_at
        self.author_name = author_name
        self.author_email = author_email
        self.authored_date = authored_date
        self.committer_name = committer_name
        self.committer_email = committer_email
        self.committed_date = committed_date


class CommitDiff:
    def __init__(self, project_id, commit_id, new_path, old_path, new_file, renamed_file, deleted_file):
        self.project_id = project_id
        self.commit_id = commit_id
        self.new_path = new_path
        self.old_path = old_path
        self.new_file = new_file
        self.renamed_file = renamed_file
        self.deleted_file = deleted_file


def get_projects(list_projects_id):
    list_projects = []
    for project_id in list_projects_id:
        response = requests.get(base_api_url + '/projects/' + str(project_id)).json()
        p_id = response['id']
        project_name = response['name']
        project_name_with_name_space = response['name_with_namespace']
        project_path = response['path']
        project_path_with_name_space = response['path_with_namespace']
        list_projects.append(Project(p_id, project_name, project_name_with_name_space, project_path,
                                     project_path_with_name_space))
    return list_projects


def get_commits(list_projects):
    list_commits = []
    for project in list_projects:
        response = requests.get(base_api_url + '/projects/' + str(project.project_id) + '/repository/commits').json()
        for r in response:
            project_id = project.project_id
            commit_id = r['id']
            created_at = r['created_at']
            author_name = r['author_name']
            author_email = r['author_email']
            authored_date = r['authored_date']
            committer_name = r['committer_name']
            committer_email = r['committer_email']
            committed_date = r['committed_date']
            list_commits.append(Commit(project_id, commit_id, created_at, author_name, author_email,
                                       authored_date, committer_name, committer_email, committed_date))

    return list_commits


def get_commit_diff(list_commits_obj):
    list_commits_diff = []
    for commit in list_commits_obj:
        response = requests.get(base_api_url + '/projects/' + str(commit.project_id) + '/repository/commits/' +
                                str(commit.commit_id) + '/diff').json()

        for r in response:
            project_id = commit.project_id
            commit_id = commit.commit_id
            new_path = r['new_path']
            old_path = r['old_path']
            new_file = r['new_file']
            renamed_file = r['renamed_file']
            deleted_file = r['deleted_file']
            list_commits_diff.append(CommitDiff(project_id, commit_id, new_path, old_path, new_file,
                                                renamed_file, deleted_file))

    return list_commits_diff


# def get_users(list_commits_obj):
#     list_users = []
#     list_users_email = []
#     for commit in list_commits_obj:
#         if commit.author_email not in list_users_email:
#             list_users_email.append(commit.author_email)
#             response = requests.get(/users?search=carlosmaulaz@gmail.com).json



def save_csv_project_list(list_projects):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\gitlab_project_list.csv"), "w")
    f.write("id")
    f.write(";")
    f.write("name")
    f.write(";")
    f.write("name_with_name_space")
    f.write(";")
    f.write("path")
    f.write(";")
    f.write("path_with_name_space")
    f.write("\n")

    for proj in list_projects:
        f.write(str(proj.project_id))
        f.write(";")
        f.write(proj.project_name)
        f.write(";")
        f.write(proj.project_name_with_name_space)
        f.write(";")
        f.write(proj.project_path)
        f.write(";")
        f.write(proj.project_path_with_name_space)
        f.write("\n")
    f.close()


def save_csv_commit_list(gitlab_commit_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\gitlab_commit_list.csv"), "w")
    f.write("project_id")
    f.write(";")
    f.write("commit_id")
    f.write(";")
    f.write("created_at")
    f.write(";")
    f.write("author_name")
    f.write(";")
    f.write("author_email")
    f.write(";")
    f.write("authored_date")
    f.write(";")
    f.write("committer_name")
    f.write(";")
    f.write("commiter_email")
    f.write(";")
    f.write("committed_date")
    f.write("\n")

    for commit in gitlab_commit_list:
        f.write(str(commit.project_id))
        f.write(";")
        f.write(commit.commit_id)
        f.write(";")
        f.write(commit.created_at)
        f.write(";")
        f.write(commit.author_name)
        f.write(";")
        f.write(commit.author_email)
        f.write(";")
        f.write(commit.authored_date)
        f.write(";")
        f.write(commit.committer_name)
        f.write(";")
        f.write(commit.committer_email)
        f.write(";")
        f.write(commit.committed_date)
        f.write("\n")
    f.close()


def save_csv_commit_diff_list(gitlab_commit_diff_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\gitlab_commit_diff_list.csv"), "w")
    f.write("project_id" + ";")
    f.write("commit_id")
    f.write(";")
    f.write("new_path")
    f.write(";")
    f.write("old_path")
    f.write(";")
    f.write("new_file")
    f.write(";")
    f.write("renamed_file")
    f.write(";")
    f.write("deleted_file")
    f.write("\n")

    for commit_diff in gitlab_commit_diff_list:
        f.write(str(commit_diff.project_id))
        f.write(";")
        f.write(commit_diff.commit_id)
        f.write(";")
        f.write(commit_diff.new_path)
        f.write(";")
        f.write(commit_diff.old_path)
        f.write(";")
        f.write(str(commit_diff.new_file))
        f.write(";")
        f.write(str(commit_diff.renamed_file))
        f.write(";")
        f.write(str(commit_diff.deleted_file))
        f.write("\n")
    f.close()


# Teste para acesso aos dados de usuários
print(base_api_url + '/projects/' + '21803695' + '/members')
response = requests.get(base_api_url + '/projects/' + '21803695' + '/members').json()
print(response)