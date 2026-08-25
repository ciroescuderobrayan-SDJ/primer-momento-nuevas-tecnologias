def calcular_promedio(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados todavia.")
        return

    total = sum(estudiante["nota"] for estudiante in estudiantes)
    promedio = total / len(estudiantes)

    print(f"\nPromedio general del grupo: {promedio:.2f}")

    for estudiante in estudiantes:
        estado = "Aprobado" if estudiante["nota"] >= 3.0 else "Reprobado"
        print(f"- {estudiante['nombre']}: {estudiante['nota']} ({estado})")
