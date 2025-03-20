

# Esta clase representa una ejecución ya hecha
class Execution:
    def __init__(self, nombre):
        self.nombre = nombre
        self.id_ejecucion = None
        self.fecha_ejecucion = None
        self.tamano_entrada = None # Valor global, incluye número de grupos y esfuerzo
        self.content = {}  # Diccionario para almacenar la salida por algoritmo
        self.num_groups = None
        self.groups = {}
        self.effort = None
        self.tiempos_de_ejecucion = {}  # Guardar tiempos separados por algoritmo
        self.algoritmos_usados = None

    def agregar_salida(self, algoritmo, salida):
        """Agrega la salida de un algoritmo específico."""
        self.content[algoritmo] = salida

    def cargar_datos_ejecucion(self, id_ejecucion, fecha_ejecucion, algoritmos_usados):
        """Carga los datos de la ejecución."""
        self.id_ejecucion = id_ejecucion
        self.fecha_ejecucion = fecha_ejecucion
        self.algoritmos_usados = algoritmos_usados


    def network_builder(self):
        secciones = self.content.strip().split("\n")  # Limpia espacios extra

        self.num_groups = int(secciones[0])  # Convertir a entero
        self.effort = float(secciones[-1])  # Convertir a flotante

        # Procesar los grupos
        self.groups = []
        for linea in secciones[1:-1]:  # Excluye num_groups y effort
            agents, op1, op2, rigidity = map(float, linea.split())  # Convertir a números
            self.groups.append({
                "num_agents": int(agents),  # Es entero
                "op1": op1,
                "op2": op2,
                "rigidity": rigidity
            })

        self.tamano_entrada = len(secciones)  # Cantidad de líneas en la entrada

        print("PRUEBA DE QUE QUEDÓ TODO BIEN JEJOX")
        print(f"Número de grupos {self.num_groups}")
        print(f"Grupos {self.groups}")
        print(f"Esfuerzo disponible {self.effort}") 
        print(f"Tamaño de la entrada {self.tamano_entrada}")
