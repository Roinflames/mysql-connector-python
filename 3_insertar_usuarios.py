#
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='testdb'
)

cursor = conexion.cursor()

# Insertar un usuario
sql = """
INSERT INTO usuarios (nombre, email, contraseña, activo) 
VALUES (%s, %s, %s, %s)
"""

valores = ("Rodrigo Reyes", "rodrigo@example.com", "mi_contraseña_segura", True)

cursor.execute(sql, valores)

# Confirmar cambios
conexion.commit()

print(f"Usuario insertado con ID: {cursor.lastrowid}")

# Cerrar recursos
cursor.close()
conexion.close()