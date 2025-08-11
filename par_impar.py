def es_par(numero):
    return numero % 2 == 0

def es_impar(numero):
    return numero % 2 != 0

def comprobar_paridad(numero):
    if es_par(numero):
        return f"{numero} es par"
    else:
        return f"{numero} es impar"

if __name__ == "__main__":
    try:
        num = int(input("Ingresa un número: "))
        resultado = comprobar_paridad(num)
        print(resultado)
    except ValueError:
        print("Por favor, ingresa un número válido")