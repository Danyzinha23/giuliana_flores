from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep as tartaruga

class WebDriverManager:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_page(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

class ProductVerifier:
    @staticmethod
    def verificar_preco(valores):
        if valores[-1] == valores[-2]:
            print('Valor igual ao presente no passo anterior')
        else:
            print('Valor diferente ao presente no passo anterior')

    @staticmethod
    def verificar_nome_do_produto(nome_produto):
        if nome_produto[-1].upper() == nome_produto[-2].upper():
            print('Nome igual ao presente no passo anterior')
        else:
            print('Nome diferente ao presente no passo anterior')

class GiulianaFloresBot:
    def __init__(self):
        self.driver_manager = WebDriverManager()
        self.product_verifier = ProductVerifier()
        self.lista_nome_produto = []
        self.lista_preco_produto = []

    def pesquisar_produto(self, produto):
        self.driver_manager.open_page("https://www.giulianaflores.com.br/")
        search_box = self.driver_manager.driver.find_element(By.ID, "txtDsKeyWord")
        search_box.send_keys(produto)
        botao_busca = self.driver_manager.driver.find_element(By.ID, 'btnSearch')
        botao_busca.click()

    def coletar_dados_produto(self):
        try:
            pagina_produtos = WebDriverWait(self.driver_manager.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="content-site"]/div[2]/div'))
            )

            nome_produto = pagina_produtos.find_element(By.XPATH, ".//a/h2")
            preco_produto = pagina_produtos.find_element(By.XPATH, ".//a/div[2]/span[2]")

            self.lista_nome_produto.append(nome_produto.text)
            self.lista_preco_produto.append(preco_produto.text)

            original_handle = self.driver_manager.driver.current_window_handle
            produto_link = pagina_produtos.find_element(By.XPATH, "/html/body/form/div[3]/main/div[2]/div/div[2]/div/div/ul/li[1]/div/a")
            produto_href = produto_link.get_attribute('href')
            self.driver_manager.driver.execute_script("window.open('"+produto_href+"');")

            tartaruga(5)  # Aguarde um segundo para garantir que o elemento está visível
            all_handles = self.driver_manager.driver.window_handles
            new_handle = None
            for handle in all_handles:
                if handle != original_handle:
                    new_handle = handle
                    break
            self.driver_manager.driver.switch_to.window(new_handle)

            pagina_detalhe_produtos = WebDriverWait(self.driver_manager.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="content-site"]/div[6]/div[1]'))
            )

            nome_produto_detalhe = pagina_detalhe_produtos.find_element(By.XPATH, '//*[@id="ContentSite_lblProductDsName"]')
            preco_produto_detalhe = pagina_detalhe_produtos.find_element(By.XPATH, '/html/body/form/div[3]/main/div[6]/div[1]/div[2]/div[6]/span[2]')

            self.lista_nome_produto.append(nome_produto_detalhe.text)
            self.lista_preco_produto.append(preco_produto_detalhe.text)

            self.product_verifier.verificar_preco(self.lista_preco_produto)
            self.product_verifier.verificar_nome_do_produto(self.lista_nome_produto)

            cep_primeira_parte = pagina_detalhe_produtos.find_element(By.XPATH,'//*[@id="ContentSite_txtZip"]')
            cep_primeira_parte.send_keys('06120')
            cep_segunda_parte = pagina_detalhe_produtos.find_element(By.XPATH,'//*[@id="ContentSite_txtZipComplement"]')
            cep_segunda_parte.send_keys('040')

            adicionar_carrinho = pagina_detalhe_produtos.find_element(By.XPATH,'//*[@id="ContentSite_lbtBuy"]')
            adicionar_carrinho.click()
            tartaruga(5)

            seleciona_horario_entrega = pagina_detalhe_produtos.find_element(By.XPATH, "/html/body/form/div[3]/main/div[6]/div[1]/div[2]/div[10]/div[3]/div[6]/div[1]/ul/li[2]/input")
            seleciona_horario_entrega.click()
            clicar_botao_ok = pagina_detalhe_produtos.find_element(By.XPATH,'//*[@id="btConfirmShippingData"]')
            clicar_botao_ok.click()
            adicionar_carrinho.click()

            print('Aguardando página do carrinho........')

            nome_produto_no_carinho = self.driver_manager.driver.find_element(By.XPATH,'//*[@id="ContentSite_Basketcontrol1_idUpdatePanel"]/div[1]/div[2]/ul[2]/li/div[2]/span[1]/a')
            valor_unitario_no_carinho = self.driver_manager.driver.find_element(By.XPATH,'//*[@id="ContentSite_Basketcontrol1_idUpdatePanel"]/div[1]/div[2]/ul[2]/li/div[4]/span[2]')

            self.lista_nome_produto.append(nome_produto_no_carinho.text)
            self.lista_preco_produto.append(valor_unitario_no_carinho.text)

            self.product_verifier.verificar_preco(self.lista_preco_produto)
            self.product_verifier.verificar_nome_do_produto(self.lista_nome_produto)

            tartaruga(5)

        except Exception as e:
            print(f"Erro ao tentar ver detalhes do produto: {e}")

    def fechar(self):
        self.driver_manager.close()

# Uso das classes refatoradas
bot = GiulianaFloresBot()
bot.pesquisar_produto("Rosas")
bot.coletar_dados_produto()
bot.fechar()
