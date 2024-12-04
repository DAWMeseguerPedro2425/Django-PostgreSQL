import os
#Metedo creado por IA para eliminar las migraciones de la base de datos y solucionar el problema de las migraciones
def clean_migrations():
    # Obtener el directorio actual
    project_dir = os.getcwd()
    
    # Recorrer todos los directorios
    for root, dirs, files in os.walk(project_dir):
        # Buscar carpetas de migraciones
        if 'migrations' in dirs:
            migrations_dir = os.path.join(root, 'migrations')
            # Recorrer archivos en la carpeta de migraciones
            for filename in os.listdir(migrations_dir):
                # No eliminar __init__.py
                if filename != '__init__.py' and filename.endswith('.py'):
                    file_path = os.path.join(migrations_dir, filename)
                    try:
                        os.remove(file_path)
                        print(f"Eliminado: {file_path}")
                    except Exception as e:
                        print(f"Error al eliminar {file_path}: {e}")

    # Eliminar base de datos SQLite si existe
    if os.path.exists('db.sqlite3'):
        try:
            os.remove('db.sqlite3')
            print("Base de datos SQLite eliminada")
        except Exception as e:
            print(f"Error al eliminar la base de datos: {e}")

if __name__ == "__main__":
    clean_migrations()
