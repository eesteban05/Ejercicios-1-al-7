num = int(input("¿cuál es el número?   "))

if num < 0 and num > -100: 
    for i in range(-1 , -101 , -2):
        print(i)

elif num > 0 and num < 100:
    for i in range(0 , 101 , 2):
        print(i)

else:
    print("     No Válido")