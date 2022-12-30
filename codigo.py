print('== TABELA IMC ==')
peso = float(input('Digite seu peso(EM QUILOS): '))   #Tipo primitivo 'float' pois é um número real.
altura = float(input('Digite sua altura (EM METROS): '))   #Variável 'altura' também no float.
imc = peso / (altura * altura)  #Calculo do IMC.

#Agora as estruturas condicionais:

if (imc < 18.5):
    print('Abaixo do peso ideal.')
    print('Seu IMC é ' ,imc)  #Concatenando com a vírgula.
elif (imc >= 18.5) and (imc <= 24.9):
    print('Peso ideal.')
    print('Seu IMC é ' ,imc)
elif (imc >= 25) and (imc <= 29.9):
    print('Acima do peso.')
    print('Seu IMC é ' ,imc)
elif (imc >= 30) and (imc <= 34.9):
    print('Obesidade 1')
    print('Seu IMC é ' ,imc)
elif (imc >= 35) and (imc <= 39.9):
    print('Obesidade 2')
    print('Seu IMC é ' ,imc)
else:
    print('Obseidade 3')
    print('Seu IMC é ' ,imc)
