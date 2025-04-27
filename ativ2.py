"""Solicitar o Salário Mensal:
Use a função input() para pedir ao usuário que insira quanto
ele ganha por mês. Converta a entrada do usuário de string
para um número (float) para permitir cálculos.

2 - Solicitar o Número de Horas Trabalhadas na Semana:
Use a função input() para pedir ao usuário que insira o número
de horas trabalhadas na semana. Converta a entrada do
usuário de string para um número (float) para permitir
cálculos.

3 - Calcular o Total de Horas Trabalhadas no Mês:
Multiplique o número de horas trabalhadas na semana por 4
para obter o total de horas trabalhadas no mês.
Objetivo: Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês, calcule o salário total e exiba o resultado (Considere que você trabalha
20 dias no mês).

4 - Calcular o Salário por Hora:
Divida o salário mensal pelo total de horas
trabalhadas no mês para obter o salário por
hora.

5 - Mostrar o Salário por Hora Calculado
para o Usuário:
Use a função print() para exibir o salário por
hora calculado."""

#Solicitar oi salário mensal do usuário e converter em float
salario_mensal = float(input("Quanto você ganha por mês?: "))

## Solicitar o número de horas trabalhadas por semana e converter para float

horas_por_semana = float(input("Quantas horas você trabalha por semana?: "))

# Calcula o tatal de horas trabalhadas no mês considerando 4 semanas
horas_por_mes = horas_por_semana * 4

#calcular o salário por hora
salario_por_hora = salario_mensal / horas_por_mes

# Exibir o salário por hora calculado
print(f"Seu salário por hora é R$ {salario_por_hora:.2f}")

