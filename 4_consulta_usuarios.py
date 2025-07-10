#
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='testdb'
)

cursor = conexion.cursor()

# Ejecutar una consulta
cursor.execute("SELECT * FROM usuarios")

# Obtener resultados
resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

# Cerrar recursos
cursor.close()
conexion.close()