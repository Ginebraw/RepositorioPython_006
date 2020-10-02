#Crear menu con 3 opciones
import os

def Numeros():
    pos=0
    neg=0
    cero=0

    cantidad=int(input("Ingrese cantidad de números a ingresar: "))
    for i in range(cantidad):
        n=int(input(str(i+1)+".-Ingresa un número: "))

        if (n>0):
            pos+=1
        elif (n<0):
            neg+=1
        else:
            cero+=1
    print("cantidad de números positivos: "+str(pos))
    print("cantidad de números negativos: "+str(neg))
    print("cantidad de 0: "+str(cero))
    pausa=input("Ingrese cualquier tecla para continuar...")

def Personas():
    sum=0
    cantidad=int(input("Ingrese cantidad de personas a ingresar: "))
    for i in range(cantidad):
        nom=input(str(i) + ".-Ingresa un nombre: ")
        edad=int(input(str(i)+ ".-Ingrese la edad: "))
        sum=sum+edad
    print("El promedio de las edades es: " + str(sum/cantidad))
    pausa=input("Ingrese cualquier tecla para continuar...")

seguir=True
while (seguir):
    os.system('cls')
    print("1. Numeros")
    print("2. Datos Personales")
    print("3. Finalizar")
    op=int(input("Digite opción 1,2,3: "))
    if(op==1):
        Numeros()  #Invocamos un metodo
    if (op==2):
        Personas()
    if (op==3):
        print("Programa Finalizado")
        pausa=input("Ingrese cualquier tecla para continuar...")
        break