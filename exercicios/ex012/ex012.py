val = float(input('Qual o preco do produto? R$'))
novo = - (val * 5 / 100)
print('O produto que custava R${:.2f}, na promocao com desconto de 5% vai custar R${:.2f}'.format(val, novo))
