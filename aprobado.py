#Ejercicio que determine si un estudiante esta arpobado o no 
# Autor :Richard Victorio Tito


def determinaraprobado(promedio):
    if promedio >=11:
        resultado ="Aprobado"
    else:
        resultado="Desaprobado"
    return resultado
promedio= int(input("Promedio:"))
print(determinaraprobado(promedio))


