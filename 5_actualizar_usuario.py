import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='testdb'
)

cursor = conexion.cursor()

# Datos nuevos para actualizar
nuevo_nombre = "Rodrigo Reyes Silva"
nuevo_email = "rodrigo.silva@example.com"
usuario_id = 1  # ID del usuario a actualizar

sql = """
UPDATE usuarios
SET nombre = %s,
    email = %s
WHERE id = %s
"""

valores = (nuevo_nombre, nuevo_email, usuario_id)

cursor.execute(sql, valores)
conexion.commit()

print(f"Filas actualizadas: {cursor.rowcount}")

cursor.close()
conexion.close()