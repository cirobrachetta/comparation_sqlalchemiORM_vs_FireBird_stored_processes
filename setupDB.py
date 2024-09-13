import mysql.connector
from mysql.connector import errorcode

try:
    # Conectarse al servidor MySQL usando un usuario con permisos suficientes
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",  # Usa un usuario que tenga permisos para crear bases de datos y usuarios
        password="tu_contraseña_root"  # La contraseña del usuario root
    )

    cursor = conexion.cursor()

    # Crear base de datos
    cursor.execute("CREATE DATABASE IF NOT EXISTS example_db")

    # Usar la base de datos creada
    cursor.execute("USE example_db")

    # Crear usuario y asignar privilegios
    cursor.execute("""
    CREATE USER IF NOT EXISTS 'tu_usuario'@'localhost' IDENTIFIED BY 'tu_contraseña';
    GRANT ALL PRIVILEGES ON example_db.* TO 'tu_usuario'@'localhost';
    FLUSH PRIVILEGES;
    """)

    # Crear tabla de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        email VARCHAR(255)
    )
    """)

    # Crear procedimiento almacenado
    cursor.execute("""
    DELIMITER //

    CREATE PROCEDURE IF NOT EXISTS agregar_usuario(IN nombre VARCHAR(255), IN email VARCHAR(255))
    BEGIN
        INSERT INTO usuarios (nombre, email) VALUES (nombre, email);
    END //

    DELIMITER ;
    """)

    print("Base de datos, usuario, y procedimientos creados exitosamente.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conexion.close()
