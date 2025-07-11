# menu.py
from auth import login
from bd_ops import crear_base_datos, eliminar_base_datos, ver_bases_datos
from tabla_ops import crear_tabla, eliminar_tabla
from usuario_ops import insertar_usuario, consultar_usuarios

def mostrar_menu(rol: str):
    while True:
        print("""
=== Menú Principal ===
1. Crear base de datos
2. Eliminar base de datos
3. Ver bases de datos
4. Crear tabla usuarios
5. Eliminar tabla usuarios
6. Insertar usuario
7. Consultar usuarios
0. Salir
""")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if rol != "Gerencia":
                print("No tiene permisos para crear bases de datos.")
                continue
            crear_base_datos(input("Nombre BD: "))

        elif opcion == "2":
            if rol != "Gerencia":
                print("No tiene permisos para eliminar bases de datos.")
                continue
            eliminar_base_datos(input("Nombre BD: "))

        elif opcion == "3":
            ver_bases_datos()

        elif opcion == "4":
            crear_tabla()

        elif opcion == "5":
            eliminar_tabla()

        elif opcion == "6":
            insertar_usuario()

        elif opcion == "7":
            consultar_usuarios()

        elif opcion == "0":
            print("Saliendo… ¡hasta luego! 🐍")
            break
        else:
            print("Opción no válida.")

def main():
    rol = login()
    if rol:
        mostrar_menu(rol)

if __name__ == "__main__":
    main()
