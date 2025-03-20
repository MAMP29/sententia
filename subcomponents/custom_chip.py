import flet as ft 

class CustomChip(ft.Chip):
    def __init__(self, label, label_color=ft.colors.WHITE, initial_color="#31393c", selected_color="4d869c"):
        super().__init__(label=ft.Text(label, color=label_color), bgcolor=initial_color)

        self.initial_color = initial_color
        self.selected_color = selected_color
        self._is_selected = False
        
        self.on_click = self.toggle_selection

    @property
    def is_selected(self):
        return self._is_selected


        # Función para manejar el clic en el chip
    def toggle_selection(self, e):
        # Cambiar el estado de seleccionado            
        self._is_selected = not self._is_selected

        # Actualizar los colores del chip dependiendo de su estado
        if self.is_selected:
            self.bgcolor = self.selected_color   # Color cuando está seleccionado
            self.leading = ft.Icon(ft.Icons.CHECK, color=ft.colors.WHITE)
        else:
            self.bgcolor = self.initial_color  # Color cuando no está seleccionado
            self.leading = None

        # Actualizar la página para reflejar el cambio
        self.update()