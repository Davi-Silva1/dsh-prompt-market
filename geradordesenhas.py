chave = input("Digite a base da sua senha: ")

senha = ""

for letra in chave:
    if letra in "Aa": senha += "1"
    elif letra in "Bb": senha += "@"
    elif letra in "Cc": senha += "2"
    elif letra in "Dd": senha += "3"
    elif letra in "Ee": senha += "4"
    elif letra in "Ff": senha += "5"
    elif letra in "Rr": senha += "#"
    elif letra in "Ss": senha += "%"
    elif letra in "Mm" : senha += "$"
    elif letra in "Jj" : senha += "_"
    else: senha = senha + letra
print(senha)