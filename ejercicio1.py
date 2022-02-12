calificacion1 = float(input("Ingrese calificación del primer parcial: "))
calificacion2 = float(input("Ingrese calificación del segundo parcial: "))
calificacion3 = float(input("Ingrese calificación del tercer parcial: "))
promedio = (calificacion1 + calificacion2 + calificacion3) / 3
print(f"El promedio del estudioante es = {promedio}")
if(promedio >= 6):
    print("El estudiante está APROBADO")
    print(" ¡¡¡¡F E L I C I D A D E S!!!!")
else:
    print("El estudiante está REPROBADO")
    print(" Intenta de nuevo en el siguiente año.... =(")