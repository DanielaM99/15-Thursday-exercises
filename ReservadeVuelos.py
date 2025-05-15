import re
import datetime


vuelos = {
    "AV-102": {
        "origen": "Lima",
        "destino": "Bogota",
        "asientos": ["A1", "A2", "A3", "B1", "B2", "C3", "C5", "D1"],
        "horarios": (15, 30),
        "reserva": []
    },
    "AV-103": {
        "origen": "Bogota",
        "destino": "Toronto",
        "asientos": ["A4", "A6", "B3", "B5", "C2"],
        "horarios": (12, 00),
        "reserva": []
    },
    "AV-140": {
        "origen": "São Paulo",
        "destino": "Bogota",
        "asientos": ["A1", "A4", "B7", "B8", "B9"],
        "horarios": (23, 00),
        "reserva": []
    },
    "AV-203": {
        "origen": "Medellín",
        "destino": "Cartagena",
        "asientos": ["A1", "A5", "B3", "C1", "C9"],
        "horarios": (18, 00),
        "reserva": []
    },
    "AV-350": {
        "origen": "Bogota",
        "destino": "Barcelona",
        "asientos": ["A4", "A5", "B3", "C8", "C9"],
        "horarios": (12, 10),
        "reserva": []
    }
}


def codigo_vuelo_valido(codigo):
    patron = r"^[A-Z]{2}-\d{3}$"
    return re.match(patron, codigo) is not None


def horario_valido(horario):
    hora, minutos = horario
    return 0 <= hora <= 23 and 0 <= minutos <= 59


def asiento_valido(asiento):
    patron = r"^[A-Z]\d+$"
    return re.match(patron, asiento) is not None


def verificar_disponibilidad(vuelo, asiento):
    return asiento in vuelo["asientos"]


def reservar_asiento(codigo_vuelo, asiento):
    if codigo_vuelo not in vuelos:
        print(f"El código de vuelo {codigo_vuelo} no existe")
        return False

    vuelo = vuelos[codigo_vuelo]

    if not asiento_valido(asiento):
        print(f"El formato del asiento {asiento} no es válido")
        return False

    if asiento in vuelo["reserva"]:
        print(f"El asiento {asiento} ya está reservado")
        return False

    if asiento in vuelo["asientos"]:
        vuelo["asientos"].remove(asiento)
        vuelo["reserva"].append(asiento)
        print(f"El asiento {asiento} fue reservado exitosamente ")
        return True
    else:
        print(f"El asiento {asiento} no está disponible")
        return False


def calcular_porcentaje_ocupacion(codigo_vuelo):
    if codigo_vuelo not in vuelos:
        print(f"El código {codigo_vuelo} de vuelo no existe.")
        return "N/A"
    vuelo = vuelos[codigo_vuelo]
    total_asientos = len(vuelo["asientos"]) + len(vuelo.get("reserva", []))
    if total_asientos > 0:
        porcentaje = (len(vuelo.get("reserva", [])) / total_asientos) * 100
        return f"{porcentaje:.2f}%"
    return "0.00%"


def reserva_vuelo():
    while True:
        print("\n-----MENÚ DE RESERVAS-----")
        print("1. Ver vuelos disponibles y reservar un asiento")
        print("2. Generar reporte de vuelos ordenados por horario")
        print("3. Salir del menú de reservas")
        opcion = input("Seleccione una opción: ").strip()
        

        if opcion == "1":
            print("\n-----RESERVA-----")
            print("Vuelos disponibles: ")
            for codigo, detalles in vuelos.items():
                hora, minutos = detalles["horarios"]
                print(f"{codigo}: {detalles['origen']} -> {detalles['destino']} ({hora:02d}:{minutos:02d})")

            codigo_vuelo_deseado = input("Ingrese el código del vuelo que desea reservar: ").strip().upper()

            if codigo_vuelo_deseado not in vuelos:
                print(f"El código {codigo_vuelo_deseado} del vuelo no es válido")
                continue

            vuelo = vuelos[codigo_vuelo_deseado]
            print(f"\nAsientos disponibles para el vuelo {codigo_vuelo_deseado} ({vuelo['origen']} -> {vuelo['destino']}):")
            print(vuelo["asientos"])

            asiento_deseado = input("Ingrese el asiento que desea reservar: ").strip().upper()

            if reservar_asiento(codigo_vuelo_deseado, asiento_deseado):
                porcentaje_ocupacion = calcular_porcentaje_ocupacion(codigo_vuelo_deseado)
                print(f"El porcentaje de ocupación para el vuelo {codigo_vuelo_deseado}: {porcentaje_ocupacion}")
            else:
                print("La reservación no fue exitosa, por favor verifica la información ingresada")
        elif opcion == "2":
            generar_reporte_vuelos()
        elif opcion == "3":
            print("Saliendo del menú")
            break  
        else:
            print("Invalido, por favor seleccione 1, 2 o 3")


def generar_reporte_vuelos(nombre_archivo="reporte.txt"):
    vuelos_ordenados = sorted(vuelos.items(), key=lambda item: item[1]["horarios"])

    with open(nombre_archivo, "w") as archivo:
        archivo.write("--- REPORTE DE VUELOS ---\n\n")
        for codigo, detalles in vuelos_ordenados:
            hora, minutos = detalles["horarios"]
            archivo.write(f"Código de Vuelo: {codigo}\n")
            archivo.write(f"  Origen: {detalles['origen']}\n")
            archivo.write(f"  Destino: {detalles['destino']}\n")
            archivo.write(f"  Horario: {hora:02d}:{minutos:02d}\n")
            archivo.write(f"  Asientos Disponibles: {', '.join(detalles['asientos'])}\n")
            archivo.write(f"  Asientos Reservados: {', '.join(detalles.get('reserva', []))}\n")
            archivo.write(f"  Porcentaje de Ocupación: {calcular_porcentaje_ocupacion(codigo)}%\n")
            archivo.write("-" * 30 + "\n")

    print(f"El reporte de vuelos ha sido generado en el archivo '{nombre_archivo}'.")


if __name__ == "__main__":
    reserva_vuelo()  
