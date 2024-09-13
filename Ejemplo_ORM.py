import sqlite3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

# Configuración de la base de datos
DATABASE_URL = "sqlite:///exampleORM.db"

# Crear una conexión a la base de datos
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definir el modelo
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Función para agregar un usuario usando el ORM
def agregar_usuario(nombre, email):
    try:
        # Medir el tiempo de inicio
        start_time = time.time()

        # Crear una instancia de Usuario
        nuevo_usuario = Usuario(nombre=nombre, email=email)
        session.add(nuevo_usuario)
        session.commit()

        # Medir el tiempo de fin
        end_time = time.time()

        # Calcular y mostrar el tiempo de ejecución
        execution_time = end_time - start_time
        print(f"Usuario agregado exitosamente. Tiempo de ejecución: {execution_time:.6f} segundos.")

    except Exception as e:
        print(f"Error al agregar usuario: {e}")

# Función para consultar usuarios
def consultar_usuarios():
    try:
        start_time = time.time()
        
        usuarios = session.query(Usuario).all()
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Consulta de usuarios completada. Tiempo de ejecución: {execution_time:.6f} segundos.")
        
        return usuarios

    except Exception as e:
        print(f"Error al consultar usuarios: {e}")
        return []

# Agregar un usuario
agregar_usuario('Ciro', 'ciro@example.com')

# Consultar y mostrar los usuarios
usuarios = consultar_usuarios()
for usuario in usuarios:
    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Email: {usuario.email}")

# Cerrar la sesión
session.close()