import flet as ft

# Botón que representa una ejecución realizada, esta asociada a la misma

class ResultExcutionButton(ft.TextButton):
    def __init__(self, execution, color, results_manager):
        super().__init__()
        self.execution = execution
        nombre = self.execution.nombre
        self.content = ft.Text(value=nombre, color=color, weight='bold')
        
        self.on_click = lambda e: results_manager.load_execution_results(self.execution)