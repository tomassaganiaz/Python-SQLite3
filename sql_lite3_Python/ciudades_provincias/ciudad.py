class Ciudad:
    def __init__(self, db):
        self.db = db

    def crear_tabla(self):
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS ciudades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cod_postal TEXT NOT NULL,
                cpa TEXT NOT NULL,
                nombre TEXT NOT NULL,
                id_provincia INTEGER,
                FOREIGN KEY (id_provincia) REFERENCES provincias(id) ON DELETE CASCADE
            );
        ''')

    def agregar(self, cod_postal, cpa, nombre_ciudad, nombre_provincia):
        provincia = self.db.fetchone("SELECT id FROM provincias WHERE nombre = ?", (nombre_provincia,))
        if provincia:
            id_provincia = provincia[0]
            self.db.execute(
                "INSERT INTO ciudades (cod_postal, cpa, nombre, id_provincia) VALUES (?, ?, ?, ?)",
                (cod_postal, cpa, nombre_ciudad, id_provincia)
            )
        else:
            print(f"Provincia '{nombre_provincia}' no encontrada.")

    def actualizar_nombre(self, id_ciudad, nuevo_nombre):
        self.db.execute("UPDATE ciudades SET nombre = ? WHERE id = ?", (nuevo_nombre, id_ciudad))

    def eliminar(self, id_ciudad):
        self.db.execute("DELETE FROM ciudades WHERE id = ?", (id_ciudad,))

    def consultar_por_provincias(self, nombres_provincias):
        placeholders = ','.join('?' for _ in nombres_provincias)
        query = f'''
            SELECT c.nombre, c.cod_postal, c.cpa, p.nombre
            FROM ciudades c
            JOIN provincias p ON c.id_provincia = p.id
            WHERE p.nombre IN ({placeholders})
        '''
        return self.db.fetchall(query, nombres_provincias)

    def consultar_ordenadas(self, nombre_provincia, orden):
        if orden not in ['cod_postal', 'cpa', 'nombre']:
            print("Orden inválido.")
            return []
        query = f'''
            SELECT c.nombre, c.cod_postal, c.cpa
            FROM ciudades c
            JOIN provincias p ON c.id_provincia = p.id
            WHERE p.nombre = ?
            ORDER BY c.{orden}
        '''
        return self.db.fetchall(query, (nombre_provincia,))
