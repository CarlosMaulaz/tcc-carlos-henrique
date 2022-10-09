print("Olá mundo, tô ma área!!!")

# Aprendendo comentários, para comentar basta iniciar a linha com hashtag

'''
Para comentários que vão além de uma linha é necesário abrir 3 áspas
'''

# No python utiliza-se a identação para que a linguagem indentifique um bloco. Conforme o exemplo a seguir:

if 5>3:
    print("5 é maior que 3")

'''
No python as variáveis não precisam ser declaradas, elas já são definidas no momento que um valor é asssociado a ela.
Elas podem mudar o tipo assim que outra variável é associada a ela.
'''

x = 10
y = "Carlos Henrique"

print(x)
print(y)

# a variável x é de um tipo int

x = "de int, x virou str"
print(x)

# Se desejar especificar o tipo de uma variável, deverá utilizar o casting
# Vamos definir variáveis do tipo string, int e float

a = str(3)
b = int(3)
c = float(3)

print(a)
print(b)
print(c)

# Para saber o tipo que a variável se encontra basta utilizar a função type

print(type(a))
print(type(b))
print(type(c))

# Strings podem ser declaradas tanto com aspas simples '' quanto por aspas duplas

x = 'String definida com aspas simples'
print(x)
print(type(x))
x = "String definida com aspas duplas"
print(x)
print(type(x))

# O nome das variáveis são case sensitive
# Então se for escrita em caixa alta não será a mesma escrita em caixa baixa. (KKK sei lá se é caixa baixa que se fala)

a = 4
A = "Carlos Henrique"
print(a)

# A variável 'A' não substituiu a variável a

'''
Algumas definições para nomes de variáveis em python:
    -> Um nome de variável deverá começar com letras ou com um sublinhado (underline, underscore)
    -> Um nome de variável não pode começar com número
    -> Um nome de variável pode apenas conter caracteres alfanuméricos
    -> O nome das variáveis são case-sensitive (uma variável 'nome' é diferente de 'Nome')
    
    Legal variable names:
        myvar = "John"
        my_var = "John"
        _my_var = "John"
        myVar = "John"
        MYVAR = "John"
        myvar2 = "John"
    
    Illegal variable names:

        2myvar = "John"
        my-var = "John"
        my var = "John"
'''

#No python você pode assimilar valores a várias variáveis em uma mesma linha como no exemplo a seguir:

x, y, z = "Carlos", "Yasmim", "Sebastião"

print(x)
print(y)
print(z)

# Se o número de variáveis não for o mesmo número de valores dará erro na linha

#Mesmo valor para múltiplas variáveis

x = y = z = "Carlos"

print(x)
print(y)
print(z)

'''
Se você tem, uma coleção de valores (tipo listas, tuplas, etc), o python te dá a liberdade de extraílas. Isso é chamado 
de Unpacking
'''

frutas = ["banana", "maça", "uva"]
x,y,z = frutas
print(x)
print(y)
print(z)

'''
Saída de variáveis.

Utilizamos a função print(), com frequêcia, para dar a saída das variáveis.  
A seguida algumas formas de utilziar a função print. Ela pode ser utilizada para múltiplas variáveis utilizando virgula 
para separar.
Ou contatenando variáveis utilizando '+' para contatenar as variáveis.

'''

print(z)
print(x,y,z)
print(x+ " " + y + " " + z)

# note que o operador '+' funicona como concatenador para Strings mas para números ele se comporta como um operador
# de soma

x = "Irá "
y = "concatenar"
print(x+y)

x = 5
y = 2
print(x+y, "resultado da soma de x + y")

# VARIÁVEIS GLOBAIS

'''
As variáveis globais são definidas fora das funções. Elas podem ser utilizadas tanto dentro ou fora das funções.
Já as variáveis de funções só existirão dentro delas.
'''

x = "awesome"

def myfunc():
    x = 'fantastic'
    print ("Python is " + x)

myfunc()

print ("Python is " + x)

# para se criar variáveis globais dentro de uma função, utilizamos a key word 'global'

def myfunc():
    global x
    x = 'fantastic'

myfunc()

print ("Python is " + x)

#Estudandos os tipos, a seguir irei explorar alguns que não conheço muito bem dentro do python

x= range(6)
print(x)
x = ["biscoito","bolacha","salgadinho"]
print(x)
x = ("crisântemo","jibóia","Comigo ninguém pode")
print(x)

x = frozenset({"apple", "banana", "cherry"})
print(x)

#Python Numbers

x = 31e2
print(x)

x = 2 + 2j
print(x)

#Convertendo os tipos das variáveis Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

a = "Hello, World"

print(a[0])

for x in "banana":
  print(x)

txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
print(b[2:5])