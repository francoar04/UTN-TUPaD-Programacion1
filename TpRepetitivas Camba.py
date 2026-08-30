#1
#Lista del 1 al 100
for i in range(101):
    print(i)
#2
#saber cuantos digitos tiene un num entero
Nentero= int(input("ingrese un número entero: "))
Nentero= abs(Nentero)
contador= 0
if Nentero==0:
    contador=1
while Nentero!= 0:
    Nentero = Nentero //10
    contador= contador +1
print("La cantidad de digitos es de: ", contador)
#3
#suma de todos los numeros enteros dados por el usuario
primero= int(input("Ingrese el primer número entero:  "))
segundo= int(input("Ingrese el segundo número entero:  "))
suma= 0
inicio = min(primero, segundo) + 1 
fin = max(primero, segundo) 
for i in range(inicio, fin):
    suma = suma + i
print("La suma es de: ", suma)
#4
#suma en secuencia de num enteros
suma= 0
num= -1
while True:
    num= int(input("Ingresar un número para sumarlo(o 0 para terminar):"))
    if num== 0:
        break
    suma = suma + num
print("La suma total de los numeros es: ",suma)
#5
#juego de adivinar el numero aleatorio del 0 al 9
import random 
numero_aleatorio= random.randint(0, 9)
intentos= 0
num= -1
while num != numero_aleatorio:
    num= int(input("Adivine el número aleatorio (0-9): "))
    intentos= intentos+ 1
print("¡Correcto! Adivinó en un total de: ",intentos )
#6
#numeros pares entre el 0 y el 100
for i in range( 100, -1, -2):
    print(i)
#7
#suma de numeros
numeron= int(input("ingrese un número entero positivo: "))
suma= 0
for i in range(0, numeron + 1):
    suma= suma + i
print("La suma de todos los números desde 0 hasta", numeron, "es:", suma)
#8
#indica en 100numeros cuantos son pares, impares, positivos y negativos
pares= 0
impares= 0
positivos= 0
negativos= 0
for i in range(100):
    num= int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares+= 1
    else:
        impares+= 1
    if num > 0:
        positivos +=1
    elif num < 0:
        negativos+=1 
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
#9 
#calcular la media 
suma= 0
for i in range(100):
    num= int(input("Ingrese un número entero: "))
    suma += num
media= suma/100
print("La media de los números ingresados es:", media)
#10
#invertidor de digitos de un numero 
num= int(input("Ingrese un número entero: "))
negativo= num<0
num=abs(num)
invertido= 0
while num != 0:
    digito = num % 10
    invertido= invertido * 10 + digito
    num = num // 10
if negativo:
    invertido=invertido*-1
print("el número quedaria",invertido)

