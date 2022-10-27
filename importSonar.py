import requests
import json
import pathlib
import os
from sonarqube import SonarCloudClient

sonar = SonarCloudClient(sonarcloud_url="https://sonarcloud.io", token='1bda9a037facea77fc3cd5e6e0e6ff05acded5cf')


class Issue:
    def __init__(self, key, rule, severity, component, project, hash, status, effort, debt, creation_date, update_date, type, resolution, close_date, assignee):
        self.key = key
        self.rule = rule
        self.severity = severity
        self.component = component
        self.project = project
        self.hash = hash
        self.status = status
        self.effort = effort
        self.debt = debt
        self.creation_date = creation_date
        self.update_date = update_date
        self.type = type
        self.resolution = resolution
        self.close_date = close_date
        self.assignee = assignee


class Components:
    def __init__(self, organization, key, uuid, name, long_name, path):
        self.organization = organization
        self.key = key
        self.uuid = uuid
        self.name = name
        self.long_name = long_name
        self.path = path


class Rules:
    def __init__(self, key, name, lang, lang_name):
        self.key = key
        self.name = name
        self.lang = lang
        self. lang_name = lang_name


class User:
    def __init__(self, login, name, active):
        self.login = login
        self.name = name
        self.active = active


def get_project_issues(project_id):
    issue_list = []
    url = 'https://sonarcloud.io/api/issues/search'

    for x in range(1,3):
        query = {'additionalFields': '_all', 'componentKeys': project_id, 'p':x, 'ps': 500}
        r = requests.get(url, params=query)
        issues_json = r.json()
        with open(os.path.join(pathlib.Path().resolve(), 'files\\data'+ str(x) +'.json'), 'w') as f:
            json.dump(issues_json, f)
        print(issues_json)
        for issues in issues_json['issues']:
            key = issues['key']
            rule = issues['rule']
            severity = issues['severity']
            component = issues['component']
            project = issues['project']
            hash = issues['hash']
            status = issues['status']
            effort = issues['effort']
            debt = issues['debt']
            creation_date = issues['creationDate']
            update_date = issues['updateDate']
            type = issues['type']
            try:
                resolution = issues['resolution']
            except KeyError:
                resolution = ""
            try:
                close_date = issues['closeDate']
            except KeyError:
                close_date = ""
            try:
                assignee = issues['assignee']
            except KeyError:
                assignee = ""

            issue_list.append(Issue(key, rule, severity, component, project, hash, status, effort, debt, creation_date, update_date, type, resolution, close_date, assignee))

    return issue_list


def get_project_components(project_id):
    component_list = []
    url = 'https://sonarcloud.io/api/issues/search'

    for x in range(1,3):
        query = {'additionalFields': '_all', 'componentKeys': project_id, 'p':x, 'ps': 500}
        r = requests.get(url, params=query)
        issues_json = r.json()
        for components in issues_json['components']:
            organization = components['organization']
            key = components['key']
            uuid = components['uuid']
            name = components['name']
            long_name = components['longName']
            try:
                path = components['path']
            except KeyError:
                path = ""

            component_list.append(Components(organization, key, uuid, name, long_name, path))

    return component_list


def get_project_rules(project_id):
    rules_list = []
    url = 'https://sonarcloud.io/api/issues/search'

    for x in range(1, 3):
        query = {'additionalFields': '_all', 'componentKeys': project_id, 'p': x, 'ps': 500}
        r = requests.get(url, params=query)
        issues_json = r.json()
        for rules in issues_json['rules']:

            key = rules['key']
            name = rules['name']
            lang = rules['lang']
            lang_name = rules['langName']
            rules_list.append(Rules(key, name, lang, lang_name))

    return rules_list

def get_project_users(project_id):
    users_list = []
    url = 'https://sonarcloud.io/api/issues/search'

    for x in range(1, 3):

        query = {'additionalFields': '_all', 'componentKeys': project_id, 'p': x, 'ps': 500}
        r = requests.get(url, params=query)
        issues_json = r.json()

        for users in issues_json['users']:

            login = users['login']
            name = users['name']
            active = users['active']

            users_list.append(User(login, name, active))

    return users_list



