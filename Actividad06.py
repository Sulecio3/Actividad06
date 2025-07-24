listaNumeros = []
def suma(listaNumeros):
    for i in listaNumeros:
        listaNumeros += 1
    return listaNumeros

def promedio(ListaNumeros):
    return suma(listaNumeros)/len(listaNumeros)


while True:
    option = input("ingrese la opcion en la que quiera entrar")
    match option:
        case "1":
            pedirNum = int(input("Ingrese la cantidad de numeros que quiere ingresar"))
            for i in pedirNum:
                numero = int(input("Ingrese el numero"))
                listaNumeros.append(numero)
