import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='testdb'
)

cursor = conexion.cursor()

# Eliminar todos los usuarios
cursor.execute("DELETE FROM usuarios")

conexion.commit()

print(f"Usuarios eliminados: {cursor.rowcount}")

cursor.close()
conexion.close()