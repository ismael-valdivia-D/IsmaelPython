frutas=["maracuya", "Pera"]

def muestraFrutas():
    print("-"*20)
    c=1
    for f in frutas:
        print(f"{c}.-{f}")
        c+=1
    print("-"*20)


def selctAdmin():
    while True:
        print("1.-Agregar producto")
        print("2.-Eliminar producto")
        print("3.-actualizar producto")
        print("4.-mostrar producto")
        op=int(input("seleccione una opcion: "))
        match op:
            case 1:
                frutas.append(frutas)
            case 2:
                opc=int(input("ingrese el numero de la fruta a eliminar"))
                frutas.pop(opc-1)
            case 3:
                opc=int(input("ingrese el numero de la fruta a actualizar"))
                frutas.pop(opc-1)
            case 4:
                muestraFrutas()
            case 5: 
                print("salir")
                break
            case _:
                print("Opcion invalida")