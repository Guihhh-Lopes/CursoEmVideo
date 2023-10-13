print('==========EXERCICIO_013===============')

sal = float(input('Digite seu salário atual: R$'))

aum = int(input('Digite quantos por cento de aumento:'))

vlaum = sal*(aum/100)

nsal = sal+vlaum

print('======================================')

print('Salário antigo:R${:0.2f} \nAumento de:{}% \nSalário Novo:R${:0.2f} \nAumentou:R${:0.2f}'.format(sal,aum,nsal,
vlaum))
print('======================================')