import os
import pytest
from selenium import webdriver
from utils.helper_functions import SaucedemoHelper

URL_BASE = "https://www.saucedemo.com"

@pytest.fixture
def setup(request):
    """Fixture para inicializar el navegador Chrome antes de cada prueba y tomar captura al finalizar."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    
    driver = webdriver.Chrome(options=options)
    driver.get(URL_BASE)
    
    yield driver
    
    # Crear la carpeta de reportes si no existe
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    
    # Nombre de la captura basado en el nombre del test
    test_name = request.node.name
    screenshot_path = os.path.join(reports_dir, f"{test_name}.png")
    
    # Tomar captura automática
    driver.save_screenshot(screenshot_path)
    
    driver.quit()

def test_01_login_exitoso(setup):
    """Caso 1: Validar automatización de login con credenciales válidas."""
    driver = setup
    helper = SaucedemoHelper(driver)

    helper.iniciar_sesion("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"
    assert helper.obtener_titulo_pagina() == "Products", "El título de la página no es 'Products'"

def test_02_navegacion_y_verificacion_catalogo(setup):
    """Caso 2: Verificar título, presencia de productos e interfaz del catálogo."""
    driver = setup
    helper = SaucedemoHelper(driver)

    helper.iniciar_sesion("standard_user", "secret_sauce")

    assert helper.obtener_titulo_pagina() == "Products"
    assert helper.verificar_elementos_interfaz(), "El menú o el filtro no están visibles"

    nombre, precio = helper.obtener_primer_producto_info()
    assert nombre != "", "El nombre del primer producto está vacío"
    assert precio != "", "El precio del primer producto está vacío"

def test_03_interaccion_con_carrito(setup):
    """Caso 3: Agregar producto, verificar contador y validar ítem en el carrito."""
    driver = setup
    helper = SaucedemoHelper(driver)

    helper.iniciar_sesion("standard_user", "secret_sauce")

    nombre_esperado, _ = helper.obtener_primer_producto_info()

    helper.agregar_primer_producto_al_carrito()

    assert helper.obtener_contador_carrito() == "1", "El contador del carrito no se incrementó correctamente"

    helper.ir_al_carrito()

    assert "/cart.html" in driver.current_url
    assert helper.obtener_nombre_producto_en_carrito() == nombre_esperado, "El producto en el carrito no coincide"