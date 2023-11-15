
# CODE:39
# IMPORTANTE: NO borrar los comentarios

import csv


def desafio(ambientes):
    print('Ejercicios con archivos CSV complejos')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Según el valor ingresado en "ambientes" está función deberá
    # retornar (return):
    # 1) si ambientes == "2_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 2 ambientes
    # 2) si ambientes == "3_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 3 ambientes

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # Puede evitar que el programa explote utilizando "try except".

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open(archivo, 'r')
    busca_deptos = list(csv.DictReader(csvfile))

    suma_2ambientes = 0
    suma_3ambientes = 0
    
    cantidad_deptos = len(busca_deptos)
    
    for departamento in range(cantidad_deptos):
        row = busca_deptos[departamento]
        try:
            cantidad_ambientes = int(row.get('ambientes'))
            
            if cantidad_ambientes == 2:
                suma_2ambientes += 1
            elif cantidad_ambientes == 3:
                suma_3ambientes += 1
        except:
            continue
            
    print('Sobre', cantidad_deptos,'propiedades:')
    print('Hay', suma_2ambientes, 'departamentos de 2 ambientes.')
    print('Hay', suma_3ambientes, 'departamentos de 3 ambientes.')
    csvfile.close()

    if ambientes == "2_ambientes":
        return suma_2ambientes
    else:
        return suma_3ambientes


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio("3_ambientes")
