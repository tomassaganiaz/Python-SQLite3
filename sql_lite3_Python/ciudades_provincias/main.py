from db_manager import DBManager
from provincia import Provincia
from ciudad import Ciudad
from setup_data import cargar_datos

def main():
    db = DBManager()
    provincia = Provincia(db)
    ciudad = Ciudad(db)

    # Crear tablas
    provincia.crear_tabla()
    ciudad.crear_tabla()

    # Cargar datos iniciales
    cargar_datos(provincia, ciudad)

    # Consultas de prueba
    print("📍 Ciudades de Córdoba y Santa Fe:")
    for c in ciudad.consultar_por_provincias(["Córdoba", "Santa Fe"]):
        print(c)

    print("\n📋 Ordenadas por nombre en Buenos Aires:")
    for c in ciudad.consultar_ordenadas("Buenos Aires", "nombre"):
        print(c)

    # Actualizar nombres
    ciudad.actualizar_nombre(1, "La Plata Centro")
    ciudad.actualizar_nombre(2, "Mar del Plata Sur")

    # Eliminar ciudad y provincia
    ciudad.eliminar(2)
    provincia.eliminar("San Luis")

    db.close()

if __name__ == "__main__":
    main()
