frutas = {'manzana': 22, 'mango': 25, 'pera': 34, 'platano': 28, 'fresa': 52, 'coco': 32}   #Creamos nuestro diccionario con el nombre de las frutas y su respectivo precio

def calcular(fruta, cantidad):           #Creamos una función que calcule el total de cada fruta
    precio_fruta = frutas.get(fruta, None)      #Con el .get obtemenos la fruta del diccionario, si no se encuentra nos devolverá Nona
    if precio_fruta is not None:        # Si la fruta está en el diccionario, es decir que su valor no es None 
        return precio_fruta * cantidad  #Realizamos la operación para calcular el total 
    else:
        print("La fruta no está en el diccionario")     #Si la fruta no está en el diccionario imprimimos este mensaje 
        return None  

while True:             #Creamos un ciclo para 
    nombre = input("Introduzca el nombre de la fruta o 's' para terminar: ")     #Solicitamos al usuario que nos dé el nombre de la fruta y si quiere terminar el ciclo que introduzca una S
    if nombre == "s" or nombre == "S":          #Si introduce una S se detiene e ciclo, de no ser así el ciclo continua 
        break
    
    if nombre not in frutas:            #Si el nombre de la fruta no está en el diccionario
        print("La fruta no está en el diccionario") #Imprime este emensaje 
        continue
    
    cantidad = int(input("Introduce la cantidad vendida: "))    #Le pedimos al usuario que introduzaca la cantidad que vendió
    total = calcular(nombre, cantidad)  # Llamamos a la función calcular 
    if total is not None:               #Si la fruta se encuentra en el diccionario 
        print("El precio total de", cantidad, nombre, "es:", total) #Se imprime este mensaje con el nombre de la fruta, la cantidad y el total
