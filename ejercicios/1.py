# op=0
# total=0
# while op!=4:
#     print("1.- PC $500.000")
#     print("2.- LGTV 55 pulgadas $450.000")
#     print("3.- Microondas Mademsa $100.000")
#     print("4.- Salir")
#     print("Seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             print("El total a pagar es ",500000*1.19 )
#             total+=500000*1.19
#         case 2:
#             print("El total a pagar es ",450000*1.19 )
#             total+=450000*1.19
#         case 3:
#             print("El total a pagar es ",100000*1.19 )
#             total+=100000*1.19
#         case 4:
#             print("Saliendo")
#             print("El total a pagar es", total)
#         case _:
#             print("Opción inválida")


# Pedir al usuario la cantidad d notas 
# mostrar el premedio de ellas
# determinar si el alumno aprueba o no

while True:
    try:
        notas=int(input("Ingrese la cant de notas: "))
        suma=0
        for i in range(notas):
            while True:
                try:
                    n=float(input(f"Ingrese la nota {i+1}: "))
                    if 1<n<7:
                        print("Error: La nota debe estar entre 1 y 7")
                        continue
                    suma=suma+n
                    break
                except ValueError:
                    print("Error: Ingrese la nota correctamente (número válido)")
        prom=suma/notas

        print("El promedio es",round(prom,1) )

        if prom>=4:
            print("Alumno aprobado")
        else:
            print("Alumno reprobado")
        break
    except ValueError:
        print("Error: Ingrese un número válido para la cantidad de notas")
    except Exception as e:
        print(f"Error: {e}")