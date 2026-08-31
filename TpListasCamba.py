#Actividad N1, Lista del 1 al 100 con multiplos de 4
numeros_multiplos=list(range(4,101,4))
print(numeros_multiplos)
#Actividad N2, Lista con cinco elementos
lista=["Perro","Gato","Oso","Hamburguesa","Pizza"]
print(lista[3])
#Actividad N3, Lista vacía 
Lista2=[]
print(f"Así está la lista...{Lista2}")
Lista2.append("Queso")
Lista2.append("Lechuga")
Lista2.append("Tomate")
print(f"Así queda la nueva lista... {Lista2}")
#Actividad N4, Remplazar valores..
animales=["perro","gato","conejo","pez"]
print(f"Lista sin modificar:{animales}")
animales[1]="loro"
animales[3]="oso"
print(f"La nueva lista quedaria: {animales}")
#Actividad N5, Respuesta
#numeros = [8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print(numeros)
#Lo que hace el codigo seria fijarse en la lista, ver cual es el número mas grande (gracias al max)
#y lo elimina gracias al remove.
#Actividad N6, lista de num 10 a 30
numeros= list(range(10, 31, 5))
print(numeros[0:2])
#Actividad N7, Remplazar valores
autos = ["sedan", "polo", "suran", "gol"] 
autos[1]= "raptor"
autos[2]= "fiesta"
print(autos)
#Actividad N8, Dobles
dobles=[]
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)
#Actividad N9, Compras
compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
print(compras)
#Actividad N10, Lista anidadaa
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)