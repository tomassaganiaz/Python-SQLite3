# Python-SQLite3

Trabajo Practico N_4: Programacion 

Tiendo en cuenta lo visto en la clase, se pide crear las funciones necesarias para poder realizar la creacion, lectura, actualizacion y eliminacion de registros en tablas de ciudades y provincias, tener en cuenta que si se elimina una provincia se deben eliminar las ciudades que pertenecen a la misma.

Campos de Provincias
ID, Nombre

Campos de Ciudades
ID, CodPostal, CPA, Nombre, IDProvincia

Cargar al menos 10 ciudades de Pcia de Buenos Aires, Cordoba, Santa Fe y San Luis

Se debera entregar, el archivo de python con las funciones y las llamadas a esas funciones para:
- La carga de la ciudades a la provincias antes citadas.
- La consulta de las ciudades de una o mas provincias, segun se ingresen por parametros de la funcion de consulta que corresponda. Ingresando el nombre o nombres de las provincias.
- La consulta cambiando el orden, ya sea por codigo postal, cpa o nombre de las ciudades de una provincia.
- La actualizacion de al menos 5 nombres de ciudades.
- La eliminacion de ciudades y de provincias.

ciudades_provincias/
│
├── main.py               # Punto de entrada
├── db_manager.py         # Clase DBManager para conexión y ejecución
├── provincia.py          # Clase Provincia
├── ciudad.py             # Clase Ciudad
└── setup_data.py         # Para cargar datos de prueba
