# Act 1 
precios_frutas={'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300

#Act 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Act 3
lista_frutas=list(precios_frutas.keys())

#Act 4
contactos={}
for i in range(5):
    nombre= input("Ingrese el nombre del contacto: ")
    numero= input("Ingrese el número de telefono: ")
    contactos[nombre]=numero
consulta= input("Ingrese el nombre que desea consultar: ")
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("El contacto no existe.")

#Act 5
frase= input("Ingrese una frase: ")
palabras= frase.split()
palabras_unicas= set(palabras)
print(f"Palabras únicas: {palabras_unicas}")
recuento= {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra]+=1
    else:
        recuento[palabra]= 1
print(f"Recuento: {recuento}")

#act 6
alumnos= {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

#Act 7
parcial_1 = {1, 2, 3, 4, 5}
parcial_2 = {4, 5, 6, 7, 8}
aprobaron_ambos = parcial_1.intersection(parcial_2)
print(f"Aprobaron ambos parciales: {aprobaron_ambos}")
aprobaron_solo_uno = parcial_1.symmetric_difference(parcial_2)
print(f"Aprobaron solo uno: {aprobaron_solo_uno}")
aprobaron_al_menos_uno = parcial_1.union(parcial_2)
print(f"Lista total (al menos uno): {aprobaron_al_menos_uno}")

#Act 8
inventario = {"lapices": 50, "cuadernos": 20, "gomas": 30}
accion = input("¿Qué desea hacer? (consultar/agregar/nuevo): ").lower()
if accion == "consultar":
    producto = input("Ingrese el producto: ")
    print(inventario.get(producto, "El producto no existe en el inventario."))
elif accion == "agregar":
    producto = input("Ingrese el producto: ")
    if producto in inventario:
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        inventario[producto] += cantidad
        print(f"Nuevo stock de {producto}: {inventario[producto]}")
    else:
        print("El producto no existe. Elija la opción 'nuevo' para agregarlo.")
elif accion == "nuevo":
    producto = input("Ingrese el nombre del nuevo producto: ")
    if producto not in inventario:
        cantidad = int(input("Ingrese el stock inicial: "))
        inventario[producto] = cantidad
        print(f"Producto {producto} agregado exitosamente.")
    else:
        print("El producto ya existe en el inventario.")

#Act 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (HH:MM): ")
actividad = agenda.get((dia, hora), "No hay actividades registradas en ese horario.")
print(actividad)
#Act 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)
