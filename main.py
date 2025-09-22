import operaciones

def calculadora():
    while True:
        print("\n=== Calculadora Modular ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("¡Gracias por usar la calculadora! 👋")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("Resultado:", operaciones.sumar(num1, num2))
        elif opcion == "2":
            print("Resultado:", operaciones.restar(num1, num2))
        elif opcion == "3":
            print("Resultado:", operaciones.multiplicar(num1, num2))
        elif opcion == "4":
            print("Resultado:", operaciones.dividir(num1, num2))
        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
