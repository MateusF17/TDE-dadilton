num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if num1 > num2:
    print("{} é maior que {}".format(num1, num2))

elif num2 > num1:
    print("{} é maior que {}".format(num2, num1))

else:
    print("Os dois números são iguais")