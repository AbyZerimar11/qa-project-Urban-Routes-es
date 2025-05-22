import time
import data
from localizadores import UrbanRoutesLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_header(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(UrbanRoutesLocators.from_field))

    def set_from(self, from_address):
        self.driver.find_element(*UrbanRoutesLocators.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*UrbanRoutesLocators.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*UrbanRoutesLocators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*UrbanRoutesLocators.to_field).get_property('value')

    def order_taxi(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(UrbanRoutesLocators.button_order_taxi)).click()

    def click_comfort_tariff(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(UrbanRoutesLocators.comfort_tariff_button)).click()

    def select_phone_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(UrbanRoutesLocators.button_phone_number)).click()

    def set_phone(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(UrbanRoutesLocators.text_popup)).text

    def write_phone_number(self):
        self.driver.find_element(*UrbanRoutesLocators.enter_phone_number).send_keys(data.phone_number)

    def get_phone(self):
        return self.driver.find_element(*UrbanRoutesLocators.enter_phone_number).get_property('value')

    def click_next(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(UrbanRoutesLocators.button_next)).click()

    def code_number(self):
        code= retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*UrbanRoutesLocators.enter_code).send_keys(code)
        return code

    def validate_code(self):
        return self.driver.find_element(*UrbanRoutesLocators.enter_code).get_property('value')

    def send_info(self):
        self.driver.find_element(*UrbanRoutesLocators.button_confirm).click()

    def validate_confirm(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(UrbanRoutesLocators.button_phone_number)).text

    def click_payment_method(self):
        self.driver.find_element(*UrbanRoutesLocators.button_payment_method).click()

    def validate_playment(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(UrbanRoutesLocators.text_payment)).text

    def click_add_card(self):
        self.driver.find_element(*UrbanRoutesLocators.button_add_card).click()

    def validate_add_card(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(UrbanRoutesLocators.text_add_card)).text

    def select_number(self):
        self.driver.find_element(*UrbanRoutesLocators.set_credit_card).click()

    def write_card_number(self):
        self.driver.find_element(*UrbanRoutesLocators.card_number).send_keys(data.card_number)

    def write_code(self):
        self.driver.find_element(*UrbanRoutesLocators.code_number).send_keys(data.card_code)

    def validate_card(self):
        return self.driver.find_element(*UrbanRoutesLocators.card_number).get_property('value')

    def validate_code_card(self):
        return self.driver.find_element(*UrbanRoutesLocators.code_number).get_property('value')

    def click_agree_card(self):
        self.driver.find_element(*UrbanRoutesLocators.agree_card).click()

    def validate_agree(self):
        checkbox = self.driver.find_element(*UrbanRoutesLocators.validate_agree)
        return checkbox.is_selected()

    def close_modal(self):
        self.driver.find_element(*UrbanRoutesLocators.close_button).click()

    def validate_close(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(UrbanRoutesLocators.validate_text_card)).text

    def set_message(self, message):
        self.driver.find_element(*UrbanRoutesLocators.driver_message_input).send_keys(message)

    def get_message(self):
        return self.driver.find_element(*UrbanRoutesLocators.input_comment).get_property('value')

    def select_blanket_handkerchiefs(self):
        self.driver.find_element(*UrbanRoutesLocators.select_blanket_handkerchiefs).click()

    def validate_slider(self):
        return self.driver.find_element(*UrbanRoutesLocators.validate_blanket_handkerchiefs).is_selected()

    def select_ice_cream(self):
        self.driver.find_element(*UrbanRoutesLocators.order_ice_cream).click()
        self.driver.find_element(*UrbanRoutesLocators.order_ice_cream).click()

    def validate_ice_cream(self):
        return  self.driver.find_element(*UrbanRoutesLocators.count_ice_cream).text

    def order_a_taxi(self):
        self.driver.find_element(*UrbanRoutesLocators.button_order_a_taxi).click()

    def validate_order(self):
        return self.driver.find_element(*UrbanRoutesLocators.validate_modal_taxi).text

    def get_driver_modal_text(self):
        return WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(UrbanRoutesLocators.validate_modal_taxi)).text

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_header()  #tiempo de espera a que se cargue la página
        address_from = data.address_from #agregar dirección desde
        address_to = data.address_to #agregar dirección hasta
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # veriricar que los valores sean corectos
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
    #Seleccionamos el taxi y la tarifa
    def test_order_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_taxi()
        routes_page.click_comfort_tariff()
        valid_selection = self.driver.find_element(*UrbanRoutesLocators.comfort_tariff_button)
        assert 'tcard active' in valid_selection.get_attribute('class'), "La tarifa comfort no fue seleccionada"

    #Seleccionamos boton de telefono y validamos que abra la ventana para ingresar los datos
    def test_phone_modal_text_is_correct(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_phone_button()
        assert routes_page.set_phone() == 'Introduce tu número de teléfono', f"Texto inesperado: {routes_page.set_phone()}"
    #Escribimos el número de telefon oen el campo y validamos que se ingrese correctamente
    def test_write_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.write_phone_number()
        phone_current =routes_page.get_phone()
        assert phone_current == data.phone_number, f"Número esperado {data.phone_number}, pero se tiene {phone_current}"
    #Enviamos el número para conocer el codigo
    def test_click_next(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_next()
        validate_change= self.driver.find_element(*UrbanRoutesLocators.text_next).text
        assert validate_change == 'Introduce el código del SMS', f"Texto inesperado: {validate_change}"
    #Validamos que el código enviado sea el que tenemos en pantalla
    def test_code_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        expected_code = routes_page.code_number()
        assert routes_page.validate_code() == expected_code, f"Código esperado: {expected_code}, pero se mostró: {routes_page.validate_code()}"
    # Enviamos toda la información y validamos que se haya registrado correctamente
    def test_send_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.send_info()
        assert routes_page.validate_confirm() == '+1 123 123 12 12', f"Texto inesperado: {routes_page.validate_confirm()}"
    #Seleccionamos el botón para agregar un metodo de pago
    def test_click_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        assert routes_page.validate_playment() == 'Método de pago', f"Texto inesperado: {routes_page.validate_playment()}"

    #seleccionamos el boton para agregar una tarjeta dentro del modal
    def test_click_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_card()
        assert routes_page.validate_add_card() == 'Agregar tarjeta', f"Texto inesperado: {routes_page.validate_add_card()}"

    #Agregamos trajeta y codigo y validamos que este sean correctos
    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_number()
        routes_page.write_card_number()
        routes_page.write_code()
        assert routes_page.validate_card() == data.card_number, f"El número de tarjeta esperado es: {data.card_number}, pero se mostró: {routes_page.validate_card()}"
        assert routes_page.validate_code_card() == data.card_code, f"El código esperado es: {data.card_code}, pero se mostró: {routes_page.validate_code_card()}"

    #Enviamos los datos de la tarjeta y validamos que si registro
    def test_agreed_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_agree_card()
        assert routes_page.validate_agree(), "El checkbox de aceptación no está seleccionado"
    #Cerrar el modal de agregar tarjeta y verificar quese muestre la tarjeta agregada
    def test_close_modal(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.close_modal()
        assert routes_page.validate_close() == "Tarjeta", f"Texto inesperado: {routes_page.validate_close()}"

    #Escribimos y enviamos un mensaje para el conductor
    def test_send_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        message=data.message_for_driver
        routes_page.set_message(message)
        assert routes_page.get_message() == message, f"Mensaje esperado {message}, pero se tiene {routes_page.get_message()}"

    #Pedir manta y pañuelos y validar que se ha seleccionado
    def test_select_blanket_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_blanket_handkerchiefs()
        assert routes_page.validate_slider()

    #Pedir dos helados y validar que se seleccione correctamente
    def test_order_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_ice_cream()
        assert routes_page.validate_ice_cream() == '2'

    #Solicitamos el taxi y validamos
    def test_order_a_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_a_taxi()
        assert 'Buscar automóvil' in routes_page.validate_order()

    #Validar que la información del conductor aparezca
    def test_driver_arrival_message_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(30)
        assert 'El conductor llegará' in routes_page.get_driver_modal_text(), f"Se esperaba 'El conductor llegará', pero se tiene: {routes_page.get_driver_modal_text()}"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
