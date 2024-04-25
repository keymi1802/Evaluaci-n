import random       #Importamos la librería random

def lista_aleatoria(n):         #Creamos una función que nos genere una lista de números aleatorios con n
    return [random.randint(1, 100) for _ in range(n)]  #Generamos n números en un rango de 1 al 100

def cuadrados(lista):       #Creamos una función que realice los cuadrados de los números aleatorios en la lista 
    return {i+1: num ** 2 for i, num in enumerate(lista)}     #En esta parte un poco complicado de explicar, utiliza el diccionario mandando a llamar a cada uno de los elementos y 
                                                              #Calculando el valor al cuadrado, asignadole un número a cada uno comenzando desde el uno 
n = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))     #Le pedimos al usuario que ingrese un número 
lista = lista_aleatoria(n)          #Generamos la lista de los números utilizando la función lista_aleatoria 
lista_cuadrados = cuadrados(lista_aleatoria) #Generamos la lista con los valores de los números al cuadrado 

print("Lista de números aleatorios:", lista)        #Imprimimos la lista de los aleatorios 
print("Diccionario de cuadrados:", cuadrados)       #Imprimimos la lista al cuadrado enumerados del 1 a n 
