from modulos.notas import registrar_nota
from modulos.promedio import calcular_promedio


def mostrar_menu():
    print("\n--- SISTEMA DE REGISTRO DE NOTAS ---")
    print("1. Registrar nota")
    print("2. Ver promedio")
    print("3. Salir")


def ejecutar_programa():
    estudiantes = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_nota(estudiantes)

        elif opcion == "2":
            calcular_promedio(estudiantes)

        elif opcion == "3":
            print("Programa terminado.")
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()
