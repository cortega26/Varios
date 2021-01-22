#1ra. Parte
#código para calcular el Dígito Verificador un RUT dado (sin guión, sin punto y sin dígito verificador)
#Este código ha sido tomado de https://gist.github.com/rbonvall/464824#file-rut-py

from itertools import cycle

def digito_verificador(RUTsinDV):
    reversed_digits = map(int, reversed(str(RUTsinDV)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11


#2da. Parte
#código para calcular si el dígito verificador de un RUT dado es correcto
#Validaciones que realiza el código:
# 1. Que el RUT no contenga puntos
# 2. Que contenga un guión
# 3. Que contenga un dígito verificador

def ValidaRUT(RUT):
    Guion=0
    CantidadDV=0
    Puntos=0
    CantidadDigitosRUT=len(RUT)-2
    for i in RUT:
        if i==".":
            Puntos+=1  
        elif i=="-":
            Guion+=1
        elif Guion==1:
            CantidadDV+=1 
    if Guion==1 and CantidadDV==1 and Puntos==0:
        RUTsinDV=RUT[0:CantidadDigitosRUT]
        DVindicado=RUT[CantidadDigitosRUT+1:CantidadDigitosRUT+2]
        if DVindicado=="k" or DVindicado=="K":
            DVindicado=10
        #print(DVindicado, digito_verificador(RUTsinDV))
        #print(type(DVindicado))
        #print(type(digito_verificador(RUTsinDV)))
        if int(DVindicado)==digito_verificador(RUTsinDV):
            print("El RUT es válido")
        else:
            print("El dígito verificador es incorrecto")
    else:
        print("El RUT es inválido")
        
RUT=input("Ingrese el RUT sin puntos y con guion: ")
ValidaRUT(RUT)
print("programa finalizado")
