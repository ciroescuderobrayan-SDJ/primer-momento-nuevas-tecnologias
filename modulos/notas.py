def registrar_nota(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    while True:
        try:
            nota = float(input("Nota del estudiante entre 0.0 y 5.0: "))

            if 0 <= nota <= 5:
                break

            print("La nota debe estar entre 0.0 y 5.0. Intente nuevamente.")
        except ValueError:
            print("Debes escribir un numero valido, ejemplo 4.5")


    estudiante = {
                "nombre": nombre,
                "nota": nota            
            }

    estudiantes.append(estudiante)
    print(f"Nota registrada exitosamente para {nombre}.")