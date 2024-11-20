def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def main():
    print("Calculadora Básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    try:
        operacion = int(input("Selecciona una operación (1/2/3/4): "))
        if operacion not in [1, 2, 3, 4]:
            print("Operación no válida")
            return

        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if operacion == 1:
            print(f"Resultado: {suma(a, b)}")
        elif operacion == 2:
            print(f"Resultado: {resta(a, b)}")
        elif operacion == 3:
            print(f"Resultado: {multiplicacion(a, b)}")
        elif operacion == 4:
            print(f"Resultado: {division(a, b)}")

    except ValueError:
        print("Entrada no válida. Por favor, ingresa números válidos.")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")

if __name__ == "__main__":
    main()