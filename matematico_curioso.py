# Trabajo práctico de programación perteneciente a:
# María Belén FLORES, Noemi Elizabeth PAEZ y Leandro Raul VALINOTTI

from random import randint # Importamos una función de la librería random
semilla=randint(20,100)    # Generamos una número entero aleatorio entre 20 y 100
cuenta=0                   # Ponemos el contador de cantidad de números en las erie
mayor=0                    # Definimos e inicializamos una variable para calcular el mayor
print("Los números de la serie son: ","\n")
while(semilla!=1):         # Chequeamos que la semilla no haya llegado a 1
    if(semilla>mayor):     # Comparamos si semilla es el mayor para luego almacenarlo
        mayor=semilla
    if(semilla%2==0):      # Chequeamos si semilla es par y generamos la lógica
        semilla=int(semilla/2)
    else:
        semilla=(semilla*3)+1
    cuenta+=1              # Contamos la cantidad de datos generados en la lista
# Imprimimos los resultados
    print(semilla, end=" ")
print("\n")
print("La cantidad de números de la serie es: ",cuenta)
print()
print("El número mayor de la serie es: ",mayor)
    
