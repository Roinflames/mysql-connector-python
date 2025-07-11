#
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='testdb'
)

cursor = conexion.cursor()

# Ejecutar la creación de la tabla
cursor.execute("""
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    rol ENUM('Administrador', 'MandosMedios', 'Gerencia') NOT NULL
);
""")

print("Tabla 'usuarios' creada o ya existía.")

# Confirmar cambios (aunque para CREATE no es obligatorio)
conexion.commit()

# Cerrar recursos
cursor.close()
conexion.close()