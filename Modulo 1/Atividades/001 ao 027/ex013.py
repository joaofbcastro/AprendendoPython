# Mostrar aumento do jaiminho
print('-------------------------')
print('Bem vindo ao EMPRESA Sistem')
print('-------------------------')
name = input('Digite o seu nome: ')
salario = float(input('Qual é o valor do seu salário atual? R$'))
print('-------------------------')
print('{}, temos um aumento para você.'.format(name))
print('------------------------')
print('Salário atual: R${:.2f}'.format(salario))
print('Novo salário: R${:.2f}'.format(salario+salario*0.15))
print('------------------------')
print('Aumento no salário de R${:.2f}'.format(salario*0.15))
print('--------------------------------------------------')
print('Obrigado por seu trabalho, colaboração e dedicação.')
print('--------------------------------------------------')
