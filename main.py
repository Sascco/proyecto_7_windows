import data
from locators import locators
from UrbanRoutesPage import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


#start

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome()  # desired_capabilities = capabilities
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.driver.implicitly_wait(10)

    #prueba 1 - PASSED - Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
    # def test_set_route(self):
    #     self.driver.get(data.URBAN_ROUTES_URL)
    #     set_route = UrbanRoutesPage(self.driver)
    #     set_route.set_from(data.ADDRESS_FROM)
    #     set_route.set_to(data.ADDRESS_TO)
    #     from_1 = set_route.get_from()
    #     assert from_1 == data.ADDRESS_FROM
    #     set_route.click_book_a_taxi_button()


    #prueba 2  PASSED
    # def test_comfort_fare(self):
    #     self.driver.get(data.URBAN_ROUTES_URL)
    #     set_route = UrbanRoutesPage(self.driver)
    #     set_route.set_from(data.ADDRESS_FROM)
    #     set_route.set_to(data.ADDRESS_TO)
    #     set_route.click_book_a_taxi_button()
    #     set_route.comfort_fare_button()
        # assert set_route.comfort_fare_button()    Fix this assert!!!!

    # prueba 3
    # def test_fill_phone_number_box(self):  # Rellenar el número de teléfono.
    #     self.driver.get(data.URBAN_ROUTES_URL)
    #     set_route = UrbanRoutesPage(self.driver)
    #     set_route.set_from(data.ADDRESS_FROM)
    #     set_route.set_to(data.ADDRESS_TO)
    #     set_route.click_book_a_taxi_button()
    #     set_route.phone_popup_window_input_box(data.phone_number)
    #     set_route.phone_popup_window_input_box_next()
    #     set_route.code_field()
    #     set_route.code_confirm_button()
    #     sleep(2)

    #prueba 4 ingresar información de tarjeta de credito
    # def test_add_payment_method(self):  # Agregar tarjeta de credito como metodo de pago
    #     self.driver.get(data.URBAN_ROUTES_URL)
    #     set_route = UrbanRoutesPage(self.driver)
    #     set_route.set_from(data.ADDRESS_FROM)
    #     set_route.set_to(data.ADDRESS_TO)
    #     set_route.click_book_a_taxi_button()
    #     sleep(1)
    #     set_route.payment_method_selector()
    #     set_route.click_on_add_new_cc()
    #     set_route.add_credit_card_number()
    #     set_route.cc_code_field()
    #     set_route.exit_payment_popup()

    #prueba 5 / NO ESTÁ COMPLETA /  Escribir un mensaje para el controlador.
    def test_special_instruction_for_service(self): # Mensaje para conductor
        self.driver.get(data.URBAN_ROUTES_URL)
        set_route = UrbanRoutesPage(self.driver)
        set_route.set_from(data.ADDRESS_FROM)
        set_route.set_to(data.ADDRESS_TO)
        set_route.click_book_a_taxi_button()
        set_route.comfort_fare_button()
        sleep(1)
        set_route.click_message_box_input()
        sleep(3)


    # def test_ordering_blanket(self): #Pedir una manta y pañuelos.
    #     self.driver.get(data.URBAN_ROUTES_URL)
    #     set_route = UrbanRoutesPage(self.driver)
    #     set_route.set_from(data.ADDRESS_FROM)
    #     set_route.set_to(data.ADDRESS_TO)
    #     set_route.click_book_a_taxi_button()
    #     set_route.comfort_fare_button()
    #     sleep(3)
    #     set_route.blanket_and_scarves()

    # def test_add_icecream(self): # Pedir 2 helados.
    #     self.driver.get(data.URBAN_ROUTES_URL)
    #     set_route = UrbanRoutesPage(self.driver)
    #     set_route.set_from(data.ADDRESS_FROM)
    #     set_route.set_to(data.ADDRESS_TO)
    #     set_route.click_book_a_taxi_button()
    #     sleep(3)
    #     set_route = UrbanRoutesPage(self.driver)
    #     ice_cream_to_order = 2
    #     set_route.click_add_ice_cream_button()
    #     #assert self.driver.find_element(*set_route.ice_cream_counter).text == str(ice_cream_to_order)
    #
    #
    #
    # def test_waiting_for_taxi_modal(self): # aparece modal para pedir taxi
    #     test_set_location = UrbanRoutesPage(self.driver)
    #     self.initial_header = test_set_location.get_waiting_popup_header()
    #     test_set_location.click_order_taxi_button()
    #     assert self.driver.find_element(*test_set_location.waiting_popup_header).text == 'Buscar automóvil'

@classmethod
def teardown_class(cls):
    cls.driver.quit()