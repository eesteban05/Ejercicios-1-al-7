#variables:
nivel = float(input("¿Cuál es el nivel de agua en la cisterna?  ")) 
#proceso:
if(nivel < 0 ):
    print("Hay FUGA en la cisterna")
elif(nivel == 0):
    print("Encender bomba de agua")
elif(nivel > 0 and nivel < 3 ):
    print("Acelerar bomba de agua")
elif(nivel >= 3 and nivel < 5):
    print("¡Bomba trabajando!")
elif(nivel >= 5 and nivel < 6):
    print("Desacelerar bomba de agua")
elif(nivel == 6):
    print("Apagar bomba de agua")
else:
    print("¡¡¡Desbordamiento de agua en Cisterna!!!")
