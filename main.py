import flet as ft
import os
from components.exec_panel import ExecPanel
from components.results_panel import ResultsPanel
from components.sidebar import SideBar
from utils.results_manager import ResultsManager

# Función para manejar la selección del archivo
def pick_file_result(e: ft.FilePickerResultEvent, exec_panel):
    if e.files:
        # Guardar la ruta completa del archivo seleccionado
        selected_file_path = e.files[0].path
        selected_file_name = os.path.basename(selected_file_path)
        print(f"Archivo seleccionado: {selected_file_name}")
        
        # Leer el contenido del archivo y pasarlo al ExecPanel
        with open(selected_file_path, 'r', encoding='utf-8') as f:
            file_content = f.read().strip()  # Lee el contenido del archivo

        # Pasar el contenido a ExecPanel para que lo procese
        exec_panel.set_selected_file(file_content, selected_file_name)

results_manager = ResultsManager()

def main(page: ft.Page):
    page.title = "EnSort"
    page.theme_mode = "light"
    page.bgcolor = "#eef7ff"


    # Crea una instancia de FilePicker que se compartirá
    file_picker = ft.FilePicker(on_result=lambda e: pick_file_result(e, exec_panel))
    page.overlay.append(file_picker)
    page.update()

    sidebar = SideBar(results_manager)
    results_panel = ResultsPanel(None)
    exec_panel = ExecPanel(file_picker, results_manager)

    results_manager.set_sidebar(sidebar)
    results_manager.set_exec_panel(exec_panel)
    results_manager.set_results_panel(results_panel)

    # Layout general
    page.add(
        ft.Row(
            controls=[
                sidebar,
                exec_panel, # O ExecPanel
            ],
            alignment=ft.MainAxisAlignment.START,  # Sidebar al inicio
            spacing=5, # Sin espacio entre sidebar y panel
            expand=True
        )
    )

    results_manager.set_page(page)

ft.app(target=main)