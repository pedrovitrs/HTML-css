numero1 = float(input('Escolha o numero: '))
numero2 = float(input('escolha o segundo numero: '))
calculadora = int(input(' [1] multiplicação \n [2] divisão \n [3] soma \n [4] subtração \n [5] sair \n qual você escolhe: '))
if calculadora==1:
    print(F'{numero1} X {numero2} = {numero1*numero2}')
if calculadora==2:
    print(F'{numero1} ÷ {numero2} = {numero1/numero2}')
if calculadora==3:
    print(F'{numero1} + {numero2} = {numero1+numero2}')
if calculadora==4:
    print(F'{numero1} - {numero2} = {numero1-numero2}')
if calculadora==5:
    print('você saio da calculadora')