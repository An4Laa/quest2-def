# Exercício Python 02: Crie um programa que leia dois números e mostre a soma, a
# subtração, a multiplicação e a divisão entre eles.

num_1 = int(input("Insira um número inteiro: "))
num_2 = int(input("Insira outro número inteiro: "))

def soma(a, b):
    soma = a + b
    print(soma)

def subtracao(a, b):
    if a < b:
        subt_b = b - a
        print(subt_b)
    else:
        subt_a = a - b
        print(subt_a)

def divisao(a, b):
    if a < b:
        div_b = b / a
        print(div_b)
    else:
        div_a = a / b
        print(div_a)
        
def multiplicacao(a, b):
    multi = a * b
    print(multi)

soma (num_1, num_2)
subtracao (num_1, num_2)
divisao (num_1, num_2)
multiplicacao (num_1, num_2)