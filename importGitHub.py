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



# Procurar repositórios pesquisando pela linguagem de programação. Porque está listando diversos repositórios?

'''
repositories = g.search_repositories(query='language:python')
for repo in repositories:
    print(repo)
    
    
'''
#############################################################################
'''
repo = g.get_repo("CarlosMaulaz/tcc-carlos-henrique")
print(repo.get_topics())
print(repo.stargazers_count)
'''

# Listando todos os arquivos de um repositório
contents = repo.get_contents("")
for content_file in contents:
    print(content_file)

#Como pegar o usuário do commit? https://pygithub.readthedocs.io/en/latest/examples.html

#commit = repo.get_commit()

'''Entendendo as classes do GIT para aprender a pegar todos os commits de um repositório e listar os usuários do commit'''

print("")
print("")
print("Tipo do repositório: ",type(repo))
print(repo.clone_url)
print(repo.contributors_url)
print("")
print("")


'''O get Contribuidores está retornando uma PaginatedList. Como retirar o loguin dos contribuidores a partis dessa classe?

github.PaginatedList.PaginatedList of github.NamedUser.NamedUser -> O que isso significa?'''
contributors = repo.get_contributors()
print("Tentando extrair informações da lista de contribuidores")
print(type(contributors))
print(contributors)

# Definir função que pega todos os contribuidores de um projeto


