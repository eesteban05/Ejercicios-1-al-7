

#Variables
x = int(input("Ingresa tu número:   "))
lista1 = list()
y = x
z = 0

#Funciones
def sum(a):
    suma = 0
    for a in lista1:
        suma += a
    return suma 


if x > 0: #si es un número positivo, almacenar el dato y solicitar otro
    lista1.append(x)   
    while (y > 0):
        print(f"Haz ingresado los siguientes datos: {lista1}" )
        y = int(input("Ingresa OTRO número:  "))
        if y > 0:
            lista1.append(y)
        else:     #sumar los datos almacenados, promediar y presentar
            print("\n Los datos ingresados son: ")
            for i in lista1:
                z = z + 1

        
    print("- La lista tiene", z , "elementos")    
    print(f"- La suma de los elementos es: {sum(lista1)}")
    print(f"- El promedio es igual a: {sum(lista1) / z}")
    
    
else: 
       
    exit