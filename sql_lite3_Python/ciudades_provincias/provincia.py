class Provincia:
    def __init__(self, db):
        self.db = db

    def crear_tabla(self):
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS provincias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE
            );
        ''')

    def agregar(self, nombre):
        self.db.execute("INSERT OR IGNORE INTO provincias (nombre) VALUES (?)", (nombre,))

    def eliminar(self, nombre):
        self.db.execute("DELETE FROM provincias WHERE nombre = ?", (nombre,))
