from db_client import Base, engine  # Asegúrate de que db_client.py esté en el mismo nivel de directorio que este script o ajusta la ruta

# Crear todas las tablas definidas en los modelos
try:
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

