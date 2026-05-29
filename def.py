productos={
    ['xbox series S',300000],

}
def menuProd():





def selctAdmin():
    while True:
        print("1.-Agregar producto")
        print("2.-Eliminar producto")
        print("3.-actualizar producto")
        print("4.-mostrar producto")
        op=int(input("seleccione una opcion: "))
        match op:
            case 1:
                nombrep=input('ingrese el n,bre del producto')
                preciop=int(input("ingrese el precio del producto"))
                productos.append([nombrep,preciop])
            case 4:
                

