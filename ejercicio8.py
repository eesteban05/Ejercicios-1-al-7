
#variables:
num1 = int(input("Ingresa un número:  "))
list1 = list(range(-99,0,2))
list2 = list(range(0,100,2))
list3 = list(range(-100,0))
list4 = list(range(1,101))

if num1 in list3:
    list1.reverse()
    print(list1)

elif num1 in list4:
      print(list2)

else:
    print("No Válido")