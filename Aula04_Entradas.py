# Entrada de dados pelo usuário através do teclado
nome =  input("Digite aqui o seu nome: ")
email = input("Digite aqui o seu e-mail: ")

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

