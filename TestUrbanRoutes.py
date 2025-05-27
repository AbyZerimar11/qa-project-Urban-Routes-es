import time
import data
import selector
from localizadores import UrbanRoutesLocators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

# 1. Confirmación del establecimiento de la ruta
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_header()
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        assert routes_page.from_value == data.address_from
        assert routes_page.to_value == data.address_to

    # 2. Prueba que verifica que se selecciona la tarifa Comfort
    def test_order_taxi(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.order_taxi() #Clic en el botón para ordenar taxi, esperando que sea clickeable.
        routes_page.click_comfort_tariff() #Clic en la tarifa confort.
        selected = self.driver.find_element(*UrbanRoutesLocators.comfort_tariff_button) #
        assert "tcard active" in selected.get_attribute("class")

    # 3. Prueba para agregar número de teléfono
    def test_set_phone_number(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.select_phone_button() #Clic en el botón para ingresar número telefónico.
        assert routes_page.set_phone() == "Introduce tu número de teléfono" #Obtiene el texto visible del popup de teléfono.

        routes_page.write_phone_number() #Se escribe el número de teléfono
        assert routes_page.phone_value == data.phone_number #Validación del número de teléfono insertado contra lo que se ve en pantalla

        routes_page.click_next() #Clic en siguiente para solicitar el código
        assert self.driver.find_element(*UrbanRoutesLocators.text_next).text == "Introduce el código del SMS" #Validación del cambio de pantalla para escribir el código

        expected_code = routes_page.code_number() #Indroducimos el código SMS
        assert routes_page.validate_code == expected_code #Validación del código

        routes_page.send_info() #Envío de toda la información
        assert routes_page.validate_confirm() == data.phone_number #Confirmamos que el teléfono se haya agregado

    # 4. Prueba que agrega tarjeta de crédito
    def test_add_card(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.click_payment_method() #Clic en agregar método de pago
        assert routes_page.validate_payment() == "Método de pago" # Validamos que se abra el modal

        routes_page.click_add_card() #Clic para agregar una nueva tarjeta
        assert routes_page.validate_add_card() == "Agregar tarjeta" #Validamos que se abra el modal

        routes_page.select_number() #Selecciona el campo para ingresar número de tarjeta.
        routes_page.write_card_number() #Escribe número de tarjeta desde data.py.
        routes_page.write_code() #Escribe código de tarjeta desde data.py.

        assert routes_page.validate_card == data.card_number #Validamos que el número de tarjeta este agregado
        assert routes_page.validate_code_card == data.card_code #Validamos que el código de tarjeta este agregado

        routes_page.click_agree_card() #Clic en el botón para aceptar tarjeta.
        assert routes_page.validate_agree #Validar que el check tarjeta está seleccionado.

        routes_page.close_modal() #Cierra el modal de agregar tarjeta.
        assert routes_page.validate_close() == "Tarjeta" #Valida texto luego de cerrar modal.

    # 5. Prueba que verifica que se pueda enviar mensaje para el conductor
    def test_write_message(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.set_message(data.message_for_driver) #Escribe un mensaje para el conductor.
        assert routes_page.get_message == data.message_for_driver #Obtiene el mensaje actual escrito para el conductor y lo valida contra el data

    # 6. Prueba que verifica que se solicitó una frazada
    def test_blanket(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.select_blanket_handkerchiefs() #Selecciona la opción de cobijas y pañuelos.
        assert routes_page.validate_slider #Valida si la opción de cobijas y pañuelos está seleccionada.

    # 7. Prueba que verifica que se añadieron helados
    def test_add_icecream(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.select_ice_cream() #Hace doble clic en el botón para ordenar helado (dos clicks consecutivos).
        assert routes_page.validate_ice_cream == "2" #Obtiene el texto con la cantidad de helados pedidos.

    # 8. Prueba que verifica la búsqueda de un conductor
    def test_find_driver(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.order_a_taxi() #Clic para ordenar taxi final.
        assert "Buscar automóvil" in routes_page.validate_order #Valida texto del modal de orden de taxi.

    # 9. Prueba que verifica la información del conductor
    def test_wait_driver_information(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        time.sleep(35)  # Esperar manualmente a que aparezca la información del conductor
        assert "El conductor llegará" in routes_page.get_driver_modal_text() #Espera y obtiene texto visible del modal del conductor.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()