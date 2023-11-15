
# CODE:38
# IMPORTANTE: NO borrar los comentarios

import csv


def desafio():
    print('Ejercicio de archivos')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Al final de esta función retornar (return) el stock total de tornillos
    # Comenzar aquí, recuerde el identado dentro de esta funcion
    stock_tornillos_total = 0

    try:
        
        with open(archivo) as csvfile:
            
            reader = csv.DictReader(csvfile)

           
            for row in reader:
                
                stock_tornillos_fila = int(row['tornillos'])

                
                stock_tornillos_total += stock_tornillos_fila

    except FileNotFoundError:
        print("El archivo 'stock.csv' no se encuentra en el directorio.")
        return None

    
    return stock_tornillos_total

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio()
