

#Variables
num = int(input("¿Cuál es el número?  "))
i = -1
j = 0

#Proceso
if num < 0 and num > -100: 
    while (i > -99):
        
        i = i - 2
        print(i)

elif num > 0 and num < 100:
    while (j < 100):
        j = j + 2
        print(j)

else:
    print("     No Válido")