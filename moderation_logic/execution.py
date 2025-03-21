from utils.useful_functions import generate_combinations
from utils.useful_functions import subtract_dict

# Esta clase representa una ejecución ya hecha
class Execution:
    def __init__(self, nombre):
        self.nombre = nombre
        self.id_ejecucion = None
        self.fecha_ejecucion = None
        self.tamano_entrada = None # Valor global, incluye número de grupos y esfuerzo
        self.content = {}  # Diccionario para almacenar la salida por algoritmo
        self.num_agents_per_group = None
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
        self.num_agents_per_group = ()
        for linea in secciones[1:-1]:  # Excluye num_groups y effort
            agents, op1, op2, rigidity = map(float, linea.split())  # Convertir a números
            self.groups.append({
                "num_agents": int(agents),  # Es entero
                "op1": op1,
                "op2": op2,
                "rigidity": rigidity
            })
            self.num_agents_per_group += (int(agents),)


        self.tamano_entrada = len(secciones)  # Cantidad de líneas en la entrada

        print("PRUEBA DE QUE QUEDÓ TODO BIEN JEJOX")
        print(f"Número de grupos {self.num_groups}")
        print(f"Grupos {self.groups}")
        print(f"Esfuerzo disponible {self.effort}") 
        print(f"Tamaño de la entrada {self.tamano_entrada}")

    def can_apply_effort(self, groups, groups_selected): # sea groups_selected una tupla con el esfuerzo aplicado a cada grupo
        print("Aplicando esfuerzo")

        total = 0
        for i, s in zip(groups, groups_selected):
            total+=(abs(i['op1'] - i['op2']) * i['rigidity'] * s)

        print(f"total de esfuerzo {total}")
        if total <= self.effort:
            return True, total
        else:
            return False, total

    def estimate_internal_conflict(self, groups):
        print("Estimando conflicto interno")

        numerador = sum((i['num_agents'] * (i['op1'] - i['op2'])**2) for i in groups)
        denominador = sum(i['num_agents'] for i in groups)

        return numerador/denominador if denominador != 0 else 0


    def modci_fb(self, groups):
        print("Ejecutando verdad por fuerza bruta")

        combinations = generate_combinations(self.num_agents_per_group)

        ci = float('inf')
        total = 0
        best_comp = ()
        for i in combinations:
            control_effort, new_total = self.can_apply_effort(groups, i)

            if control_effort:
                new_group = subtract_dict(i, groups)
                ci_temp = self.estimate_internal_conflict(new_group)

                if ci_temp < ci:
                    ci = ci_temp
                    total = new_total
                    best_comp = i

        print(total, best_comp, ci)
        return total, best_comp, ci



