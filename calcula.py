def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return a ** 0.5

class Calculadora:
    def __init__(self):
        self.historial = []
    
    def calcular(self, operacion, a, b=None):
        if operacion == "suma":
            resultado = sumar(a, b)
        elif operacion == "resta":
            resultado = restar(a, b)
        elif operacion == "multiplicacion":
            resultado = multiplicar(a, b)
        elif operacion == "division":
            resultado = dividir(a, b)
        elif operacion == "potencia":
            resultado = potencia(a, b)
        elif operacion == "raiz":
            resultado = raiz_cuadrada(a)
        else:
            raise ValueError("Operación no válida")
        
        self.historial.append(f"{operacion}: {resultado}")
        return resultado
    
    def ver_historial(self):
        return self.historial
    
    def limpiar_historial(self):
        self.historial = []

def main():
    calc = Calculadora()
    
    print("Calculadora Básica")
    print("Operaciones disponibles: suma, resta, multiplicacion, division, potencia, raiz")
    
    while True:
        try:
            operacion = input("\nIngresa la operación (o 'salir' para terminar): ").lower()
            
            if operacion == 'salir':
                break
            
            if operacion == 'historial':
                print("Historial:", calc.ver_historial())
                continue
                
            if operacion == 'limpiar':
                calc.limpiar_historial()
                print("Historial limpiado")
                continue
            
            if operacion == "raiz":
                a = float(input("Ingresa el número: "))
                resultado = calc.calcular(operacion, a)
            else:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                resultado = calc.calcular(operacion, a, b)
            
            print(f"Resultado: {resultado}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()