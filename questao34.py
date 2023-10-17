def determinar_conceito(nota, faltas):
    if faltas <= 20:
        if 9.0 <= nota <= 10.0:
            return "A"
        elif 7.5 <= nota < 9.0:
            return "B"
        elif 5.0 <= nota < 7.5:
            return "C"
        elif 4.0 <= nota < 5.0:
            return "D"
        elif 0.0 <= nota < 4.0:
            return "E"
    else:
        if 9.0 <= nota <= 10.0:
            return "B"
        elif 7.5 <= nota < 9.0:
            return "C"
        elif 5.0 <= nota < 7.5:
            return "D"
        elif 4.0 <= nota < 5.0:
            return "E"
        elif 0.0 <= nota < 4.0:
            return "E"


nota = float(input("Digite a sua nota: "))
faltas = float(input("Digite o número de faltas: "))
conceito = determinar_conceito(nota, faltas)
print(f"Conceito do aluno: {conceito}")