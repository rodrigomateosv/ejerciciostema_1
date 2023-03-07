
def formatear_cadena_corrupta(cadena_corrupta):
    cadena_volteada = cadena_corrupta[::-1][::-1]
    lista = cadena_volteada.split()
    nota = lista[1]
    lista_1 = lista[:-1]
    nombre_completo = " ".join(lista_1)
    mensaje_formateado = f"{nombre_completo} ha sacado un {nota} de nota."
    return mensaje_formateado

cadena_corrupta = "zeréP nauJ,01"
mensaje_formateado = formatear_cadena_corrupta(cadena_corrupta)
print(mensaje_formateado)

