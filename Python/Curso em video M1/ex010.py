print('==========EXERCICIO_010==========')

real=float(input('Digite quantos reais você tem: R$'))

cambio=float(input('Quanto tá o Valor do dolar em: R$'))

dolar=float(real/cambio)

print('==================================')

print('Consegue comprar com R${:0.2f} \ncom o cambio de R${:0.2f} por dolar \nsomente ${:0.2f}'.format(real,cambio,dolar))
