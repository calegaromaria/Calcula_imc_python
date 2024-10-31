#calcular o imc em python
nome = ""
altura = 0 
peso = 0
imc = 0

def le_dados():
    global nome
    global altura
    global peso
    nome = input ("digite seu nome, por favor: ")
    altura = float(input("Digite sua altura: "))
    peso = int(input("digite seu peso: "))

def calcula_imc():
   peso
   altura
   imc = peso / pow(altura, 2)
   return round (imc, 2)


def avalia_imc():
    imc = calcula_imc()
    if imc < 18.5: 
        return "abaixo do peso."
    elif imc >= 18.5 and imc <25:
        return "com peso normal"
    else :
       return "com sobrepeso"
    
le_dados()
imc =calcula_imc()
msg = avalia_imc()
print(f'{nome} está {msg}')
    