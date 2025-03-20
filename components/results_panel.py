import flet as ft
from textwrap import dedent

class ResultsPanel(ft.Container):
    def __init__(self, execution):
        super().__init__()
        self.name_execution = ft.Text("Panel de los resultados", size=20, weight="bold")
        self.execution = execution



        # Es necesario mantenerlo así para que no falle
        self.test_message = dedent("""
        # Este es un ejemplo de un panel de resultados 

        Aquí podrás ver los resultados de tus ejecuciones. Cada ejecución tiene su información respectiva, esta se cargará sobre el panel junto a sus gráficos y demás información para que puedas verlas.

        ---

        - **Detalles:** Información detallada de cada ejecución.
                                
        Selecciona uno de los botones para visualizar los resultados de la ejecución correspondiente.
        """)

        self.btn_bf = ft.ElevatedButton(
            content=ft.Text("Brute Force result", color=ft.colors.WHITE, weight="bold"), 
            bgcolor="#707d82", 
            disabled=True, 
            on_click=self.change_content_to_lst
        )

        self.btn_dm = ft.ElevatedButton(
            content=ft.Text("Dinamic method result", color=ft.colors.WHITE, weight="bold"), 
            bgcolor="#707d82", 
            disabled=True, 
            on_click=self.change_content_to_bst
        )

        self.btn_gm = ft.ElevatedButton(
            content=ft.Text("Greedy result", color=ft.colors.WHITE, weight="bold"),
            bgcolor="#707d82",
            disabled=True,
            on_click=self.change_content_to_dl
        )

        self.buttons_row = ft.Row(
            controls=[self.btn_bf, self.btn_dm, self.btn_gm],
            expand=False
        )

        self.brute_force = None
        self.dinamic_method = None
        self.greedy_method = None

        self.obtain_output()

        

        self.markdown = ft.Markdown(value=self.test_message, selectable=True)
        

        self.results_text = ft.Container(
            content=ft.Column(
                controls=[
                    self.buttons_row,
                    ft.Column(controls=[self.markdown,],scroll=ft.ScrollMode.AUTO,expand=True)
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=5,
            ),
            bgcolor=ft.colors.WHITE,
            alignment=ft.alignment.center,
            border=ft.border.all(1, ft.colors.BLACK26),
            border_radius=10,
            padding=10,
            expand=True,
        )




        self.download_listdict_button = ft.ElevatedButton(text="Descargar resultado",
                                                          icon=ft.icons.DOWNLOAD,
                                                          tooltip="Se descargará en txt el resultado seleccionado en el markdown",
                                                          disabled=False,
                                                          on_click=self.download)
        

        self.download_result = ft.Row(
            controls=[
                self.download_listdict_button,
            ],
        )

        self.texto_tiempos = None
        self.texto_entradas = None

        self.view_for_content()
        self.extra_info_text = self.extra_info_text_examiner()

        self.extra_info = ft.Container(
            content=ft.Column(
                controls=[
                    self.extra_info_text, 
                    ft.Container(expand=True),  # Esto empuja el botón al fondo
                    self.download_listdict_button
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.END  # Alinea al final de la columna
            ),
            bgcolor="#e9ecef",
            border=ft.border.all(1, ft.colors.BLACK26),
            alignment=ft.alignment.center,
            border_radius=10,
            padding=5,
            expand=True,
        )

        self.chart_info = ft.Container(
            content=self.download_result,
            bgcolor="#e9ecef",
            border=ft.border.all(1, ft.colors.BLACK26),
            border_radius=10,
            padding=5,
            expand=True,
        )
        
        self.info_panel = ft.Column(
            controls=[
                self.extra_info,
            ],
            spacing=5,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.END ,
        )

        self.principal_result_panel = ft.Row(
            controls=[
                self.results_text,
                self.info_panel,
            ],
            spacing=10,
            expand=True,
        )

        self.content = ft.Column(
            controls=[
                self.name_execution,
                self.principal_result_panel,
            ],
            spacing=10,
        )

        # Añadir bordes y estilo al contenedor principal
        self.border = ft.border.all(1, ft.colors.BLACK26)
        self.border_radius = 10
        self.padding = 10
        self.expand = True


    def obtain_output(self):
        if self.execution is not None:
            self.listas_diccionarios = self.execution.content.get('Listas-diccionarios', {}).get('salida', None)
            self.arbol_binario_busqueda = self.execution.content.get('Arbol Binario de Busqueda', {}).get('salida', None)
            self.listas_doblemente_enlazadas = self.execution.content.get('Listas doblemente enlazadas', {}).get('salida', None)
            
            

    def view_for_content(self):
        if self.execution is not None:

            if self.brute_force is not None:
                self.btn_bf.disabled = False
                self.btn_bf.bgcolor = "#31393c"

            if self.dinamic_method is not None:
                self.btn_dm.disabled = False
                self.btn_dm.bgcolor = "#af4500"

            if self.greedy_method is not None:
                self.btn_gm.disabled = False
                self.btn_gm.bgcolor = "#00a841"
                                

    def change_content_to_lst(self, e):
        # Actualizar el contenido del markdown

        formatted_text = self.listas_diccionarios

        formatted_text = formatted_text.replace("\n", "\n\n")

        self.markdown.value = dedent(formatted_text)
        
        # Cambiar colores de los botones
        self.btn_bf.bgcolor = "#4d869c"
        self.btn_dm.bgcolor = "#707d82"
        self.btn_gm.bgcolor = "#707d82"
        
        # Actualizar botones y markdown
        self.btn_bf.update()
        self.btn_dm.update()
        self.btn_gm.update()
        self.markdown.update()


    def change_content_to_bst(self, e):
        # Similar al método anterior, pero con contenido BST

        formatted_text = self.arbol_binario_busqueda

        formatted_text = formatted_text.replace("\n", "\n\n")

        self.markdown.value = dedent(formatted_text)


        self.btn_bf.bgcolor = "#707d82"
        self.btn_dm.bgcolor = "#4d869c"
        self.btn_gm.bgcolor = "#707d82"
        
        self.btn_bf.update()
        self.btn_dm.update()
        self.btn_gm.update()
        self.markdown.update()

    def change_content_to_dl(self, e):
        # Similar al método anterior, pero con contenido DL
        formatted_text = self.listas_doblemente_enlazadas

        formatted_text = formatted_text.replace("\n", "\n\n")

        self.markdown.value = dedent(formatted_text)

        self.btn_bf.bgcolor = "#707d82"
        self.btn_dm.bgcolor = "#707d82"
        self.btn_gm.bgcolor = "#40905f"

        self.btn_bf.update()
        self.btn_dm.update()
        self.btn_gm.update()
        self.markdown.update()

    def extra_info_text_examiner(self):
        if self.execution is None:
            return ft.Text("Aquí verás información adicional", size=20, weight="bold")
        else:
            tiempos_ejecucion = self.execution.tiempos_de_ejecucion
            tiempo_general = tiempos_ejecucion['general']
            tiempo_tamaño_entrada = tiempos_ejecucion['tamano_entrada']
            tiempo_listas_diccionarios = self.execution.content.get("Listas-diccionarios", {}).get("tiempo_ejecucion", "No consideraste esta ejecución")
            tiempo_bst = self.execution.content.get("Arbol Binario de Busqueda", {}).get("tiempo_ejecucion", "No consideraste esta ejecución")
            tiempo_listas_doblemente_enlazadas = self.execution.content.get("Listas doblemente enlazadas", {}).get("tiempo_ejecucion", "No consideraste esta ejecución")


            tamano_entrada = self.execution.tamano_entrada
            tamano_entrada_total = tamano_entrada['total']
            tamano_entrada_participantes = tamano_entrada['participantes']
            tamano_entrada_preguntas = tamano_entrada['preguntas']
            tamano_entrada_temas = tamano_entrada['temas']


            # Concatenar todo en un solo string
            self.texto_tiempos = f"Tiempo general: {tiempo_general} \n Tiempo tamaño entrada: {tiempo_tamaño_entrada} \n Tiempo listas-diccionarios: {tiempo_listas_diccionarios} \n Tiempo BST: {tiempo_bst} \n Tiempo Listas doblemente enlazadas: {tiempo_listas_doblemente_enlazadas}"

            self.texto_entradas = f"Tamaño total: {tamano_entrada_total} \n Participantes: {tamano_entrada_participantes} \n Preguntas: {tamano_entrada_preguntas} \n Temas: {tamano_entrada_temas}"


            return ft.Column(
                controls=[
                    ft.Text("Resultados generales", size=20, weight="bold"),
                    ft.Text(self.texto_tiempos, size=15, weight="bold"),
                    ft.Text(self.texto_entradas, size=15, weight="bold")
                ],
            )
        
    def download(self, e):
        # Descargar el contenido del markdown
        valor = []
        print(self.texto_tiempos)
        print(self.texto_entradas)

        valor.append(str(self.markdown.value))
        valor.append("")
        valor.append(str(self.texto_tiempos))
        valor.append("")
        valor.append(str(self.texto_entradas))


        # Convertir la lista en una cadena de texto separada por saltos de línea
        contenido = "\n".join(valor)

        with open(f"{self.execution.nombre}_{self.execution.id_ejecucion}.txt", "w", encoding='utf-8') as f:
            f.write(contenido)
       