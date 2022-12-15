# primeiro contato com o Python comandos Basicos#

# Codigo Print#
print('Olá Mundo!')
nome = 'Alex'
print(nome)
# Posso usar aspas simples ou duplas para printa#

# VARIABLES

personagem_nome = 'Marcos'
pesonagem_idade = '19'
personagem_esporte = 'Futebol'
# aqui e manipulação de variaveis
print('Meu nome e ' + personagem_nome + ',')
print('eu tenho ' + pesonagem_idade + ' anos de idade.')
print('Meu esporte favorito e o ' + personagem_esporte)

# STRINGS

print('Wallace \n the Lion')  # O \n coloca toda continuação na segunda linha
# consigmos adicionar a aspas na string  usando a barra
print('Wallace \' the Lion')
# O +  e um operador logico usado para concatenar valores

# utilizamos o . para marcar uma função neste caso to tranfomando o valor em Maiusculo
print(personagem_esporte.upper())

valorNome = 'Alexandre Fernandes Pires'
print(valorNome[5])  # este e o vetor index ele sempre vai iniciar do 0
print(valorNome.index('xa'))  # aqui ele aponta onde começa o xa do vertor
print(len(valorNome))  # conta o tamanho maximo do campo
print(valorNome.count('a' or 'A'))  # quantos A existem


# Number

print(2)

print(-9)

print(2.04500)

# soma
print(2 + 8.2)

# multiplicação
print(2 * 8 + 3)  # para voce exigir a soma primeiro so colocar o parenteses antes


# Variaveis de String numeros

num1 = 5
num2 = 10
print(num1 + num2)
# convertemos para string o numero para poder converter-los
print(str(num1) + 'e meu numero da sorte')

# funções

print(min(2, 9))

print(max(2, 9))

print(pow(2, 9))  # Potencia 2 elevado a 9

# IMPUT
# capturar dados do usuário
nomeimp = input('Digite o seu nome: ')
idadeimp = input('Digite a sua idade: ')
print('Olá ' + nomeimp + '!' + 'Hoje Voce tem ' + idadeimp + ' anos de idade')

#
#
#
#
#
# LIST
amigos = ['Thiago', 'Moloise', 'Felipe', 'Richard', 'Cris']
print(amigos[3])
print(amigos[-4])  # Puxar a lista ao contrario
# encontrar os nomes da lista 1 até o 5 (O quinto não entra na lista)
print(amigos[1:5])
# Manipulando os intes dentro da lista sem precisar alterara
amigos[1] = 'Joao'
print(amigos)

# funcoes dentro da List
# ListFunctions

friends = ['Thiago', 'Moloise', 'Felipe', 'Richard', 'Cris']
numerosF = [3, 5, 4, 7, 9]
print(friends[0])  # ver quem esta na posição do index
# isso serve para colocar duas listas em um resultado so
friends.extend(numerosF)
friends.append('layon')  # colocar ele no final da fila
# Podemos escolher a posição do layon
friends.insert(3, 'layon')
# removendo o Moloise da lista
friends.removendo('Moloise')
# removendo atraves do index
friends.pop(1)  # dai remove o Moloise
# Verificar se existe o dado na lista
print(friends.index('Felipe'))
# Função Organizar a lista
friend.sort()
print(friends)
