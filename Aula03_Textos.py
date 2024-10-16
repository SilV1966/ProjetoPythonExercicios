faturamento = 1000

custo = 700

lucro = faturamento - custo

# Valores dinâmicos utilizando a forma "f" para formatar a saída
print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email = "EMAIL_falso@gmail.com"

# Transformar texto em letra minúscula 
print(email.lower())

# Transformar texto em letra maiúscula
print(email.upper())

# Procurar algo dentro de um texto com o comando find retorna -1 se não encontrar
# se encontrar ele mostra a posição do elemento 
print(email.find("@"))

# Buscar qual o servidor do e-mail de um endereço de e-mail
posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)

# Buscar o nome do e-mail antes do @ ":" servie para indicar tudo até o final tanto pra frente quanto para trás
servidor = email[:posicao]
print(servidor)

# Retorna a quantidade de letras que tem a variável que contém o email
tamanho_email = len(email)
print(tamanho_email)

# Trocar uma informação pela outra com o Replace
troca_email = email.replace("gmail.com", "hotmail.com")
print(troca_email)

# Primeira letra do texto em maiúscula - Capitalize e todas as primeiras letras em maiúsculas Title
nome = "silmar vasconcelos"

print(nome.capitalize())
print(nome.title())

# Formatação numéricas especiais. Coloca 2 pontos após a variável e a formatação que vc quer
print(f"Faturamento: R$ {faturamento:,.2f}, Custo: {custo}, Lucro: {lucro}")

# Exibição de valores decimais utilizar % e a quantidade de casas decimais depois %1
margem = lucro / faturamento
print(f"Margem: {margem: .1%}")

# Salto de linha é o \n
print(f"Faturamento: R$ {faturamento: ,.2f}\n Custo: {custo}\n Lucro: {lucro}\n")

# Atividade - Criar duas variáveis nome e e-mail de uma pessoa
# 1o. - Imprima uma mensagem contendo o Primeito nome da pessoa e o email que foi cadastrado
nome = "Silmar Vasconcelos"
email = "silmar.vasconcelos@gmail.com"
posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

print(f"Prezado Sr. {primeiro_nome}\n o seu e-mail cadastrado foi: {email}")

# 2o. - Imprima uma mensagem - Enviamos um link de confirmação para o endereço de email ******
primeira_letra = email[0]
print(f"Enviamos um email de confirmação para o email {primeira_letra}***{servidor}")

