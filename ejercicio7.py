
from sre_constants import RANGE


nivel = float(input("¿Cuál es el nivel de agua en la cisterna?  ")) 
nivel0  = list((1,2))
nivel1 = list((3,4))


if(nivel < 0):
    print("Hay FUGA en la cisterna")
elif(nivel == 0):
    print("Encender bomba de agua")
elif(nivel == nivel0):
    print("Acelerar bomba de agua")
elif(nivel == nivel1):
    print("¡Bomba trabajando!")
elif(nivel == range(5,6,1)):
    print("Desacelerar bomba de agua")
elif(nivel == 6):
    print("Apagar bomba de agua")
else:
    print("¡¡¡Desbordamiento de agua en Cisterna!!!")
