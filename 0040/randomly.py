import random
#uso y explicaion de random

# num=random.randint(1, 10)
# print(num)

# for i in range(num):
#     print('hola vicente')

# for i in range(10):
#     print(f"{num}x{i}= {num*i}")

# 3 personas juegan golf 
# cada persona tiene la posibilidad de golpear
# y la distancia varia entre 60 y 190 metros
# mostrar al final el golpe mas fuerte
# j1=random.randint(60, 190)
# j2=random.randint(60, 190)
# j3=random.randint(60, 190)
# print(f"Jugador 1 golpeo a {j1} metros")
# print(f"Jugador 2 golpeo a {j2} metros")
# print(f"Jugador 3 golpeo a {j3} metros")

# if j1 > j2 and j1 > j3:
#     print(f"El golpe mas fuerte fue de {j1} metros")
# elif j2 > j1 and j2 > j3:
#     print(f"El golpe mas fuerte fue de {j2} metros")
# elif j3 > j1 and j3 > j2:
#         print(f"El golpe mas fuerte fue de {j3} metros")
# else:    print("Hubo un empate en el golpe mas fuerte")


# max_golpe = 0
# for i in range(3):
#     golpe = random.randint(60, 190)
#     print(f"Jugador {i+1} golpeo a {golpe} metros")
#     if golpe > max_golpe:
#         max_golpe = golpe
# print(f"El golpe mas fuerte fue de {max_golpe} metros")


# dado1=random.randint(1, 6)
# dado2=random.randint(1, 6)

# print(f"El dado 1 saco: {dado1}")
# print(f"El dado 2 saco: {dado2}")

# #si los dados son iguales el jugador se va a la carcel
# if dado1 == dado2:
#     print("Los dados son iguales, vas a la carcel") 
# else:    print("Los dados son diferentes, puedes avanzar")


#pelea
peleador1= 100
peleador2= 100
golpe= random.randint(7, 18)
while peleador1 > 0 and peleador2 > 0:
    peleador1 -= golpe
    print(f"el peleador 1 recibe un daño de {golpe} su HP es de {peleador1}")
    if peleador1 <= 0:
        print("El peleador 2 gana")
        break
    peleador2 -= golpe
    print(f"el peleador 2 recibe un daño de {golpe} su HP es de {peleador2}")
    if peleador2 <= 0:
        print("El peleador 1 gana")
        break

#ludo
dado2=0
psicion =0
turnos=0
while psicion < 50 :
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    posicion +=dado1 + dado2 
    turnos += 1
    print(f"turno{turnos} : el dado 1 dio {dado1} y el dado 2 dio {dado2}, la posicion actual es de {posicion}")
print(f"Felicidades, has llegado a la meta en {turnos} turnos")