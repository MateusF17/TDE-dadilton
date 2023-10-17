Km = float(input("Digite a distância em Km: "))
gasolina = float(input("Digite o consumo gasto de gasolina: "))

consumo = Km / gasolina

if consumo < 8:
    mensagem = "Venda o carro!"
elif consumo >= 8 and consumo <= 14:
    mensagem = "Econômico!"
else:
    mensagem = "Super econômico!"