def save_csv_issue_list(issue_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\issue_list.csv"), "w")
    f.write("key")
    f.write(";")
    f.write("rule")
    f.write(";")
    f.write("severity")
    f.write(";")
    f.write("component")
    f.write(";")
    f.write("project")
    f.write(";")
    f.write("hash")
    f.write(";")
    f.write("status")
    f.write(";")
    f.write("effort")
    f.write(";")
    f.write("debt")
    f.write(";")
    f.write("creation_date")
    f.write(";")
    f.write("update_date")
    f.write(";")
    f.write("close_date")
    f.write(";")
    f.write("type")
    f.write(";")
    f.write("resolution")
    f.write(";")
    f.write("assignee")
    f.write("\n")
    for issue in issue_list:
        f.write(issue.key)
        f.write(";")
        f.write(issue.rule)
        f.write(";")
        f.write(issue.severity)
        f.write(";")
        f.write(issue.component)
        f.write(";")
        f.write(issue.project)
        f.write(";")
        f.write(issue.hash)
        f.write(";")
        f.write(issue.status)
        f.write(";")
        f.write(issue.effort)
        f.write(";")
        f.write(issue.debt)
        f.write(";")
        f.write(issue.creation_date)
        f.write(";")
        f.write(issue.update_date)
        f.write(";")
        f.write(issue.close_date)
        f.write(";")
        f.write(issue.type)
        f.write(";")
        f.write(issue.resolution)
        f.write(";")
        f.write(issue.assignee)
        f.write("\n")
    f.close()


def save_csv_component_list(component_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\component_list.csv"), "w")
    f.write("organization")
    f.write(";")
    f.write("key")
    f.write(";")
    f.write("uuid")
    f.write(";")
    f.write("name")
    f.write(";")
    f.write("long_name")
    f.write(";")
    f.write("path")
    f.write("\n")
    for component in component_list:
        f.write(component.organization)
        f.write(";")
        f.write(component.key)
        f.write(";")
        f.write(component.uuid)
        f.write(";")
        f.write(component.name)
        f.write(";")
        f.write(component.long_name)
        f.write(";")
        f.write(component.path)
        f.write("\n")
    f.close()


def save_csv_rules_list(rules_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\rules_list.csv"), "w")
    f.write("key")
    f.write(";")
    f.write("name")
    f.write(";")
    f.write("lang")
    f.write(";")
    f.write("langName")
    f.write("\n")
    for rule in rules_list:
        f.write(rule.key)
        f.write(";")
        f.write(rule.name)
        f.write(";")
        f.write(rule.lang)
        f.write(";")
        f.write(rule.lang_name)
        f.write("\n")
    f.close()


def save_csv_users_list(users_list):
    f = open(os.path.join(pathlib.Path().resolve(), "files\\users_list.csv"), "w")
    f.write("login")
    f.write(";")
    f.write("name")
    f.write(";")
    f.write("active")
    f.write("\n")
    for user in users_list:
        f.write(user.login)
        f.write(";")
        f.write(user.name)
        f.write(";")
        f.write(str(user.active))
        f.write("\n")
    f.close()

def get_issues_changelog(issue_list):
    url = 'https://sonarcloud.io/api/issues/changelog'
    for issue in issue_list:
        print(issue.key)
        query = {'issue': issue.key}
        r = requests.get(url, params=query)
        issue_changelog = r.json()
        print(issue_changelog)


def get_issue_authors(project_id):
    url = 'https://sonarcloud.io/api/issues/authors'
    for x in range(1,3):
        query = {'additionalFields': '_all', 'componentKeys': project_id, 'p':x, 'ps': 500}
        r = requests.get(url, params=query)
        issues_json = r.json()
        print(issues_json)