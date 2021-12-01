# Kreff_Facundo
# Practica para final
import os
import random
# La dirección de tránsito de un municipio necesita un programa para gestionar los datos de las distintos multas que sus
# agentes han emitido en la ciudad. Por cada multa se conoce su número de identificación (un entero), la patente del
# vehículo multado (una cadena), un número entero entre 0 y 24 que indica el tipo de multa (por ejemplo: 0: cruce en
# rojo, 1: mal estacionamiento, etc.) y finalmente el importe a pagar por la misma (un número en coma flotante).

class Multa:
    # Generador patente
    def Patente():
        a = random.randrange(1, 3)
        if a == 1:
            letras = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(
                ("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
            patente = letras + str(numeros)
            return patente
        else:
            letras1 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            numeros = str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
            letras2 = random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ")) + random.choice(("ABCDEFGHYJKLMOPQRSTUVWXYZ"))
            patente = letras1 + str(numeros) + letras2
            return patente

    def __init__(self, numIden=random.randint(1,400), patente=Patente(), tipoMulta=random.randint(0, 24), montoPagar=random.randint(500,4000)):
        self.numero=numIden
        self.patente=patente
        self.tipoMulta=tipoMulta
        self.monto=montoPagar


#Desarrollo de la opcion 1
def Opcion_1():
    registro = []
    cantMultas = int(input("Cantidad de multas a ingresar: "))
    for i in range(cantMultas):
        registro.append(Multa())
        print('\nNuevo ingreso')
        print('Numero: ' + str(registro[i].numero) + '\nPatente: ' + str(registro[i].patente))
        print('Tipo Multa: ' + str(registro[i].tipoMulta) + '\nMonto: ' + str(registro[i].monto))
    return registro

#Desarrollo de la opcion 2
def Opcion_2(ar):
    if type(ar) == str:
        print("\033[0;31"+"aAun no se a cargado los datos"+"\033[0;m")
    else:
        for i in range(len(ar)):
            print("   N° identificacion: " ,ar[i].numero,"   Patente: " ,ar[i].patente,"   Tipo: " ,ar[i].tipoMulta,"   Monto: " ,ar[i].monto)

# 1)Desarrollar un programa completo con menú de opciones que permita cumplir los requerimientos que se indican
# a continuación. [máximo: 3 puntos – 12% del total]

def Menu():
    i = 1
    arreglo = ""
    # Ciclo While para generar menu
    while (i > 0 or i < 10):
        # Mostrar en pantalla menu
        print("\033[4;33m" + "\nGestion de multas de la Municipalidad" + '\033[0;m')
        print("1. Carga de Datos")
        print("2. Mostrar Datos")
        print("3. Crear arreglo con multas mayor al promedio")
        print("4. Mostrar multas mayor al promedio")
        print("5. Buscar y aumentar un 10% multa del punto 4")
        print("6. Importe acumulado por tipo de multa")
        print("7. Crear un archivo sin los tipo de multa 0, 1, 2 y 3")
        print("8. Mostrar el archivo")
        print("9. Salir")
        i = int(input("\033[1;4;32m"+"\nIngrese la opcion seleccionada:"+"\033[0;m"+" "))
        # Opcion 1
        # Cargar los datos de las multas en un arreglo, pero de forma tal que el arreglo siempre vaya quedando ordenado
        # por número de identificación. Se considerará INCORRECTA una solución basada en cargar todo el arreglo y
        # ordenarlo al final. Realice las validaciones que considere necesarias. Puede desarrollar este punto haciendo que
        # el programa genere en forma aleatoria el contenido de cada registro que se vaya a agregar. [máximo: 3 puntos –
        # 12% del total]
        if i == 1:
            arreglo = Opcion_1()
        # Opcion 2
        elif i == 2:
            Opcion_2(arreglo)
        # Opcion 3
        elif i == 3:
            print(3)
        # Opcion 4
        elif i == 4:
            print(4)
        elif i == 5:
            print(5)
        elif i == 6:
            print(6)
        elif i == 7:
            print(7)
        elif i == 8:
            print(8)
        elif i == 9:
            print("\n\u001B[1;30;46m\n  Fin del Programa ;)\n\n\u001B[0;m")
            break
        else:
            print("\n\u001B[1;31mOpcion Incorrecto! \nVuelva a ingresar N° opcion\u001B[0;m")
            i=1

Menu()