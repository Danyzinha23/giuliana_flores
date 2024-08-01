

'''features/comprar_produto.feature:

    Feature: Comprar Produto
        Como um cliente
        Gostaria de comprar produtos no site Giuliana Flores
        Para presentear alguém especial

        Scenario: Comprar Rosas
            Given que eu estou no site da Giuliana Flores
            When eu pesquiso por "Rosas"
            And eu clico no primeiro produto da lista
            And eu adiciono o produto ao carrinho
            Then o produto "Rosas" é exibido no carrinho
    steps/comprar_produto_steps.py:'''


from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
import time



# Abrir o navegador e acessar o site
driver = webdriver.Chrome()
driver.get("https://www.giulianaflores.com.br/")

# Pesquisar por um produto
search_box = driver.find_element(By.ID, "search")
search_box.send_keys("Rosas")
search_box.submit()

# Validar nome e preço do produto na página de resultados
product_name = driver.find_element(By.XPATH, "//div[@class='name']//a").text
product_price = driver.find_element(By.XPATH, "//div[@class='price-new']").text

# Clicar no produto para ver detalhes
driver.find_element(By.XPATH, "//div[@class='name']//a").click()

# Validar nome e preço do produto na página do produto
product_name_details = driver.find_element(By.CLASS_NAME, "h1").text
product_price_details = driver.find_element(By.CLASS_NAME, "dadosProdutoPreço").text

# Adicionar produto ao carrinho
driver.find_element(By.NAME, "buy-button").click()

# Validar nome e preço do produto no carrinho
product_name_cart = driver.find_element(By.CLASS_NAME, "basket-product-name").text
product_price_cart = driver.find_element(By.CLASS_NAME, "basket-product-price").text

# Fechar o navegador
driver.quit()



@given('que eu estou no site da Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('eu pesquiso por "{produto}"')
def step_impl(context, produto):
    context.driver.get("https://www.giulianaflores.com.br/")
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(produto)
    search_box.submit()

@when('eu clico no primeiro produto da lista')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@class='name']//a").click()

@when('eu adiciono o produto ao carrinho')
def step_impl(context):
    context.driver.find_element(By.NAME, "buy-button").click()

@then('o produto "{produto}" é exibido no carrinho')
def step_impl(context, produto):
    product_name_cart = context.driver.find_element(By.CLASS_NAME, "basket-product-name").text
    assert produto in product_name_cart

    context.driver.quit()


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.giulianaflores.com.br/")

    def search_product(self, product):
        search_box = self.driver.find_element(By.ID, "search")
        search_box.send_keys(product)
        search_box.submit()

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(By.XPATH, "//div[@class='name']//a").text

    def get_product_price(self):
        return self.driver.find_element(By.XPATH, "//div[@class='price-new']").text

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