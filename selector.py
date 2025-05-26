from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from localizadores import UrbanRoutesLocators
import phone_code
import data


class UrbanRoutesPage:
    def __init__(self, driver, wait_time=10):
        """
        Inicializa la página con el driver y tiempo de espera configurable.
        """
        self.driver = driver
        self.wait_time = wait_time

    def wait_for_load_header(self):
        """Espera hasta que el campo 'from' esté visible en la página."""
        WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(UrbanRoutesLocators.from_field)
        )

    def set_from(self, from_address):
        """Escribe la dirección de origen, limpiando el campo antes."""
        element = self.driver.find_element(*UrbanRoutesLocators.from_field)
        element.clear()
        element.send_keys(from_address)

    def set_to(self, to_address):
        """Escribe la dirección de destino, limpiando el campo antes."""
        element = self.driver.find_element(*UrbanRoutesLocators.to_field)
        element.clear()
        element.send_keys(to_address)

    @property
    def from_value(self):
        """Obtiene el valor actual del campo 'from'."""
        return self.driver.find_element(*UrbanRoutesLocators.from_field).get_property('value')

    @property
    def to_value(self):
        """Obtiene el valor actual del campo 'to'."""
        return self.driver.find_element(*UrbanRoutesLocators.to_field).get_property('value')

    def order_taxi(self):
        """Clic en el botón para ordenar taxi, esperando que sea clickeable."""
        WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable(UrbanRoutesLocators.button_order_taxi)
        ).click()

    def click_comfort_tariff(self):
        """Clic en la tarifa confort."""
        WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable(UrbanRoutesLocators.comfort_tariff_button)
        ).click()

    def select_phone_button(self):
        """Clic en el botón para ingresar número telefónico."""
        WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable(UrbanRoutesLocators.button_phone_number)
        ).click()

    def set_phone(self):
        """Obtiene el texto visible del popup de teléfono."""
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(UrbanRoutesLocators.text_popup)
        ).text

    def write_phone_number(self):
        """Escribe el número de teléfono desde data.py."""
        element = self.driver.find_element(*UrbanRoutesLocators.enter_phone_number)
        element.clear()
        element.send_keys(data.phone_number)

    @property
    def phone_value(self):
        """Obtiene el valor actual del campo de teléfono."""
        return self.driver.find_element(*UrbanRoutesLocators.enter_phone_number).get_property('value')

    def click_next(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(UrbanRoutesLocators.button_next)
        ).click()

    def code_number(self):
        """Obtiene el código SMS y lo escribe en el campo de código."""
        code = phone_code.retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*UrbanRoutesLocators.enter_code).send_keys(code)
        return code

    @property
    def validate_code(self):
        """Obtiene el valor actual del campo de código SMS."""
        return self.driver.find_element(*UrbanRoutesLocators.enter_code).get_property('value')

    def send_info(self):
        """Clic en el botón confirmar para enviar la información."""
        self.driver.find_element(*UrbanRoutesLocators.button_confirm).click()

    def validate_confirm(self):
        """Obtiene el texto del botón de teléfono para validar confirmación."""
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(UrbanRoutesLocators.button_phone_number)
        ).text

    def click_payment_method(self):
        """Clic en el botón de método de pago."""
        self.driver.find_element(*UrbanRoutesLocators.button_payment_method).click()

    def validate_payment(self):
        """Obtiene texto visible para validar sección de pago."""
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(UrbanRoutesLocators.text_payment)
        ).text

    def click_add_card(self):
        """Clic para agregar tarjeta."""
        self.driver.find_element(*UrbanRoutesLocators.button_add_card).click()

    def validate_add_card(self):
        """Obtiene texto visible para validar agregar tarjeta."""
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(UrbanRoutesLocators.text_add_card)
        ).text

    def select_number(self):
        """Selecciona el campo para ingresar número de tarjeta."""
        self.driver.find_element(*UrbanRoutesLocators.set_credit_card).click()

    def write_card_number(self):
        """Escribe número de tarjeta desde data.py."""
        element = self.driver.find_element(*UrbanRoutesLocators.card_number)
        element.clear()
        element.send_keys(data.card_number)

    def write_code(self):
        """Escribe código de tarjeta desde data.py."""
        element = self.driver.find_element(*UrbanRoutesLocators.code_number)
        element.clear()
        element.send_keys(data.card_code)

    @property
    def validate_card(self):
        """Obtiene el valor actual del campo número de tarjeta."""
        return self.driver.find_element(*UrbanRoutesLocators.card_number).get_property('value')

    @property
    def validate_code_card(self):
        """Obtiene el valor actual del campo código de tarjeta."""
        return self.driver.find_element(*UrbanRoutesLocators.code_number).get_property('value')

    def click_agree_card(self):
        """Clic en el checkbox para aceptar tarjeta."""
        self.driver.find_element(*UrbanRoutesLocators.agree_card).click()

    @property
    def validate_agree(self):
        """Valida si el checkbox de aceptar tarjeta está seleccionado."""
        checkbox = self.driver.find_element(*UrbanRoutesLocators.validate_agree)
        return checkbox.is_selected()

    def close_modal(self):
        """Cierra el modal de agregar tarjeta."""
        self.driver.find_element(*UrbanRoutesLocators.close_button).click()

    def validate_close(self):
        """Valida texto luego de cerrar modal."""
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located(UrbanRoutesLocators.validate_text_card)
        ).text

    def set_message(self, message):
        """Escribe un mensaje para el conductor."""
        element = self.driver.find_element(*UrbanRoutesLocators.driver_message_input)
        element.clear()
        element.send_keys(message)

    @property
    def get_message(self):
        """Obtiene el mensaje actual escrito para el conductor."""
        return self.driver.find_element(*UrbanRoutesLocators.input_comment).get_property('value')

    def select_blanket_handkerchiefs(self):
        """Selecciona la opción de cobijas y pañuelos."""
        self.driver.find_element(*UrbanRoutesLocators.select_blanket_handkerchiefs).click()

    @property
    def validate_slider(self):
        """Valida si la opción de cobijas y pañuelos está seleccionada."""
        return self.driver.find_element(*UrbanRoutesLocators.validate_blanket_handkerchiefs).is_selected()

    def select_ice_cream(self):
        """
        Hace doble clic en el botón para ordenar helado (dos clicks consecutivos).
        """
        element = self.driver.find_element(*UrbanRoutesLocators.order_ice_cream)
        element.click()
        element.click()

    @property
    def validate_ice_cream(self):
        """Obtiene el texto con la cantidad de helados pedidos."""
        return self.driver.find_element(*UrbanRoutesLocators.count_ice_cream).text

    def order_a_taxi(self):
        """Clic para ordenar taxi final."""
        self.driver.find_element(*UrbanRoutesLocators.button_order_a_taxi).click()

    @property
    def validate_order(self):
        """Valida texto del modal de orden de taxi."""
        return self.driver.find_element(*UrbanRoutesLocators.validate_modal_taxi).text

    def get_driver_modal_text(self):
        """Espera y obtiene texto visible del modal del conductor."""
        return WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(UrbanRoutesLocators.validate_modal_taxi)
        ).text
