from github import Github

# First create a Github instance:

# using an access token
g = Github("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")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
    print(repo)

user = g.get_user()
print(user)




