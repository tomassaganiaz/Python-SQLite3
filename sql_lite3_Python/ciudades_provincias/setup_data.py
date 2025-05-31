def cargar_datos(provincia_obj, ciudad_obj):
    provincias = ["Buenos Aires", "Córdoba", "Santa Fe", "San Luis"]
    for p in provincias:
        provincia_obj.agregar(p)

    ciudades = {
        "Buenos Aires": [("1000", "C1000", "La Plata"), ("1001", "C1001", "Mar del Plata")],
        "Córdoba": [("2000", "C2000", "Córdoba Capital"), ("2001", "C2001", "Villa María")],
        "Santa Fe": [("3000", "C3000", "Rosario"), ("3001", "C3001", "Santa Fe")],
        "San Luis": [("4000", "C4000", "San Luis"), ("4001", "C4001", "Villa Mercedes")]
    }

    for provincia, lista_ciudades in ciudades.items():
        for cod_postal, cpa, nombre in lista_ciudades:
            ciudad_obj.agregar(cod_postal, cpa, nombre, provincia)
