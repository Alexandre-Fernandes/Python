
idade = input('qual sua idade? ')
idade = int(idade)
altura = input('qual sua altura? ')
altura = float(altura)
peso = input('qual seu peso? ')
peso = int(peso)

altura = pow ( altura, 2)
imc = round(peso / altura, 2)


if imc <= 18:
    print('Abaixo do Peso \n Seu imc e de: ' + str(imc) )
elif imc >= 18 and imc <= 24:
    print('Normal \n Seu imc e de: ' + str(imc) )
elif imc >= 25 and imc <= 29:
    print('Sobrepeso \n Seu imc e de: ' + str(imc) )
elif imc >= 30 and imc <= 34:
    print('Obesidade \n Seu imc e de: ' + str(imc) )
elif imc >= 35 and imc <= 40:
    print('Obesidade Grau 2 \n Seu imc e de: ' + str(imc) )
elif imc >= 41:
    print('Obesidade Grau Morbida \n Seu imc e de: ' + str(imc) )
else:
    print('Nao conseguimos proceder no calculo favor CONTATAR O ADM DO SISTAMA')
    

   #adiciona mais funcoes ae
