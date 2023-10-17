altura = float(input("Digite a sua altura (coloque o ponto quando for colocar os centímetros): "))
peso = float(input("Digite o seu peso: "))

if altura < 1.20:
    print("Você tem nanismo?")
    if peso <= 60:
        print("Usuário é da classe A")
    elif peso > 60 and peso <= 90:
        print("Usuário é da classe D")
    else:
        print("Usuário é da classe G")

elif altura > 1.20 and altura <= 1.70:
    if peso <= 60:
        print("Usuário é da classe B")
    elif peso > 60 and peso <= 90:
        print("Usuário é da classe E")
    else:
        print("Usuário é da classe H")
    
else:
    if peso <= 60:
        print("Usuário é da classe C")
    elif peso > 60 and peso <= 90:
        print("Usuário é da classe F")
    else:
        print("Usuário é da classe I")

