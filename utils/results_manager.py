import flet as ft
from components.results_panel import ResultsPanel
from subcomponents.custom_button import ResultExcutionButton

# Este manager permite un puente entre el sidebar y el excel panel para que puedan compartir información, en especial el apartado de ejecuciones
class ResultsManager:
    def __init__(self):
        self.sidebar = None
        self.exec_panel = None
        self.results_panel = None
        self.page = None

    def set_page(self, page):
        self.page = page

    def set_sidebar(self, sidebar):
        self.sidebar = sidebar

    def set_exec_panel(self, exec_panel):
        self.exec_panel = exec_panel

    def set_results_panel(self, results_panel):
        self.results_panel = results_panel

    def add_result_button(self, execution):
        # Crea el botón pasando el execution manager
        button = ResultExcutionButton(
            execution=execution, 
            color=ft.colors.BLACK, 
            results_manager=self
        )
        
        # Añade el botón al sidebar
        if self.sidebar:
            self.sidebar.add_results_button(button)


    def load_execution_results(self, execution):
        # Crear un nuevo ResultsPanel con la ejecución específica
        new_results_panel = ResultsPanel(execution)
        
        # Reemplazar el panel actual en la fila
        if self.page:
            row = self.page.controls[0]
            row.controls[1] = new_results_panel
            self.page.update()

    def load_execution_panel(self, execution_panel=None):
        # Si no se proporciona un panel específico, usar el panel de ejecución predeterminado
        panel_to_load = execution_panel or self.exec_panel
        
        if self.page and panel_to_load:
            # Accede a la fila principal
            row = self.page.controls[0]
            # Reemplaza el segundo control (índice 1) con el nuevo panel
            row.controls[1] = panel_to_load
            self.page.update()