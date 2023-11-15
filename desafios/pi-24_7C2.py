
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
    cvsfile = open(archivo, 'r')
    busca_deptos = list(csv.DictReader(cvsfile))

    deptos_2_amb = 0
    deptos_3_amb = 0

    cantidad_deptos = len(busca_deptos)

    for departamento in range(cantidad_deptos):
        row = busca_deptos[departamento]
        try: 
            cantidad_ambientes = int(row.get('ambientes'))

            if cantidad_ambientes == 2:
                deptos_2_amb += 1
            elif cantidad_ambientes == 3:
                deptos_3_amb += 1
        except:
            continue
    
    print('Sobre', cantidad_deptos, 'propiedades: ')
    print('Hay', deptos_2_amb, 'deptaramentos de 2 ambientes')
    print('Hay', deptos_3_amb, 'deptaramentos de 3 ambientes')
    cvsfile.close()  

    if ambientes == "2_ambientes":
        return deptos_2_amb
    else:
        return deptos_3_amb  

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio("2_ambientes")
