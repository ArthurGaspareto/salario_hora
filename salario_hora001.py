'''
Programa: Soma
Descrição: calcule o sal´ario de um professor horista na Universidade XYZ. O programa deve perguntar o n´umero de horas trabalhadas, calcular e imprimir na tela o valor do sal´ario bruto,
do sal´ario l´ıquido e do total de descontos, sabendo que o desconto do imposto ´e 30% e
que o valor da hora-aula ´e R$ 40,00.
Autor: Arthur Gaspareto
Data: 25/02/25
Versão: 0.0.1
Novidades da Versão

25/02/2025
Nesta versão:
1.
'''

#Alocação de Memória
horas = float()
salario_bruto = float()
salario_liquido = float()
impostos = 0.3
descontos = 0
valor_hr = 40

#Entrada de Dados

horas = float(input('Quantas horas trabalhadas?'))

#Processamento de Dados
salario_bruto = valor_hr * horas
descontos = salario_bruto*impostos
salario_liquido = salario_bruto - descontos

#Saída de dados

print(f'O Salário Bruto é: {salario_bruto}.\nO Salário Liquido é: {salario_liquido}.\nO total de desconstos foi: {descontos}.')