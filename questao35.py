def is_data_valida(ano, mes, dia):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True
    else:
        bissexto = False

    if mes < 1 or mes > 12:
        return False
    
    dias_no_mes = [31, 28 if not bissexto else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if 1 <= dia <= dias_no_mes[mes - 1]:
        return True
    else:
        return False
    
ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))
dia = int(input("Digite o dia: "))

if is_data_valida(ano, mes, dia):
    print(f"A data {dia}/{mes}/{ano} é válida.")
else:
    print(f"A data {dia}/{mes}/{ano} não é válida.")