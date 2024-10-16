# Operações
faturamento = 1000
custo = 700
novas_vendas = 300

faturamento = faturamento + novas_vendas # Adição
lucro = faturamento - custo # Subtração
imposto = faturamento * 0.1 # Multimplicação

print(faturamento)
print(lucro)

# Calcular a margem de lucro
margem_lucro = lucro / faturamento # Divisão
print(margem_lucro)

restituicao = imposto * 0.1
print(restituicao)

# Resto da Divisão
# para saber se um número é par ou ímpar
resto = 10 % 3

# Pegar somente a parte inteira de um número
parte_inteira = int(140 / 17)
print(parte_inteira)


# Arredondamento de um número
numero = 123.97
print(round(numero))

# Edição visual para facilitar a compreensão de números muito extensos
# por exemplo 139018182 - Fica difícil de saber qual o valor então pode usar o underline para separar
faturamento = 139_018_182
print(faturamento)

