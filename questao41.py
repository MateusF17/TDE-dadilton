def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc < 25:
        return "Saudável"
    elif 25 <= imc < 30:
        return "Peso em Excesso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"
    
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}")
