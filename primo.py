def es_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

def main():
    try:
        num = int(input("Ingresa un número: "))
        if es_primo(num):
            print(f"{num} es primo")
        else:
            print(f"{num} no es primo")
    except ValueError:
        print("Por favor, ingresa un número válido")

if __name__ == "__main__":
    main()