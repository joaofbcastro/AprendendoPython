# Aluguel de Carro
print('-' * 25)
print('Bem vindo(a) Moovida.')
print('-' * 25)
dias = int(input('Quantos dias você ficou com o carro? '))
kms = float(input('Quantos km você percorreu com o carro? '))
custo = (kms * 0.15) + (dias * 60.0)
print('-' * 25)
print('Custo do aluguel: R${:.2f}'.format(custo))
print('-' * 25)
