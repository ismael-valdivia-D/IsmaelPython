# frutas=["Maracuyá", "Pera"]

# def muestraFruta():
#     print("-"*20)
#     c=1
#     for f in frutas:
#         print(f"{c}.- {f}")
#         c+=1
#     print("-"*20)

# def agregaFruta():
#     nombreF=input("Ingrese el nombre del Fruta: ")
#     frutas.append(nombreF)

# def eliminaFruta():
#     muestraFruta()
#     opc=int(input("Seleccione el numero de la fruta a eliminar: "))
#     frutas.pop(opc-1)

# def actualiazaFruta():
#     muestraFruta()
#     opci=int(input("Seleccione el numero de la fruta a eliminar: "))
#     nuevaFruta=input("ingrese la nueva fruta: ")
#     frutas[opci-1]=nuevaFruta

# def feria():
#     while True:
#       print("1.- Agregar Fruta")
#       print("2.- Eliminar Fruta")
#       print("3.- Actualizar Fruta")
#       print("4.- Mostrar Frutas")
#       print("5.- Salir")
#       op=int(input("Seleccione una opcion: "))
#       match op:
#          case 1:
#             agregaFruta()
#          case 2:
#             eliminaFruta()
#          case 3:
#             actualiazaFruta()
#          case 4:
#             muestraFruta()
#          case 5:
#             print("Salir")
#             break
#          case _:
#             print("Opcion invalida")   


# feria()

# vegetales={
#    1: "maracuya",
#    2: "pera",
#    3: "Cebolla",
#    7: "papa" 
# }

# print(len(vegetales))

# def agregaVegetal():
#    nombreF=input("Ingrese el nombre del vegetal: ")
#    vegetales[list(vegetales.items())[-1][0]+1]=nombreF

# def muestravegetal():
#    for key, value in vegetales.items():
#       print(key,".-", value)
#       print("-"*30)

# def EliminaVegetal():
#    muestravegetal
#    opc=int(input("Seleccione el numero de el vegetal a eliminar: "))
#    vegetales.pop[opc-1]

# def ActualizacionVegetal():
#     muestravegetal()
#     Actualizar=int(input("Seleccione el numero de la fruta a eliminar: "))
#     nuevoVegetal=input("ingrese la nueva fruta: ")
#     vegetales[Actualizar]=nuevoVegetal

# def VegetalesMenu():
#    while True:
#       print("1.- Agregar Vegetal")
#       print("2.- Eliminar Vegetal")
#       print("3.- Actualizar Vegetal")
#       print("4.- Mostrar Vegetal")
#       print("5.- Salir")
#       op=int(input("Seleccione una opcion: "))
#       match op:
#          case 1:
#             agregaVegetal()
#          case 2:
#             EliminaVegetal()
#          case 3:
#             ActualizacionVegetal()
#          case 4:
#             muestravegetal()
#          case 5:
#             print("Salir")
#             break
#          case _:
#             print("Opcion invalida")   j
   
# VegetalesMenu()
   
# productosList=[
#     {"nombre":"Maracuya","precio":3000},
#     {"nombre":"Pera","precio":1500},
#     {"nombre":"Cebolla","precio":1200}
# ]
productosDicc={
   1:{"nombre":"Maracuya","precio":3000},
   2:{"nombre":"Pera","precio":1500},
   3:{"nombre":"Cebolla","precio":1200}
}

def mostrarDicc():
    for key, value in productosDicc.items():
        print(key,".-", value)
        print("-"*30)

def Compra():
   precio=0
   mostrarDicc()
   op=int(input("Ingrese el numero del producto a comprar"))


def CarritoCompras():
  while True:
      print("1.- Comprar")
      print("2.- Crear Boleta")
      print("3.- Salir")
      op=int(input("Seleccione una opcion: "))
      match op:
         case 1:
           Compra()
         case 2:
            
         case 3:
            print("Salir")
            break
         case _:
            print("Opcion invalida")  


