#Feito por Guihhh
#13 de outubro de 2023
print('================Gerenciador_Salário====================')

salUser = float(input('Digite seu salário:R$'))

gastosEssenciais = float(salUser * 0.5)

gastosNaoEssenciais = float(salUser * 0.1)

investimentos = float(salUser * 0.3)

torrar = float(salUser * 0.1)

print('=======================================================')

print('Com o seu Salário de R${:0.2f}, \npara você fazer um bom aproveitamento deve \nseguir os valores abaixo:'.format(salUser))

print('=======================================================')

print('Gastos Essenciais - 50% (R${:0.2f})'.format(gastosEssenciais))

print('* Aluguel\n* Supermercado\n* Transporte\n* Seguro de Saúde\n* Plano de internet\n* e por aí vai...')

print('=======================================================')

print('Gastos NÃO Essenciais - 10% (R${:0.2f})'.format(gastosNaoEssenciais))

print('* Encomendar Comida\n* Roupas Novas\n* Entretenimento\n* E por aí vai...')

print('=======================================================')

print('Investimentos - 30% (R${:0.2f})'.format(investimentos))

print('* Reserva de Emergencia\n* Aplicação em ações\n* Fundos Imobiliarios\n* Renda Fixa\n* Ativos Internacionais\n* E por aí vai...')

print('=======================================================')

print('Torrar - 10% (R${:0.2f})'.format(torrar))

print('* Diversão\n* Compras\n* Lazer\n* E por aí vai...')

print('=======================================================')