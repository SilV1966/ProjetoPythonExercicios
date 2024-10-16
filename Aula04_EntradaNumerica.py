# Pedir o usuário para inserir um valor para calcular 1% de bonus sobre as venda
#vendas = input("Digite as vendas do dia: ")
#bonus = vendas * 0.01
#print(bonus)
# Erro pq está multiplicando um valor string 


# Converter a variável vendas para tipo Real ou Decimal com casas decimais
vendas = input("Digite as vendas do dia: ")
vendas = float(vendas)
bonus = vendas * 0.01
print(bonus)