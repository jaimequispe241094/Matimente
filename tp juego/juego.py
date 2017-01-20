import random
from os import system

def seguir(nivel):
##    la funcion pregunta si el usuario qiere seguir jugando o no
    print("Felicitaciones!! paso de Nivel!!\ntu puntaje fue de: ",nivel)
    input("presione Enter para Continuar")
    system("cls")
    opcion=input("¿desea seguir jugando?\nrespuesta: ")
    opcion=opcion.upper()
    system("cls")
    while opcion!="SI" and opcion!="NO":
        opcion=input("¿desea seguir jugando?\nrespuesta: ")
        opcion=opcion.upper()
        system("cls")
    return opcion

def corroborar(jugador):
##    corrobora si el usuario realmente existe para reanudar su juego
    player=input("escriba el nombre con el que se guardo su partida: ")
    system("cls")
    archivo=str(player)+".txt"
    try:
        fichero=open(archivo)
        fichero.close()
        p="SI"
    except:
        p="NO"

    if p=="SI":
        f=open(str(player)+".txt","r")
        p=f.readline()
        puntos=int(p)
        f.close()
        system("cls")
##        si el usuario ya completo todo el juego se le da la opcion de empazar de nuevo
##        o dejar guardada supartida
        if puntos>=700:
            a=input("ya terminaste el juego\n¿quiere empezar de nuevo?")
            a=a.upper()
            system("cls")
            while a!="SI" and a!="NO":
                a=input("ya terminaste el juego\n¿quiere empezar de nuevo?")
                a=a.upper()
            if a=="SI":
                archivo=open(str(player)+".txt","w")
                archivo.write(str(0))
                archivo.close()
                input("Su partida ha sido reiniciada!\npresiona enter para volver al menu")
                system("cls")
                menu()
            else:
                input("presiona enter para volver al menu")
                system("cls")
                menu()

        else:
            jugador=player
            juego(jugador,puntos)
    else:
        print("el nombre que usted ingreso no esta registado en MATIMENTE")
        input("enter para volver al menu")
        system("cls")
        menu()
    return()

def existearchivo(jugador):
##    se corrobora si el usuario existe o no
    archivo=str(jugador)+".txt"
    try:
        fichero=open(archivo)
        fichero.close()
        p="SI"
##        el usuario existe
    except:
        p="NO"
##        el usuario no existe
    if p=="SI":
##        se pide que ingrese otro usuario hasta que su existencia sea no valida,
##        entonces cuanto esto sucede se crea el usuario
        while True:
            system("cls")
            jugador=input("el usuario ya existe ingrese otro nombre: ")
            system("cls")
            archivo=str(jugador)+".txt"
            try:
                fichero=open(archivo)
                fichero.close()
                p="SI"
            except:
                p="NO"

            if p=="NO":
                archivo=open(str(jugador)+".txt","w")
                archivo.write(str(0))
                archivo.close()
                break
    else:
##        el usuario se crea
         archivo=open(str(jugador)+".txt","w")
         archivo.write(str(0))
         archivo.close()
    print("¡Hola:",jugador,"bienvenido a matimente!")
    print("El juego consiste en una serie de ejercicios matematicos\npara poner a prueba tu mente")
    input("presione enter para continuar")
    system("cls")
    return ()

def lectura(fichero):
##    abre un un archivo especifico(ayuda, estadistica o pistas) y se lo muestra al
##    usuario para que lo lea hasta que el mismo desee volver al menu
    linea=fichero.readline()
    print(linea)
    while linea!="":
        linea=fichero.readline()
        print(linea)
    input("presione enter para volver al menu")
    fichero.close()
    system("cls")
    menu()
    return()

def estadisticayjugada(jugador,nivel):
##    se guardan los datos de jugadas en las estadisticas y en archivo del
##    usuario
    fichero=open("estadisticas.txt","w")
    fichero.write("jugador: ")
    fichero.write(str(jugador))
    fichero.write("\npuntaje: ")
    fichero.write(str(nivel))
    fichero.close()
    arc=open(str(jugador)+".txt","w")
    arc.write(str(nivel))
    arc.close()
    return()


def reanudar():
##    reanuda el juego desde donde se quedo por ultima vez el usuario
##       solo si tiene alguna artida guardada
    preg=input("¿usted ya jugo este juego?\nrespuesta: ")
    preg=preg.upper()
    system("cls")
    while preg!="SI" and preg!="NO":
        preg=input("ya jugo el juego?\nrespuesta: ")
        preg=preg.upper()
        system("cls")
    if preg=="SI":
        corroborar(jugador)
    else:
        print("Entonces deberas comenzar a jugar desde el principio!")
        input("presione enter para ir al menu")
        system("cls")
        menu()
    return()

def menu():
##    se le muestra al usuario el menu y se le pide que elija una de las opciones
##     validas dependiendo la opcion que este elija se lo manda a una a otra funcion
##     con una tarea especifica
    print("**********MENU**********")
    print("Comenzar (presione C)\nEstadisticas (presione E)\nReanudar (presione R)")
    print("Pistas (presione P)\nAyuda (presione A)\nSalir (presione S)")
    opc=input("\nElija una opcion: ")
    opc=opc.upper()
    system("cls")
    while opc!="A" and opc!="C" and opc!="S" and opc!="E" and opc!="R" and opc!="P":
        print("**********MENU**********")
        print("Comenzar (presione C)\nEstadisticas (presione E)\nReanudar (presione R)")
        print("Pistas (presione P)\nAyuda (presione A)\nSalir (presione S)")
        opc=input("\nPor favor elija una opcion valida: ")
        opc=opc.upper()
        system("cls")

    if opc=="C":
        juego(jugador,puntos)
    elif opc=="E":
        fichero=open("estadisticas.txt","r")
        lectura(fichero)
    elif opc=="R":
        reanudar()
    elif opc=="A":
        fichero=open("ayuda.txt","r")
        lectura(fichero)
    elif opc=="P":
        fichero=open("pistas.txt","r")
        lectura(fichero)
    else:
