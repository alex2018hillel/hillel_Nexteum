import unittest
import configparser
from tests.utils.default_page import Default_page
#from tests.utils.create_page import Create_mail
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class The_first_page_test(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)

    def test_first(self, quantity = 4):
        wdriver = self.driver
        parser = configparser.ConfigParser()
        parser.read('simple_config.ini')
        url = parser.get('data', 'url')

        # Cart filling
        wdriver.get(url)
        product_name_field = wdriver.find_element_by_xpath(Default_page.product_name_field)
        product_name = product_name_field.text
        prise_elem = wdriver.find_element_by_xpath(Default_page.prise_field)
        prise = prise_elem.text
        quantity_field = wdriver.find_element_by_xpath(Default_page.quantity_field)
        quantity_field.send_keys(quantity)
        button_add = wdriver.find_element_by_xpath(Default_page.button_add)
        button_add.click()
        wdriver.implicitly_wait(10)

        purchased_goods_field = wdriver.find_element_by_xpath(Default_page.purchased_goods_field)
        assert product_name == purchased_goods_field.text
        calculated_full_prise = float(prise)*quantity
        full_prise_elem = wdriver.find_element_by_xpath(Default_page.quantity_elem)
        assert float(full_prise_elem.text) == calculated_full_prise

        # Remove from cart
        button_delite = wdriver.find_element_by_xpath(Default_page.button_delite)
        button_delite.click()
        assert len(wdriver.find_elements_by_xpath(Default_page.quantity_elem)) == 0

        def tear_down(self):
            self.driver.quit()

    if __name__ == "__main__":
        unittest.main()






















