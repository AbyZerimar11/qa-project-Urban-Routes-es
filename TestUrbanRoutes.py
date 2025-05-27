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
        routes_page.order_taxi()
        routes_page.click_comfort_tariff()
        selected = self.driver.find_element(*UrbanRoutesLocators.comfort_tariff_button)
        assert "tcard active" in selected.get_attribute("class")

    # 3. Prueba para agregar número de teléfono
    def test_set_phone_number(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.select_phone_button()
        assert routes_page.set_phone() == "Introduce tu número de teléfono"

        routes_page.write_phone_number()
        assert routes_page.phone_value == data.phone_number

        routes_page.click_next()
        assert self.driver.find_element(*UrbanRoutesLocators.text_next).text == "Introduce el código del SMS"

        expected_code = routes_page.code_number()
        assert routes_page.validate_code == expected_code

        routes_page.send_info()
        assert routes_page.validate_confirm() == data.phone_number

    # 4. Prueba que agrega tarjeta de crédito
    def test_add_card(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        assert routes_page.validate_payment() == "Método de pago"

        routes_page.click_add_card()
        assert routes_page.validate_add_card() == "Agregar tarjeta"

        routes_page.select_number()
        routes_page.write_card_number()
        routes_page.write_code()

        assert routes_page.validate_card == data.card_number
        assert routes_page.validate_code_card == data.card_code

        routes_page.click_agree_card()
        assert routes_page.validate_agree
        '''from selenium.webdriver.common.by import By
        self.driver.find_element(By.XPATH, "//input[@id='number']").click()
        self.driver.find_element(By.XPATH, "//*[text()='Agregar']").click()'''

        routes_page.close_modal()
        assert routes_page.validate_close() == "Tarjeta"

    # 5. Prueba que verifica que se pueda enviar mensaje para el conductor
    def test_write_message(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.set_message(data.message_for_driver)
        assert routes_page.get_message == data.message_for_driver

    # 6. Prueba que verifica que se solicitó una frazada
    def test_blanket(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.select_blanket_handkerchiefs()
        assert routes_page.validate_slider

    # 7. Prueba que verifica que se añadieron helados
    def test_add_icecream(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.select_ice_cream()
        assert routes_page.validate_ice_cream == "2"

    # 8. Prueba que verifica la búsqueda de un conductor
    def test_find_driver(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        routes_page.order_a_taxi()
        assert "Buscar automóvil" in routes_page.validate_order

    # 9. Prueba que verifica la información del conductor
    def test_wait_driver_information(self):
        routes_page = selector.UrbanRoutesPage(self.driver)
        time.sleep(35)  # Esperar manualmente a que aparezca la información del conductor
        assert "El conductor llegará" in routes_page.get_driver_modal_text()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()