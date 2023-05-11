# Desenvolva uma calculadora de IMC, o programa deve pedir o peso e a 
# altura ao usuario, calcular o IMC e retornar para o usuario o IMC e a categoria em que se encontra

# Baixo peso: Se for menor que 18.5
# Peso normal: entre 18.6 e 24.9
# Sobrepeso: entre 25 e 29.9
# Obesidade: igual ou acima de 30

def calcular(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def determinar(imc):
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 29.9:
        categoria = "Sobrepeso"
    elif imc >= 30:
        categoria = "Obesidade"
    return categoria

altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = calcular(peso, altura)

categoria = determinar(imc)
print(" Seu índice de massa corporal é: ", imc, "você se encaixa na categoria", categoria)