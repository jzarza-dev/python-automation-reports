import csv

def leer_datos():
    with open('data.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def mostrar_datos(datos):
    for d in datos:
        print(f"{d['id']} - {d['nombre']} - {d['edad']} - {d['carrera']}")

def generar_reporte(datos):
    total = len(datos)
    print(f"\nTotal de registros: {total}")

def menu():
    datos = leer_datos()
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar datos")
        print("2. Generar reporte")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_datos(datos)
        elif opcion == "2":
            generar_reporte(datos)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
