def pedirDatos (lista):
    pedirNum = int(input("Ingrese la cantidad de numeros que quiere ingresar: "))
    for i in range(pedirNum):
        numero = int(input("Ingrese el numero: "))
        lista.append(numero)

def suma(numeros):
    suma = 0
    for i in numeros:
        suma += i
    return suma

def promedio(numeros):
    return suma(numeros)/len(numeros)

def positivoNegativo (numeros):
    positivos = 0
    negativos = 0
    for i in numeros:
        if i > 0:
            positivos +=1
        else:
            negativos += 1
    return print(f"La cantidad de numeros positivos es: {positivos} y de negativos: {negativos}")

def area(a,b):
    area = (a*b)/2
    return print(f"El area del triangulo es: {area}")

def parImpar(num):
    if num%2==0:
        print("Es par")
    else:
        print("Es impar")

def numeroMayorMenor(listaNum):
    mayor = max(listaNum)
    menor = min(listaNum)
    return print(f"El numero mayor es: {mayor} y el numero menor es: {menor}")


while True:
    print("--Bienvenido al Menu--")
    print("1. Suma, promedio y la cantidad de numeros positivos y negativos")
    print("2. Area de un triangulo")
    print("3. Verificar si el numero es par o impar")
    print("4. calcular el promedio")
    print("5. Mostrar cual es el mayor y menor")
    print("6. Salir")
    option = input("ingrese la opcion en la que quiera entrar: ")
    match option:
        case "1":
            listaNumeros = []
            pedirDatos(listaNumeros)
            print(f"La suma de todos sus numeros es: {suma(listaNumeros)}")
            print(f"El promedio de todos sus numeros es: {promedio(listaNumeros)}")
            positivoNegativo(listaNumeros)
        case "2":
            altura= int(input("Ingrese la altura del triangulo: "))
            base = int(input("Ingrese la base del triangulo: "))
            area(altura, base)
        case"3":
            numero= int(input("Ingrese el numero que quiere evaluar"))
            parImpar(numero)
        case "4":
            calificaciones = []
            pedirDatos(calificaciones)
            print(f"El promedio de sus calificaciones: {promedio(calificaciones)}")
        case "5":
            listaNumeros = []
            pedirDatos(listaNumeros)
            numeroMayorMenor(listaNumeros)
        case "6":
            print("Saliendo del programa")
            break
        case _:
            print("opcion no valida, intente de nuevo")