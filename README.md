# mysql-connector-python
Requisitos:
## Instalación del motor de base de datos MySQL en Windows
- Ve a: https://dev.mysql.com/downloads/installer/
- Descarga MySQL Installer for Windows (puedes elegir la versión pequeña: web installer).
- Durante la instalación, selecciona:
- MySQL Server
- Opcional: MySQL Workbench (interfaz gráfica)
- Sigue los pasos y anota la contraseña de root.
## Verifica que el servidor esté corriendo
```
mysql -u root -p
```
### Mostrar bases de datos creadas
```
SHOW DATABASES;
```
## Crear una base de datos
```
python 2
```
## Conectar desde Python (opcional)
```
python 1_conexion.py
```
## Iniciar y detener el servicio manualmente (si lo necesitas)
```
net start mysql
net stop mysql
```
## Configuración del ambiente virtual
```
pipenv install mysql-connector-python bcrypt python-dotenv
pipenv shell
```
# Ventajas de esta estructura
| Ventaja            | Por qué es útil                                                                         |
| ------------------ | --------------------------------------------------------------------------------------- |
| **Modularidad**    | Puedes testear cada módulo por separado y reutilizar funciones.                         |
| **Seguridad**      | Contraseñas hasheadas con `bcrypt`, credenciales fuera del código duro.                 |
| **Escalabilidad**  | Agregar nuevos roles u operaciones ahora es añadir funciones, no tocar el menú gigante. |
| **Mantenibilidad** | Si cambias la forma de conectar, solo editas `conexion.py`.                             |
