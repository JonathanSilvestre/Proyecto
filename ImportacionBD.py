import csv

def leer_csv(nombre_archivo):
    productos = []
    with open(nombre_archivo, mode='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)  # Saltar la cabecera
        for lines in csvFile:
            productos.append(lines)
    return productos

