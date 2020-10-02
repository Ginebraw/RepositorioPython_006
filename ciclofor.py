par=0
impar=0
for i in range(10):
    nume=int(input("Digite un numero: "))
    if(nume%2==0):
        par=par+1
    else:
        impar=impar+1
print("La cantidad de numeros pares es: " + str(par))
print("La cantidad de numeros impares es: "+ str(impar))
