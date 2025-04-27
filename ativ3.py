"""Objetivo: Criar um Programa que Peça as 4 Notas
Bimestrais e Mostre a Média

Instruções:

1 - Solicitar as Notas do Usuário:
Use a função input() para pedir ao usuário que insira
cada uma das quatro notas bimestrais. Converta a
entrada do usuário de string para um número (float)
para permitir cálculos.

2 - Calcular a Média das Notas:
Some as quatro notas e divida o resultado
por quatro para obter a média.

3 - Mostrar a Média Calculada para o Usuário:
Use a função print() para exibir a média das notas
calculada."""

# Solicitar as quatro notas bimestrais e converter para float
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))

# Calcular a média das notas
media = (nota1 + nota2 + nota3 + nota4 / 4)

# Exibir a média calculada
print(f"Sua média bimestral é: {media:.2f}")