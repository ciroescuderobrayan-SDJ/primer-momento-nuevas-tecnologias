# Sistema de Registro de Notas

Aplicación de consola en Python que permite registrar estudiantes con su nota y calcular el promedio del grupo, indicando si cada estudiante aprobó o reprobó.

## Funcionalidades

- **Registrar nota**: pide el nombre del estudiante y una nota entre 0.0 y 5.0, y la guarda.
- **Ver promedio**: muestra el promedio general del grupo y el estado (Aprobado/Reprobado) de cada estudiante registrado.
- **Salir**: termina el programa.

## Cómo ejecutarlo

Requiere Python 3.

```
python main.py
```

## Estructura del proyecto

```
main.py               # punto de entrada, menu principal e interactivo
modulos/notas.py      # logica para registrar notas
modulos/promedio.py   # calculo de promedio y estado aprobado/reprobado
```

## Autor

Brayan Esneider Ciro Escudero
