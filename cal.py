def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def main():
    print('Calculadora Básica')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    
    while True:
        try:
            choice = input('\nSelecciona una opción (1-4) o "q" para salir: ')
            
            if choice.lower() == 'q':
                break
                
            if choice not in ['1', '2', '3', '4']:
                print('Opción inválida')
                continue
                
            num1 = float(input('Ingresa el primer número: '))
            num2 = float(input('Ingresa el segundo número: '))
            
            if choice == '1':
                result = add(num1, num2)
                print(f'Resultado: {num1} + {num2} = {result}')
            elif choice == '2':
                result = subtract(num1, num2)
                print(f'Resultado: {num1} - {num2} = {result}')
            elif choice == '3':
                result = multiply(num1, num2)
                print(f'Resultado: {num1} * {num2} = {result}')
            elif choice == '4':
                result = divide(num1, num2)
                print(f'Resultado: {num1} / {num2} = {result}')
                
        except ValueError as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'Error inesperado: {e}')

if __name__ == '__main__':
    main()
