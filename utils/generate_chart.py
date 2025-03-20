import flet as ft

class ChartGenerator:
    def __init__(self, execution, listas_diccionarios, arbol_binario_busqueda):
        self.execution = execution
        self.listas_diccionarios = listas_diccionarios
        self.arbol_binario_busqueda = arbol_binario_busqueda

    def generate_bar_chart(self, label, value, color):
        """Genera un grupo de barras para la gráfica"""
        return ft.BarChartGroup(
            x=0,
            bar_rods=[
                ft.BarChartRod(
                    from_y=0,
                    to_y=value,
                    width=40,
                    color=color,
                    tooltip=label,
                    border_radius=0,
                ),
            ],
        )

    def generate_chart(self):
        """Genera la gráfica dependiendo del estado de ejecución"""
        if self.execution is None:
            return ft.Text("Podrás visualizar gráficas aquí", size=20, weight="bold")

        total = self.execution.tamano_entrada.get('total', 0)

        # Configuración de la gráfica base
        chart = ft.BarChart(
            border=ft.border.all(1, ft.Colors.GREY_400),
            left_axis=ft.ChartAxis(
                labels_size=10, title=ft.Text("Tiempo de ejecución (s)"), title_size=20,
                labels=[
                    ft.ChartAxisLabel(value=0, label=ft.Text("0")),
                    ft.ChartAxisLabel(value=max_tiempo, label=ft.Text(f"{max_tiempo:.2f}"))
                ]
            ),
            bottom_axis=ft.ChartAxis(
                labels_size=10,
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.Colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.GREY_300),
            max_y=10,
            interactive=True,
            expand=True,
        )

        # Se verifican las condiciones para mostrar las diferentes gráficas
        if self.listas_diccionarios is not None and self.arbol_binario_busqueda is None:
            tiempo_ejecucion = self.execution.content.get("Listas-diccionarios", {}).get("tiempo_ejecucion", 0)
            print(f"Tiempo de ejecución: {tiempo_ejecucion}")
            max_tiempo = tiempo_ejecucion
            chart.bar_groups = [self.generate_bar_chart("Listas-diccionarios", tiempo_ejecucion, ft.Colors.AMBER)]
            chart.bottom_axis.labels = [ft.ChartAxisLabel(value=0, label=ft.Container(ft.Text("Listas-diccionarios"), padding=10))]

        elif self.listas_diccionarios is None and self.arbol_binario_busqueda is not None:
            tiempo_ejecucion = self.execution.content.get("Arbol Binario de Busqueda", {}).get("tiempo_ejecucion", 0)
            print(f"Tiempo de ejecución: {tiempo_ejecucion}")
            max_tiempo = tiempo_ejecucion
            chart.bar_groups = [self.generate_bar_chart("Arbol Binario de Busqueda", tiempo_ejecucion, ft.Colors.BLUE_500)]
            chart.bottom_axis.labels = [ft.ChartAxisLabel(value=0, label=ft.Container(ft.Text("Arbol Binario de Busqueda"), padding=10))]

        elif self.listas_diccionarios is not None and self.arbol_binario_busqueda is not None:
            tiempo_listas = self.execution.content.get("Listas-diccionarios", {}).get("tiempo_ejecucion", 0)
            tiempo_arbol = self.execution.content.get("Arbol Binario de Busqueda", {}).get("tiempo_ejecucion", 0)
            max_tiempo = max(tiempo_arbol, tiempo_listas)
            chart.bar_groups = [
                self.generate_bar_chart("Listas-diccionarios", tiempo_listas, ft.Colors.AMBER),
                self.generate_bar_chart("Arbol Binario de Busqueda", tiempo_arbol, ft.Colors.BLUE_500)
            ]
            chart.bottom_axis.labels = [
                ft.ChartAxisLabel(value=0, label=ft.Container(ft.Text("Listas-diccionarios"), padding=10)),
                ft.ChartAxisLabel(value=1, label=ft.Container(ft.Text("Arbol Binario de Busqueda"), padding=10))
            ]

        chart.max_y = max_tiempo * 1.2 if max_tiempo > 0 else 10

        return chart