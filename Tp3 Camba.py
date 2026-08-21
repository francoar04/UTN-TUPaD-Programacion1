#Act N1
edad= int(input("Por favor ingrese su edad: "))
if edad>=18:
    print(f"Usted es mayor de edad")
else: print("Usted es menor de edad")
#Act N2
Nota= float(input("Ingrese la nota de su examen: "))
if  Nota>=6:
    print("Usted está aprobado")
else:
    print("Usted está desaprobado")
#Act N3
Num= int(input("Ingrese un número: "))
if Num%2==0:
    print("Ha ingresado un número par")
else:
    print("Por Favor ingrese un número par")
#Act N4
Edadd= int(input("Por favor, ingrese su edad: "))
if Edadd<12:
    print("Usted es un Niño.")
elif Edadd<18:
    print("Usted es un Adolescente.")
elif Edadd<30:
    print("Usted es un Adulto Joven.")
else:
    print("Usted es un Adulto")
#Act N5
contraseña= input("Por favor ingrese una contraseña(entre 8 y 14 caracteres): ")
if 8<= len(contraseña)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("La contraseña tiene que contener entre 8 y 14 caracteres.")
#Act N6
import random
from statistics import mode, median, mean
Numrandoms= [random.randint(1,100)for _ in range(50)]
moda= mode(Numrandoms)
mediana= median(Numrandoms)
media= mean(Numrandoms)
if media>mediana and mediana>moda:
    sesgo= "Sesgo positivo o a la derecha"
elif media< mediana and mediana<moda:
    sesgo= "sesgo negativo o a la izquierda"
else: 
    sesgo= "Sin sesgo."
print("Esta es la lista del número generado:")
print(f"Su numero random es: {Numrandoms}")
print(f"moda: {moda} ")
print(f"mediana: {mediana}")
print(f"media: {media}")
print(f"tipo de sesgo: {sesgo}")
#Act N7
Frase= input("Ingrese una palabra o frase: ")
ult= Frase[-1]
vocales= "AEIOUaeiou"
if ult in vocales:
    listo = Frase + "!"
    print(f"{listo}")
else:
    print(f"{Frase}")
#Act N8
nombre= input("Ingrese su nombre por favor:")
opcion= input("Ahora elija la opcion 1(Mayúsculas), 2(Minúscula), 3(Primer letra Mayúscula y lo demas en Minúscula)")
if opcion== "1":
    Resultado1= nombre.upper()
    print(f"{Resultado1}")
elif opcion== "2":
    Resultado2= nombre.lower()
    print(f"{Resultado2}")
elif opcion== "3":
    Resultado3= nombre.title()  
    print(f"{Resultado3}") 
else:
    print("Invalido, seleccione la opcion 1, 2 o 3")
#Act N9
magnitud= float(input("Por favor ingrese la magnitud del terremoto: "))
if magnitud<2.9:
    print("Terremoto muy leve (imperceptible).")
elif magnitud<3.9:
    print("Terremoto leve (ligeramente perceptible).")
elif magnitud<4.9:
    print("Terremoto moderado(sentido por personas, pero generalmente no causa daños).")
elif magnitud<5.9:
    print("Terremoto fuerte (puede causar daños en estructuras debiles).")
elif magnitud<6.9:
    print("Terremoto muy fuerte (puede causar daños significativos).")
elif magnitud>=7:
    print("terremoto extremo (puede causar graves daños a gran escala).")
#Act N10
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
else:
    estacion_norte = "Otoño"

if hemisferio == "N":
    estacion = estacion_norte

elif hemisferio == "S":
    if estacion_norte == "Invierno":
        estacion = "Verano"
    elif estacion_norte == "Primavera":
        estacion = "Otoño"
    elif estacion_norte == "Verano":
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio inválido"

print(f"La estación es: {estacion}")
