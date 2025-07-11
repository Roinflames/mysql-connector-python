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
resultados = cursor.fetchall() # Obtener todas las filas
# resultados = cursor.fetchone() # Obtener una sola fila
# resultados = cursor.fetchmany(5) # Obtener un número específico de filas

for fila in resultados:
    print(fila)

# Cerrar recursos
cursor.close()
conexion.close()