##        esta es la opcion S con ella simplemente se cierra el juego
        input("ADIOS!!\nGracias por elegir Matimente\npresione enter para salir")
        system("cls")
    return ()

def juego(jugador,puntos):
##    esta funcion contiene los niveles que componen el juego!
    if puntos==0:
        print("Nivel 1")
        nivel=0
        while nivel<100 and nivel>-100:
            num=random.randint(1,50)
            print(num,"¿es par o impar?")
            if num%2==0:
                solucion="PAR"
            else:
                solucion="IMPAR"
            resp=input("respuesta: ")
            resp=resp.upper()
            system("cls")
            while resp!="PAR" and resp!="IMPAR":
                print(num,"¿es par o impar?")
                resp=input("respuesta: ")
                resp=resp.upper()
                system("cls")
            system("cls")
            if resp==solucion:
                nivel+=20
            else:
                nivel-=10
        if nivel>=100:
            siono=seguir(nivel)
            if siono=="SI":
                estadisticayjugada(jugador,nivel)
                puntos=nivel
            else:
                estadisticayjugada(jugador,nivel)
                menu()
        else:
            print("usted supero el limite de respuestas incorrectas")
            input("presione enter para volver al menu")
            system("cls")
            menu()

    if puntos>=100 and puntos<250:
        print("Nivel 2")
        nivel=0
        while nivel<250 and nivel>-250:
            nu1=random.randint(1,20)
            nu2=random.randint(1,20)
            suma=nu1+nu2
            while True:
                print("¿cual es el resultado de la siguiente suma: ",nu1,"+",nu2,"?")
                resp=input("respuesta: ")
                system("cls")
                try:
                    resp=float(resp)
                    break
                except ValueError:
                    print("respuesta no valida!")
                    input("enter para continuar")
                    system("cls")

            if resp==suma:
                nivel+=30
            else:
                nivel-=20

        if nivel>=250:
            siono=seguir(nivel)
            if siono=="SI":
                estadisticayjugada(jugador,nivel)
                puntos=nivel
            else:
                estadisticayjugada(jugador,nivel)
                menu()
        else:
            print("usted supero el limite de respuestas incorrectas")
            input("presione enter para volver al menu")
            system("cls")
            menu()

    if puntos>=250 and puntos<400:
        print("nivel 3")
        nivel=0
        while nivel<400 and nivel>-400:
            num1=random.randint(10,100)
            num2=random.randint(1,10)
            resto=(num1%num2)
            while True:
                print("¿Cual es el resto de la siguiente cuenta:",num1,"/",num2,"?")
                resp=input("respuesta: ")
                system("cls")
                try:
                    resp=float(resp)
                    break
                except ValueError:
                    print("respuesta no valida!")
                    input("enter para continuar")
                    system("cls")
            if resp==resto:
                nivel+=45
            else:
                nivel-=30

        if nivel>=400:
            siono=seguir(nivel)
            if siono=="SI":
                estadisticayjugada(jugador,nivel)
                puntos=nivel
            else:
                estadisticayjugada(jugador,nivel)
                menu()
        else:
            print("usted supero el limite de respuestas incorrectas")
            input("presione enter para volver al menu")
            system("cls")
            menu()

    if puntos>=400 and puntos<550:
        print("Nivel 4")
        nivel=0
        while nivel<550 and nivel>-550:
            num=random.randint(1,30)
            cont=0
            for i in range(1,num+1):
                if (num%i)==0:
                    cont+=1
            while True:
                print("¿Cuantos divisores tiene: ",num,"?")
                resp=input("respuesta: ")
                system("cls")
                try:
                    resp=float(resp)
                    break
                except ValueError:
                    print("respuesta no valida!")
                    input("enter para continuar")
                    system("cls")
            if resp==cont:
                nivel+=75
            else:
                nivel-=40

        if nivel>=550:
            siono=seguir(nivel)
            if siono=="SI":
                estadisticayjugada(jugador,nivel)
                puntos=nivel
            else:
                estadisticayjugada(jugador,nivel)
                menu()
        else:
            print("usted supero el limite de respuestas incorrectas")
            input("presione enter para volver al menu")
            system("cls")
            menu()

    if puntos>=550 and puntos<700:
        print("Nivel 5")
        nivel=0
        while nivel<700 and nivel>-700:
            valor1=random.randint(3,20)
            valor2=random.randint(3,10)
            oper=(valor1*valor2)
            while True:
                print("Â¿resultado de la operacion:",valor1,"*",valor2,"?")
                resp=input("respuesta: ")
                system("cls")
                try:
                    resp=float(resp)
                    break
                except ValueError:
                    print("respuesta no valida!")
                    input("enter para continuar")
                    system("cls")
            if resp==oper:
                nivel+=100
            else:
                nivel-=65
        if nivel>=700:
            print("Felicitaciones!! Terminaste el ultimo Nivel!!\ntu puntaje fue de: ",nivel)
            input("presione Enter para Continuar")
            system("cls")

            print("Felicidades",jugador,"Has llegado al final del juego!!")
            input("Gracias por Jugar!\npresione enter para ir al menu")
            system("cls")
            estadisticayjugada(jugador,nivel)
            menu()
        else:
            print("usted supero el limite de respuestas incorrectas")
            input("presione enter para volver al menu")
            system("cls")
            menu()
    return()

##programaga principal!
jugador=input("ingrese su nombre: ")
existearchivo(jugador)
puntos=0
menu()


