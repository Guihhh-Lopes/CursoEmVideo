('==========EXERCICIO_014===============')

da = int ( input('Digite quantos dias o veiculo foi alugado: '))

km = int ( input('Digite quantos Km rodados: ') )

ppda = float(da * 60)

ppkm = float(km * 0.15)

total = ppda + ppkm

print('O total a pagar é de R${:0.2f}'.format(total))
