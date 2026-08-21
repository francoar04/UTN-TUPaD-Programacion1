#1ra actividad
print("Hola Mundo!")
#2da actividad
nombre= input("Ingrese su nombre por favor:")
print(f"¡Hola {nombre}!")
#3er actividad
Nombre= input("Ingrese su nombre nuevamente:")
apellido= input("Ingrese su apellido:")
edad= input("ingrese su edad:")
lugar= input("ingrese su lugar de residencia:")
print(f"Soy {Nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")
#4ta actvididad
radio= float(input("Ingrese el radio de un círculo: "))
pi= 3.14159
area= (pi*radio*radio)
perimetro= (2*radio*pi)
print (f"El Radio es de:{radio}, su area es de: {area:.2f} y su perimetro es de: {perimetro:.2f}")
#5ta actividad
segundos= float(input("Ingrese una cantidad de segundos: "))
horas= round(segundos / 3600, 2)
print (f"La cantidad de {segundos} segundos, son un total de {horas} horas.")
#6ta actividad
Tabla= int(input("Ingrese un número:"))
print (f"Esta es la tabla de multiplicar del número {Tabla}")
print (f"{Tabla} x 1= {Tabla * 1}")
print (f"{Tabla} x 2= {Tabla * 2}")
print (f"{Tabla} x 3= {Tabla * 3}")
print (f"{Tabla} x 4= {Tabla * 4}")
print (f"{Tabla} x 5= {Tabla * 5}")
print (f"{Tabla} x 6= {Tabla * 6}")
print (f"{Tabla} x 7= {Tabla * 7}")
print (f"{Tabla} x 8= {Tabla * 8}")
print (f"{Tabla} x 9= {Tabla * 9}")
print (f"{Tabla} x 10= {Tabla * 10}")
#7ma actividad
num1= int(input("Ingrese el primer número distinto a 0: "))
num2= int(input("Ingrese el segundo número distinto a 0: "))
suma= num1 + num2 
resta= num1 - num2
multiplicacion= num1 * num2 
division= num1 / num2
print (f"La suma de {num1}+{num2} da como resultado:{suma}")
print (f"La resta de {num1}-{num2} da como resultado:{resta}")
print (f"La multiplicación de {num1}x{num2} da como resultado:{multiplicacion}")
print (f"La división de {num1}/{num2} da como resultado:{division}")
#8va actividad
altura= float(input("Ingresar su altura en metros: "))
peso= float(input(" ahora ingrese su peso:  "))
imc= float(peso/altura**2)
print (f"su indice de masa corporal es de {imc:.2f}")
#9na actividad
celcius= int(input("Por favor ingrese la temperatura en grados Celcius para saber su equivalente en Fahrenheit: "))
Fahrenheit= 9/5*celcius+32
print (f"{celcius} grados Celcius equivalen a {Fahrenheit} grados Fahrenheit")
#10ma actividad
n1= float(input("Ingresar el primer número:"))
n2= float(input("Ingresar el segundo número:"))
n3= float(input("Ingresar el tercer número:"))
suma2= n1+n2+n3
promedio= suma2/3
print (f"El promedio de esos tres numeros es de {promedio}")
