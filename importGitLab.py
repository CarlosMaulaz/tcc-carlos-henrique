import gitlab
import requests

###################################### Acesso ao GitLab ##############################################################

'''
# anonymous read-only access for public resources (GitLab.com)
gl = gitlab.Gitlab()

# anonymous read-only access for public resources (self-hosted GitLab instance)
gl = gitlab.Gitlab('https://gitlab.example.com')

# private token or personal token authentication (GitLab.com)
gl = gitlab.Gitlab(private_token='glpat-A6cWK7xiqmBHnyxrv3hK')
'''

# private token or personal token authentication (self-hosted GitLab instance)
gl = gitlab.Gitlab(private_token='glpat-xoqAg_ka95WfnnP7b3_N')
'''
# oauth token authentication
gl = gitlab.Gitlab('https://gitlab.example.com', oauth_token='my_long_token_here')

# job token authentication (to be used in CI)
# bear in mind the limitations of the API endpoints it supports:
# https://docs.gitlab.com/ee/ci/jobs/ci_job_token.html
import os
gl = gitlab.Gitlab('https://gitlab.example.com', job_token=os.environ['CI_JOB_TOKEN'])

# Define your own custom user agent for requests
gl = gitlab.Gitlab('https://gitlab.example.com', user_agent='my-package/1.0.0')
'''
# make an API request to create the gl.user object. This is not required but may be useful
# to validate your token authentication. Note that this will not work with job tokens.
gl.auth()

base_api_url = 'https://gitlab.com/api/v4/'
user_id1 = 'miikanissi'
user_id2 = 'carlosmaulaz'


response = requests.get(base_api_url + '/users/' + user_id2 + '/projects').json()

list_projects = []

for r in response:
    id = r['id']
    list_projects.append(id)
    print(id)


# class Projects:
#     def __init__(self, id, ):

#######################################################################################################################

