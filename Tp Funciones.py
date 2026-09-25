# Act 1 hola mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# Act 2 Saludar usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre_ingresado=input("Ingresa tu nombre: ")
resultado= saludar_usuario(nombre_ingresado)
print(resultado)

# Act 3 saludar usuario
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre = input("Ingrese su nombre: ")
apellido =input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia =input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# Act 4 circulo
import math
def calcular_area_circulo(radio):
    return math.pi * (radio**2)
def calcular_perimetro_circulo(radio):
    return 2*math.pi*radio
radio_usuario= float(input("Ingrese el radio del circulo: "))
area= calcular_area_circulo(radio_usuario)
perimetro= calcular_perimetro_circulo(radio_usuario)
print(f"El área es de: {area}")
print(f"El perímetro es de: {perimetro}")

# Act 5  segundos a horas
def segundos_a_horas(segundos):
    return segundos/3600
segundos= float(input("Ingrese la cantidad de segundos: "))
horas= segundos_a_horas(segundos)
print(f"Los segundos equivalen a {horas} horas")

# Act 6 Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")
num =int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)

# Act 7 op basicas
def operaciones_basicas(a, b):
    suma= a+b
    resta= a-b
    multiplicacion=a*b
    division=a/b
    return (suma, resta, multiplicacion, division)
numero1= float(input("Ingrese el primer número: "))
numero2= float(input("Ingrese el segundo número: "))
resultado= operaciones_basicas(numero1, numero2)
print("Resultados: ")
print(f"suma: {resultado[0]}")
print(f"resta: {resultado[1]}")
print(f"multiplicación: {resultado[2]}")
print(f"división: {resultado[3]}")

# Act 8 imc
def calcular_imc(peso, altura):
    return peso/(altura**2)
peso_ingresado= float(input("Ingrese su peso en Kilos: "))
altura_ingresada= float(input("Ingrese su peso en mentros: "))
imc=calcular_imc(peso_ingresado, altura_ingresada)
print(f"Su IMC es de: {imc:.2f}")

#Act 9 Celcius a Fahrenheit
def celcius_a_fahrenheit(celcius):
    return (celcius * 9/5)+32
celcius=float(input("Ingrese la temperatura en Grados Celcius: "))
fahrenheit= celcius_a_fahrenheit(celcius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# Act 10 promedio
def calcular_promedio(a, b, c):
    return (a+b+c)/ 3
num1= float(input("Ingrese el primer número: "))
num2= float(input("Ingrese el segundo número: "))
num3= float(input("Ingrese el tercer número: "))
promedio_final= calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números es de: {promedio_final}")
