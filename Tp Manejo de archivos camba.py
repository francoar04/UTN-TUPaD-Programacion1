#Act 1
with open ("productos.txt", "w")as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,500.0,15\n")
    archivo.write("Goma,50.0,50\n")

productos=[]
print("===Lista de Productos===")
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        datos=linea.strip().split(",")
        nombre=datos[0]
        precio=float(datos[1])
        cantidad=int(datos[2])
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

        diccionario_producto= {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        productos.append(diccionario_producto)
print("\n===Agregar un nuevo producto===")
nuevonombre=input("Ingrese el nombre del producto nuevo: ")
nuevoprecio=float(input("Ingrese el precio: "))
nuevacantidad=int(input("Ingrese la cantidad: "))
with open("productos.txt", "a")as archivo:
    archivo.write(f"{nuevonombre},{nuevoprecio},{nuevacantidad}\n")
productos.append({"nombre": nuevonombre, "precio": nuevoprecio, "cantidad": nuevacantidad})
#Act 5 
print("===Buscar Producto===")
producto_buscado= input("Ingrese el nombre del producto que desea buscar: ")
encontrado= False
for prod in productos:
    if prod["nombre"].lower()==producto_buscado.lower():
        print(f"¡Producto encontrado! -> Nombre: {prod['nombre']}| Precio: ${prod['precio']}| Cantidad: {prod['cantidad']}")
        encontrado= True
        break
if not encontrado:
    print("Error: El producto no existe...")
#Act 6 
with open("productos.txt", "w")as archivo:
    for prod in productos:
        archivo.write (f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")
print("\n ¡El archivo productos.txt ha sido actualizado con la lista final!")