operacao = int(input("Digite o número equivalente à operação.\n[1]-Soma dos dois números\n[2]-Diferença dos dois números\n[3]-Produto entre dois números\n[4]-Divisão entre dois números (o denominador não pode ser zero): "))

while operacao < 1 or operacao > 4:
    print("Operação inválida, tente novamente.")
    operacao = int(input("Digite o número equivalente à operação.\n[1]-Soma dos dois números\n[2]-Diferença dos dois números\n[3]-Produto entre dois números\n[4]-Divisão entre dois números (o denominador não pode ser zero): "))

if operacao == 1:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"A soma dos números é {soma}")
    
elif operacao == 2:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite o segundo número: "))
    
    if num1 > num2:
        diferenca = num1 - num2
        print(f"A diferença dos números é {diferenca}")
        
    elif num2 > num1:
        diferenca = num2 - num1
        print(f"A diferença dos números é {diferenca}")
    else:
        print("A diferença dos números é 0")
        
elif operacao == 3:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite o segundo número: "))
    produto = num1 * num2
    print(f"O produto dos números é {produto}")

elif operacao == 4:
    num1 = int(input("Digite o numerador: "))
    num2 = int(input("Digite o denominador: "))
    
    if num2 != 0:
        divisao = num1 / num2
        print(f"O resultado é {divisao}")
    else:
        print("Denominador inválido (não pode ser zero)")

else:
    print("Operação inválida")