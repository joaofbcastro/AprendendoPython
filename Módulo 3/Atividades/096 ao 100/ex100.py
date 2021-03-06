"""
Exercício 100

Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint


numbers = []


def sorteia():
    for i in range(5):
        numbers.append(randint(0, 9))
    print('~'*50)
    print(f'Os valores sorteados foram: {numbers}')


def somapar():
    soma = 0
    for i in numbers:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos valores pares é {soma}')


sorteia()
somapar()
