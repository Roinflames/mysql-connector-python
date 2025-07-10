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
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);
""")

print("Tabla 'usuarios' creada o ya existía.")

# Confirmar cambios (aunque para CREATE no es obligatorio)
conexion.commit()

# Cerrar recursos
cursor.close()
conexion.close()