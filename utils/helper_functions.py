#Defino funciones reutilizables con esperas explícitas de Selenium y estrategias de localización
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SaucedemoHelper:
    # Locatores de Login
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    # Locatores del Inventario / Catálogo
    TITLE_LABEL = (By.CLASS_NAME, "title")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    FIRST_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_name")
    FIRST_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price")
    FIRST_ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) button")
    
    # Locatores de Interfaz
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    PRODUCT_SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    
    # Locatores del Carrito
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def iniciar_sesion(self, usuario, password):
        """Realiza el login ingresando credenciales y haciendo clic en ingresar."""
        user_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        user_field.clear()
        user_field.send_keys(usuario)

        pwd_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        pwd_field.clear()
        pwd_field.send_keys(password)

        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_btn.click()

    def obtener_titulo_pagina(self):
        """Retorna el texto del título visible en el inventario."""
        return self.wait.until(EC.visibility_of_element_located(self.TITLE_LABEL)).text

    def obtener_primer_producto_info(self):
        """Retorna el nombre y precio del primer producto listado."""
        nombre = self.wait.until(EC.visibility_of_element_located(self.FIRST_ITEM_NAME)).text
        precio = self.wait.until(EC.visibility_of_element_located(self.FIRST_ITEM_PRICE)).text
        return nombre, precio

    def agregar_primer_producto_al_carrito(self):
        """Hace clic en el botón de agregar al carrito del primer producto."""
        btn_agregar = self.wait.until(EC.element_to_be_clickable(self.FIRST_ADD_TO_CART_BTN))
        btn_agregar.click()

    def obtener_contador_carrito(self):
        """Retorna el número indicado en el ícono del carrito."""
        return self.wait.until(EC.visibility_of_element_located(self.CART_BADGE)).text

    def ir_al_carrito(self):
        """Navega a la página del carrito y espera a que la URL cambie."""
        cart_icon = self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        cart_icon.click()
        self.wait.until(EC.url_contains("/cart.html"))

    def verificar_elementos_interfaz(self):
        """Valida que estén presentes el menú lateral y el filtro de productos."""
        menu = self.wait.until(EC.presence_of_element_located(self.MENU_BUTTON))
        filtro = self.wait.until(EC.presence_of_element_located(self.PRODUCT_SORT_CONTAINER))
        return menu.is_displayed() and filtro.is_displayed()

    def obtener_nombre_producto_en_carrito(self):
        """Retorna el nombre del primer producto dentro del carrito de compras."""
        return self.wait.until(EC.visibility_of_element_located(self.CART_ITEM_NAME)).text