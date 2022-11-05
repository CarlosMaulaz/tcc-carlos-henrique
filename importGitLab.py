import gitlab
import requests

# ##################################### Acesso ao GitLab ##############################################################

# private token or personal token authentication (self-hosted GitLab instance)
gl = gitlab.Gitlab(private_token='glpat-xoqAg_ka95WfnnP7b3_N')

gl.auth()

# #####################################################################################################################

base_api_url = 'https://gitlab.com/api/v4/'
user_id1 = 'miikanissi'
user_id2 = 'carlosmaulaz'
project_ch = 'Carlos Henrique Maulaz de Freitas / tcc-carlos-henrique'


# ############################################# Classes ###############################################################

class Commit:
    def __init__(self, project_id, commit_id, author_name, author_email, author_date, commiter_name, commiter_email, commiter_date, tree_sha):
        self.project_id = project_id
        self.sha = sha
        self.author_name = author_name
        self.author_email = author_email
        self.author_date = author_date
        self.commiter_name = commiter_name
        self.commiter_email = commiter_email
        self.commiter_date = commiter_date
        self.tree_sha = tree_sha

response = requests.get(base_api_url + '/users/' + user_id2 + '/projects').json()

list_projects = []

#print(response)

for r in response:
    id = r['id']
    list_projects.append(id)
    print(id)


def get_commits(project_id):
    response = requests.get(base_api_url + '/projects/' + str(project_id) + '/repository/commits').json()
    print(response)

# class Projects:
#     def __init__(self, id, ):

#######################################################################################################################
# /projects/:id/repository/commits

get_commits(40743609)