ano_atual = 2023

def eh_ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def data_eh_valida(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False

    if mes == 2:
        if eh_ano_bissexto(ano):
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False
    elif mes in [4, 6, 9, 11]:
        if dia < 1 or dia > 30:
            return False
    else:
        if dia < 1 or dia > 31:
            return False

    if ano > ano_atual:
        return False

    return True

dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

if data_eh_valida(dia, mes, ano):
    print("Data válida")
else:
    print("Data inválida")