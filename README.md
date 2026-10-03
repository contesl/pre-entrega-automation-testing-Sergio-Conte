# Pre-entrega Automation Testing - SauceDemo

Este repositorio contiene la solución automatizada para las pruebas end-to-end de la aplicación web [SauceDemo](https://www.saucedemo.com).

## 📌 Propósito del Proyecto
Demostrar la capacidad de automatizar flujos básicos de navegación, login, verificación de catálogo e interacción con el carrito de compras en una aplicación web utilizando Python, Selenium WebDriver y Pytest.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.10+
- **Automatización Web:** Selenium WebDriver 4
- **Framework de Pruebas:** Pytest
- **Reportes:** Pytest-HTML
- **Control de Versiones:** Git y GitHub

## 📁 Estructura del Proyecto
```text
pre-entrega-automation-testing-Sergio-Conte/
├── datos/                        # Datos auxiliares o de prueba (si aplica)
├── reports/                      # Generación de reportes HTML y evidencias gráficas
│   ├── Reporte.html
│   ├── test_01_login_exitoso.png
│   ├── test_02_navegacion_y_verificacion_catalogo.png
│   └── test_03_interaccion_con_carrito.png
├── tests/                        # Casos de prueba automatizados
│   ├── __init__.py
│   └── test_saucedemo.py
├── utils/                        # Funciones auxiliares y locatores (Page Helpers)
│   ├── __init__.py
│   └── helper_functions.py
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Documentación general
```

## 🧪 Casos de Prueba Coberturados

1. **`test_01_login_exitoso`**: Valida la autenticación con credenciales válidas (`standard_user`) y la posterior redirección al catálogo (`/inventory.html`).
2. **`test_02_navegacion_y_verificacion_catalogo`**: Verifica la presencia del título de la página, la visibilidad de elementos clave de la interfaz (menú, filtros) y la correcta carga de datos del catálogo.
3. **`test_03_interaccion_con_carrito`**: Verifica la adición de un producto al carrito, la actualización del contador en el ícono y la validación del ítem al navegar a `/cart.html`.

## 🚀 Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU-USUARIO/pre-entrega-automation-testing-Sergio-Conte.git
   cd pre-entrega-automation-testing-Sergio-Conte
   ```

2. **Crear y activar entorno virtual (Opcional recomendado):**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Ejecución de Pruebas y Reportes

Para ejecutar todas las pruebas automatizadas, tomar capturas de pantalla automáticas y generar el reporte HTML ejecute:

```bash
python -m pytest tests/test_saucedemo.py -v --html=reports/Reporte.html
```

* **Reporte HTML:** Estará disponible en `reports/Reporte.html`.
* **Capturas de pantalla:** Se guardarán automáticamente en la carpeta `reports/` al finalizar cada prueba.
