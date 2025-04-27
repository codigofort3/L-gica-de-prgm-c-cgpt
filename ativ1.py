"""Objetivo: Peça ao usuário para digitar seu nome, idade e cidade
natal. Use uma f-string para formatar e exibir uma mensagem
com essas informações."""

# Solicitar nome do usuário
nome = input("Por favor digite o seu nome: ")

# Solicitar a idade do usuário e tranformoar em inteiro

idade = int(input("Por favor isira a sua idade: "))

# Solicitar a cidade natal do usuário
cidade_natal = input("Por favor insira a sua cidade natal: ")

#Formatar e exibir a mensagem com f-string
mensagem = f"Olá ,{nome}! Você tem {idade} anos e nasceu em {cidade_natal}."
print(mensagem)