from datetime import datetime


def validarData(dataStr):
    try:
        datetime.strptime(dataStr, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False


def adicionarEvento(listaEventos, nome, data, local, categoria):
    if not nome.strip():
        return False

    if not validarData(data):
        return False

    if not local.strip():
        return False

    if not categoria.strip():
        return False

    evento = {
        "id": len(listaEventos) + 1,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria
    }

    listaEventos.append(evento)

    return True


listaEventos = []


adicionarEvento(
    listaEventos,
    "Workshop de Python",
    "2026-09-15",
    "Laboratorio 1",
    "Tecnologia"
)


def listarEventos(listaEventos):
    return listaEventos

print(listarEventos(listaEventos))

def procurarEventoPorNome(listaEventos, nome):
    resultados = []

    for evento in listaEventos:
        if nome.lower() in evento["nome"].lower():
            resultados.append(evento)

    return resultados

print(procurarEventoPorNome(listaEventos, "Python"))

def deletarEvento(listaEventos, id):
    for evento in listaEventos:
        if evento["id"] == id:
            listaEventos.remove(evento)
            return True

    return False

print(deletarEvento(listaEventos, 1))
print(listaEventos)
