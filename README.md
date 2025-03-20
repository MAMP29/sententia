# Pasos para ejecutar Sententia
---
La GUI que usa Sententia fue construida en Flet, un framework de Python creado para el desarrollo facíl y práctico de distintas aplicaciones multiplataforma, en este estado de desarrollo, para poder usar Sententia debe:

1. Crear y activar el entorno virtual de Python 

- **En Linux/macOS:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

- **En Windows:**

   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```
   
 2. Instalar flet
Usuarios de Linux:
Quizás sea necesario instalar varias librerías adicionales para hacer funcionar Flet. Consulte la [documentación oficial de Flet](https://flet.dev/docs/publish/linux/#prerequisites) para más detalles.
 
     ```
    pip install flet
    ```

Finalmente ejecute el archivo **main.py** desde el entorno virtual.
