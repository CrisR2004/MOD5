import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("presupuesto.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS articulos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT,
    monto REAL NOT NULL,
    fecha TEXT
)
""")
conn.commit()

# Función para registrar un artículo
def registrar_articulo():
    nombre = input("Ingrese el nombre del artículo: ")
    categoria = input("Ingrese la categoría del artículo: ")
    monto = float(input("Ingrese el monto del artículo: "))
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")

    cursor.execute("INSERT INTO articulos (nombre, categoria, monto, fecha) VALUES (?, ?, ?, ?)",
                   (nombre, categoria, monto, fecha))
    conn.commit()
    print("Artículo registrado exitosamente.\n")

# Función para buscar artículos
def buscar_articulo():
    nombre = input("Ingrese el nombre del artículo a buscar: ")
    cursor.execute("SELECT * FROM articulos WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cursor.fetchall()

    if resultados:
        print("\nResultados de la búsqueda:")
        for row in resultados:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Categoría: {row[2]}, Monto: ${row[3]}, Fecha: {row[4]}")
    else:
        print("No se encontraron artículos con ese nombre.\n")

# Función para editar un artículo
def editar_articulo():
    id_articulo = input("Ingrese el ID del artículo a editar: ")
    cursor.execute("SELECT * FROM articulos WHERE id = ?", (id_articulo,))
    articulo = cursor.fetchone()

    if articulo:
        nombre = input(f"Ingrese el nuevo nombre del artículo (anterior: {articulo[1]}): ")
        categoria = input(f"Ingrese la nueva categoría (anterior: {articulo[2]}): ")
        monto = float(input(f"Ingrese el nuevo monto (anterior: {articulo[3]}): "))
        fecha = input(f"Ingrese la nueva fecha (anterior: {articulo[4]}): ")

        cursor.execute("UPDATE articulos SET nombre = ?, categoria = ?, monto = ?, fecha = ? WHERE id = ?",
                       (nombre, categoria, monto, fecha, id_articulo))
        conn.commit()
        print("Artículo actualizado exitosamente.\n")
    else:
        print("No se encontró un artículo con ese ID.\n")

# Función para eliminar un artículo
def eliminar_articulo():
    id_articulo = input("Ingrese el ID del artículo a eliminar: ")
    cursor.execute("SELECT * FROM articulos WHERE id = ?", (id_articulo,))
    articulo = cursor.fetchone()

    if articulo:
        cursor.execute("DELETE FROM articulos WHERE id = ?", (id_articulo,))
        conn.commit()
        print("Artículo eliminado exitosamente.\n")
    else:
        print("No se encontró un artículo con ese ID.\n")

# Función para ver todos los artículos
def ver_articulos():
    cursor.execute("SELECT * FROM articulos")
    articulos = cursor.fetchall()

    if articulos:
        print("\nLista de todos los artículos:")
        for row in articulos:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Categoría: {row[2]}, Monto: ${row[3]}, Fecha: {row[4]}")
    else:
        print("No hay artículos registrados.\n")

# Función para mostrar el menú
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("a) Registrar un nuevo artículo")
    print("b) Buscar un artículo")
    print("c) Editar un artículo existente")
    print("d) Eliminar un artículo")
    print("e) Ver todos los artículos")
    print("f) Salir")

# Función principal para ejecutar el programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ").lower()

        if opcion == 'a':
            registrar_articulo()
        elif opcion == 'b':
            buscar_articulo()
        elif opcion == 'c':
            editar_articulo()
        elif opcion == 'd':
            eliminar_articulo()
        elif opcion == 'e':
            ver_articulos()
        elif opcion == 'f':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

    # Cerrar la conexión al salir
    conn.close()

# Ejecutar el programa
main()
