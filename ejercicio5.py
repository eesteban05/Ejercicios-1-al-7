accion1 = input("¿Quieres convertir °C a °F y °K?  ")

if((accion1) == "si"):
    C = float(input("Ingresa el valor de °C: "))
    F = ((C) * 1.8 + 32)
    K = ((C) + 273.15)
    print(f"El valor en °F es = {F}°F")
    print(f"El valor en °K es = {K}°K")
elif((accion1) == "no"):
    accion2 = input("¿Quieres convertir °F a C y K?")
    if((accion2) == "si"):
        F2 = float(input("Ingresa el valor de °F: "))
        C2 = (((F2) - 32) * (5/9))
        K2 = (((F2) - 32) * (5/9) + 273.15)
        print(f"El valor en °C es = {C2}°C")
        print(f"El valor en °K es = {K2}°K")
    else:
        exit
else:
    exit
