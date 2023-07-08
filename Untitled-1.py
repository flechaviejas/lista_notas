alumnos = []

# Agregar alumnos y notas al registro
def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    cantidad_notas = int(input("Ingrese la cantidad de notas del alumno: "))
    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
    alumno = {
        "nombre": nombre,
        "notas": notas
    }
    alumnos.append(alumno)
    print("Alumno agregado con éxito.")

# Mostrar el promedio de notas de un alumno
def promedio_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    for alumno in alumnos:
        if alumno["nombre"] == nombre:
            notas = alumno["notas"]
            promedio = sum(notas) / len(notas)
            print(f"El promedio de notas de {nombre} es: {promedio}")
            return
    print("No se encontró al alumno en el registro.")

# Mostrar el promedio de notas de todos los alumnos
def promedio_general():
    promedios = []
    for alumno in alumnos:
        notas = alumno["notas"]
        promedio = sum(notas) / len(notas)
        promedios.append(promedio)
    promedio_total = sum(promedios) / len(promedios)
    print(f"El promedio general de todos los alumnos es: {promedio_total}")

# Mostrar las notas más altas de todos los alumnos
def notas_mas_altas():
    notas_altas = []
    for alumno in alumnos:
        notas = alumno["notas"]
        nota_maxima = max(notas)
        notas_altas.append(nota_maxima)
    print(f"Las notas más altas de todos los alumnos son: {notas_altas}")

# Programa principal
while True:
    print("\n--- Registro de Notas ---")
    print("1. Agregar alumno")
    print("2. Calcular promedio de un alumno")
    print("3. Calcular promedio general")
    print("4. Mostrar notas más altas")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        agregar_alumno()
    elif opcion == 2:
        promedio_alumno()
    elif opcion == 3:
        promedio_general()
    elif opcion == 4:
        notas_mas_altas()
    elif opcion == 5:
        break
    else:
        print("Opción inválida. Intente nuevamente.")