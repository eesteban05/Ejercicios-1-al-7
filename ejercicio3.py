

AñoActual = int(input("Ingrese el año actual: "))
AñoNacimiento = int(input("Ingrese su año de nacimiento: "))
Edad = ((AñoActual) - (AñoNacimiento))
if(Edad >= 0):
    print(f"Tu edad es {Edad} años !!!")
else:
    print("El año actual NO puede ser menor al año de nacimiento")