# 🚀 PyAPI-Starter 🐍💻
API funcional en **Python** con **FastAPI** y gestión de cambios en **GitHub** 

---

## 📦 Descripción
Proyecto para el desarrollo colaborativo de una API en Python con FastAPI, enfocada en la creación de métodos básicos que devuelvan JSON estático como prueba de funcionamiento. Incluye una plantilla para documentar cambios antes de nuevas versiones.

## 🔹Características:

*   ###  🛠️ Stack Técnico:
    - ⚡ FastAPI (endpoints REST)
    - 🔥 Uvicorn (servidor ASGI)

*   ### 🔄 Flujo Colaborativo:
    - ✅ Flujo con ramas/PRs
    - 📄 Template para cambios
    - 👥 Revisión comunitaria

*   ### 🚀 Entorno virtual:
    - 🛡️🐍 venv preconfigurado

---

## 🛠️ Instalación 

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/LionelMc/projPractice---PyAPI-Starter.git](https://github.com/LionelMc/projPractice---PyAPI-Starter.git)
    cd projPractice---PyAPI-Starter/
    ```

2.  **Crear y cambiar a la rama de desarrollo (opcional pero recomendado):**
    ```bash
    git checkout -b nueva_rama
    ```

---

## ⚙️ Entorno Virtual 

1.  **Navegar al directorio de la API:**
    ```bash
    cd API/
    ```

2.  **Crear un entorno virtual (si no existe):**
    ```bash
    python3 -m venv venv
    ```

3.  **Activar el entorno virtual:**
    ```bash
    source venv/bin/activate
    ```
    *(Observarás que el prompt de tu terminal cambia, indicando que el entorno virtual está activo)*

4.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Este paso asegura que tengas todas las librerías necesarias para ejecutar la API)*

5.  **Desactivar el entorno virtual cuando termines (opcional):**
    ```bash
    deactivate
    ```
    *(El prompt de tu terminal volverá a su estado normal)*

---

## 🚀 Aplicación y Uso 

Una vez que has configurado el entorno virtual y las dependencias, puedes ejecutar la API de FastAPI.

1.  **Navegar al directorio de la API (si no estás ya allí):**
    ```bash
    cd API/
    ```

2.  **Activar el entorno virtual:**
    ```bash
    source venv/bin/activate
    ```

3.  **Ejecutar la API con Uvicorn:**
    ```bash
    uvicorn app:app --reload
    ```

4.  **Acceder a los endpoints de la API:**
    Una vez que la aplicación se está ejecutando, puedes acceder a los siguientes endpoints a través de tu navegador o una herramienta como `curl`:
    * `/familia`: Retorna una lista de nombres de familia.
    * `/superheroesDC`: Retorna una lista de superhéroes de DC Comics.
    * `/superheroesMarvel`: Retorna una lista de superhéroes de Marvel Comics.
    * `/cursosPlatzi`: Retorna una lista de cursos de Platzi.

    Por ejemplo, para acceder a la lista de familia, abre tu navegador en: `http://127.0.0.1:8000/familia`

5.  **Detener la API:**
    En la terminal donde se está ejecutando Uvicorn, presiona `Ctrl + C`.

6.  **Desactivar el entorno virtual (opcional):**
    ```bash
    deactivate
    ```

---

## 🧪 Pruebas 

Para asegurar la calidad de la API, aquí se muestra cómo ejecutar las pruebas con el script `test_app.py`

1.  **Instalar librería de prueba (si aún no las tienes):**
    ```bash
    cd API/        # Navegar al directorio de la API (si no estás allí)
    source venv/bin/activate  # Activar el entorno virtual
    pip install pytest httpx  # Instala pytest para ejecutar pruebas y httpx como dependencia de FastAPI TestClient
    ```
    *(Asegúrate de que el entorno virtual esté activo para instalar la librería dentro de él)*

2.  **Crear un archivo de pruebas (ejemplo: `API/test_app.py`):**
    ```python
    from fastapi.testclient import TestClient
    from .app import app  # Importa la instancia de la aplicación

    client = TestClient(app)

    def test_get_familia():
        response = client.get("/familia")
        assert response.status_code == 200
        assert response.json() == ["Amin", "Marce", "Miranda"]

    def test_get_superheroes_dc():
        response = client.get("/superheroesDC")
        assert response.status_code == 200
        assert "Superman" in response.json()

    def test_get_superheroes_marvel():
        response = client.get("/superheroesMarvel")
        assert response.status_code == 200
        assert "Spiderman" in response.json()

    def test_get_cursos_platzi():
        response = client.get("/cursosPlatzi")
        assert response.status_code == 200
        assert "Python" in response.json()
    ```

3.  **Ejecutar las pruebas:**
    Navega al directorio principal o a la raíz del proyecto y ejecuta:
    ```bash
    pytest API/   
    ```
    *(Esto buscará y ejecutará los archivos de prueba (test_*.py o *_test.py) dentro del directorio `API`)*

---

## 🤝 Pull Requests (PR)
Para un flujo de colaboración estructurado, usa la **plantilla de Pull Request**:  
➡️ [Acceder a la plantilla](https://github.com/LionelMc/projPractice---PyAPI-Starter/blob/main/.github/pull-request-template.md)


Al abrir un PR, completa la plantilla con la siguiente información para facilitar la revisión y el seguimiento:

* **Descripción del Cambio:** ¿Qué se modificó?
* **Contexto:** ¿Por qué este cambio es necesario?
* **Método de prueba:** ¿Cómo se verificó el funcionamiento?
* **Tickets relacionados:** ¿Cierra o se vincula a algún issue?
* **Capturas de pantalla (si aplica):** Visuales de la interfaz si hubo cambios.
* **Checklist:**
    * [ ] Seguí las convenciones de estilo.
    * [ ] Agregué pruebas unitarias (si aplica).
    * [ ] Todos los tests pasan.
    * [ ] Documenté los cambios.
* **Otros comentarios:** Notas adicionales para la revisión.

**Utilizar la plantilla asegura trazabilidad, revisiones claras y una documentación continua del proyecto.**