print('==========EXERCICIO_012==========')

valprod = float(input('Digite o valor do produto:'))

descinf = int(input('Digite o Desconto:'))

descreal = descinf/100

valfinal = valprod - (valprod * descreal)

print('Valor sem Desconto:R${:0.2f} \nValor com Desconto:R${:0.2f}\nDesconto Aplicado:{}%'.format(valprod,valfinal,descinf))