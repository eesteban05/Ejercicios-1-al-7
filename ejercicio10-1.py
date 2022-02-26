
x = int(input("Ingresa tu número:   "))
lista1 = list()
y = x
n = 0




def sum(a):
    suma = 0
    z = len(lista1)
    for a in lista1:
        suma += a

    return print( f"- La suma de los elementos es: {suma}\n- El promedio de sus elementos es: {suma / z} ")



if x > 0: #si es un número positivo, almacenar el dato y solicitar otro
    lista1.append(x)   
    while (y > 0):
        print(f"Haz ingresado los siguientes datos: {lista1}" )
        y = int(input("Ingresa OTRO número:  "))
        if y > 0:
            lista1.append(y)
        else:
    
            for i in lista1:

                n = n + 1
        
    print("\nLos datos ingresados son: ")
    print("- La lista tiene", n , "elementos")    
    sum(lista1)
    

    
else: #sumar los datos almacenados, promediar y presentar
    
    
    
    
    exit