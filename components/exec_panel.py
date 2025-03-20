import flet as ft
from components.down_panel import DownPanel

class ExecPanel(ft.Container):
    def __init__(self, file_picker, result_manager):
        super().__init__()
        self.color_bg = "#eef7ff"
        #self.sidebar = sidebar
        self.result_manager = result_manager
        self.selected_file = ft.Text()
        self.file_picker = file_picker #ft.FilePicker(on_result=self.pick_file_result)
        self.selected_file = None  # Variable para guardar el contenido del archivo

        self.down_panel = DownPanel(self.result_manager)

        self.button_files = ft.ElevatedButton(
            text="Seleccione el archivo",
            icon=ft.Icons.UPLOAD_FILE,
            on_click=lambda _: self.file_picker.pick_files(allow_multiple=False),
        )

        self.content = ft.Column(
            controls=[
                ft.Text("Panel de Ejecuciones"),
                ft.Container(
                    content=self.button_files,
                    alignment=ft.alignment.center,
                    expand=True
                ),
                self.down_panel,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.MainAxisAlignment.CENTER
        )
        self.bgcolor = self.color_bg
        self.expand = True  # Permite que el panel derecho ocupe el resto del espacio

        # Añadir bordes y estilo al contenedor principal
        self.border = ft.border.all(1, ft.colors.BLACK26)
        self.border_radius = 10
        self.padding = 10
        self.expand = True

    def set_selected_file(self, file_content, nombre_archivo):
        # Pasar el contenido del archivo a BSTBasedSurvey
        self.button_files.text = nombre_archivo
        self.button_files.update()
        self.down_panel.set_content(file_content, nombre_archivo)

        # Llamar a cargar_datos de BSTBasedSurvey
        #self.bst_survey.cargar_datos(self.selected_file_path)
