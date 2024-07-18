from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar o driver do navegador
driver = webdriver.Chrome()

# Navegar até o site da Giuliana Flores
driver.get("https://www.giulianaflores.com.br/")

# Pesquisar por um produto (ex: Rosas)
search_box = driver.find_element(By.ID, "search")
search_box.send_keys("Rosas")
search_box.submit()

# Clicar no primeiro produto da lista
driver.find_element(By.XPATH, "//div[@class='name']//a").click()

# Obter nome e preço do produto na página do produto
product_name = driver.find_element(By.XPATH, "//h1").text
product_price = driver.find_element(By.CLASS_NAME, "price-new").text

# Adicionar o produto ao carrinho
driver.find_element(By.NAME, "buy-button").click()

# Validar o nome e preço do produto no carrinho
product_name_cart = driver.find_element(By.CLASS_NAME, "basket-product-name").text
product_price_cart = driver.find_element(By.CLASS_NAME, "basket-product-price").text

# Fechar o navegador
driver.quit()

from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.giulianaflores.com.br/")

    def search_product(self, product):
        search_box = self.driver.find_element(By.ID, "search")
        search_box.send_keys(product)
        search_box.submit()

from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(By.XPATH, "//h1").text

    def get_product_price(self):
        return self.driver.find_element(By.CLASS_NAME, "price-new").text

    def add_to_cart(self):
        self.driver.find_element(By.NAME, "buy-button").click()

from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "basket-product-name").text

    def get_product_price(self):
        return self.driver.find_element(By.CLASS_NAME, "basket-product-price").text

from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

driver = webdriver.Chrome()
home_page = HomePage(driver)
product_page = ProductPage(driver)
cart_page = CartPage(driver)

# Navegar até a página inicial
home_page.open()

# Pesquisar por um produto
home_page.search_product("Rosas")

# Obter nome e preço do produto na página de resultados
product_name = product_page.get_product_name()
product_price = product_page.get_product_price()

# Clicar no produto para ver detalhes
# Validar nome e preço do produto na página do produto
# Adicionar produto ao carrinho
product_page.add_to_cart()

# Obter nome e preço do produto no carrinho
product_name_cart = cart_page.get_product_name()
product_price_cart = cart_page.get_product_price()

# Fechar o navegador
driver.quit()