import re



vuelos = {
    "AV-102":{
        "origen":"Lima",
        "destino":"Bogota",
        "asientos": ["A1","A2","A3","B1","B2","C3","C5","D1"],
        "horarios": (15,30)
    },
    "AV-103":{
        "origen":"Bogota",
        "destino":"Toronto",
        "asientos": ["A4","A6","B3","B5","C2"],
        "horarios": (12,00)
    },
    "AV-140":{
        "origen":"São Paulo",
        "destino":"Bogota",
        "asientos": ["A1","A4","B7","B8","B9"],
        "horarios": (23,00)
    },
    "AV-203":{
        "origen":"Medellín",
        "destino":"Cartagena",
        "asientos": ["A1","A5","B3","C1","C9"],
        "horarios": (18,00)
    },
    "AV-350":{
        "origen":"Bogota",
        "destino":"Barcelona",
        "asientos": ["A4","A5","B3","C8","C9"],
        "horarios": (12,10)
    }

}



def codigo_vuelo_valido(codigo):
    patron = r"^[A-Z]{2}-\d{3}$"
    return re.match(patron, codigo) is not None

def horario_valido(horario):
    hora, minutos = horario
    return 0 <= hora <= 23 and 0 <= minutos <= 59

def formato_asiento_valido(asiento):
    patron = r"^[A-Z]\d+$"
    return re.match(patron, asiento) is not None

def verificar_disponibilidad(vuelo, asiento):
    return asiento in vuelo["asientos"]


def validacion_reserva(vuelo, asiento):
    if not formato_asiento_valido(asiento):
        print(f"El formato del asiento {asiento} no es válido para el vuelo {vuelo['codigo_vuelo']}")
        return False
    if "reservado" in vuelo and asiento in vuelo["reservado"]:
        print(f"El asiento {asiento} ya está reservado")
        return False
    if asiento in vuelo["asientos"]:
        vuelo["asientos"].remove(asiento)
        if "reservado" not in vuelo:
            vuelo["reservado"] = []
        vuelo["reservado"].append(asiento)
        print(f"El asiento {asiento} fue reservado exitosamente en el vuelo {vuelo['codigo_vuelo']}")
        return True
    else:
        print(f"El asiento {asiento} no está disponible")
        return False

def calcular_puestos_ocupados(vuelo):
    disponibles = len(vuelo["asientos"])
    reservados = len(vuelo.get("reservados", []))
    total_asientos = disponibles + reservados
    if total_asientos > 0:
        porcentaje = (reservados / total_asientos) * 100
        return f"{porcentaje:.2f}%"
    return "0%"

