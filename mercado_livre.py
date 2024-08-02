from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import re


class MercadoLivre:
    def __init__(self) -> None:
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)

    def wait(self) -> None:
        try:
            element = WebDriverWait(self.navegador,7).until(
                EC.presence_of_element_located((By.XPATH,'//footer[@class="nav-footer"]'))
            )
        except Exception as ex:
            print(ex)
    
    
    def acessar_ambiente(self) ->None:
        """ Acessa o ambiente mercado livre 
        """
        self.navegador.get('https://www.mercadolivre.com.br/')
        self.wait()
        hora_atual = datetime.now() 

        if  EC.presence_of_element_located((By.XPATH,'(//a[@class="nav-logo"])')):
            while hora_atual < hora_atual + timedelta(seconds = 30):
                self.navegador.get('https://www.mercadolivre.com.br/')
                self.wait()       
                if  EC.presence_of_element_located((By.XPATH,'(//a[@class="nav-logo"])')):
                    break
      

    def escolher_produto(self,produto:str)->None:
        barra_pesquisa = self.navegador.find_element(By.ID,'cb1-edit')
        barra_pesquisa.clear()
        barra_pesquisa.send_keys(produto,Keys.ENTER)
        self.wait()


    def valida_item_pag(self,quantidade):
        try:
            WebDriverWait(self.navegador,2).until( 
                EC.presence_of_element_located((By.XPATH,
                f'(//li[@class="ui-search-layout__item"])[{quantidade}]'))       
            )
            return True
        except:
            return False



    def trocar_pagina(self):

        try:
            WebDriverWait(self.navegador,2).until( 
                EC.presence_of_element_located((By.XPATH,'//button[@class="cookie-consent-banner-opt-out__action cookie-consent-banner-opt-out__action--primary cookie-consent-banner-opt-out__action--key-accept"]'))       
            )
            cookies = self.navegador.find_element(By.XPATH,'//button[@class="cookie-consent-banner-opt-out__action cookie-consent-banner-opt-out__action--primary cookie-consent-banner-opt-out__action--key-accept"]')
            cookies.click()
        except:
            pass
        numero_proximo = self.navegador.find_element(By.XPATH,
                "(//li[@class='andes-pagination__button'])").text
        
        numero_proximo = int(numero_proximo) 
        if numero_proximo ==2:
            pag = self.navegador.find_element(By.XPATH,
                f"(//li[@class='andes-pagination__button'])") 
            pag.click()
        else:
            numero_proximo +=1
            pag = self.navegador.find_element(By.XPATH,
                f"(//li[@class='andes-pagination__button'])[{numero_proximo}]") 
            pag.click()


    def verifica_avaliacao(self,quantidade):
        try:
            WebDriverWait(self.navegador,2).until( 
                EC.presence_of_element_located((By.XPATH,
                                f'(//li[@class="ui-search-layout__item"])[{quantidade}]'
                                +'//div[@class="ui-search-reviews ui-search-item__group__element"]'))
                     
            )
            return True
        except :
            return False


    def recolher_avaliacao(self,quantidade):
        try:
            if self.verifica_avaliacao(quantidade=quantidade):
                avaliacao = self.navegador.find_element(By.XPATH,
                            f'(//div[@class="ui-search-reviews ui-search-item__group__element"])[{quantidade}]'
                            +'/span[contains(@class, "andes-visually-hidden") and contains(text(),'
                            +'"Avaliação")]') 
                avaliacao = avaliacao.text.split(' ')[1]
                return avaliacao
            else:
                avaliacao = 'Sem avaliação'
                return avaliacao
        except:
            avaliacao = 'Sem avaliação'
            return avaliacao


    def recolher_nome_produto(self,quantidade):
        try:
            self.wait()
            nome_vendedor_produto = self.navegador.find_element(By.XPATH,f'(//li[@class="ui-search-layout__item"])[{quantidade}]'
                                                    +'//a[@class="ui-search-item__group__element ui-search-link__title-card ui-search-link"]')
            nome_vendedor_produto = nome_vendedor_produto.text
            return nome_vendedor_produto
        except:
            return 'erro'

    def recolher_valor(self,quantidade):
        try:
            self.wait()
            valor_produto = self.navegador.find_element(
                By.XPATH,f'(//li[@class="ui-search-layout__item"])[{quantidade}]'
                +'//span[@class="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"]'
            )
            valor_produto = valor_produto.text.upper()
            valor_produto = re.sub(r'\s+','',valor_produto)
            return valor_produto
        except:
            return 'Erro'

    def verifica_vendedor_fora(self,quantidade):
        try:
            WebDriverWait(self.navegador,2).until( 
                EC.presence_of_element_located((By.XPATH,
                                f'(//li[@class="ui-search-layout__item"])[{quantidade}]'
                                +'//p[@class="ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY"]'))
                     
            )
            return True
        except :
            return False



    def recolher_vendedor(self,quantidade):
        try:
            if self.verifica_vendedor_fora(quantidade):
                vendedor = self.navegador.find_element(By.XPATH,
                                    f'(//li[@class="ui-search-layout__item"])[{quantidade}]'
                                    +'//p[@class="ui-search-official-store-label ui-search-item__group__element ui-search-color--GRAY"]')
                vendedor = vendedor.text
                return vendedor
            else:
                self.wait()
                nome_vendedor = self.navegador.find_element(By.XPATH,f'(//li[@class="ui-search-layout__item"])[{quantidade}]'
                                                +'//a[@class="ui-search-item__group__element ui-search-link__title-card ui-search-link"]')
                nome_vendedor.send_keys(Keys.ENTER)
                self.wait()
                vendedor = self.navegador.find_element(By.XPATH,'//div[@class="ui-pdp-seller__header"]//span[2]')
                vendedor = vendedor.text
                self.navegador.back()
                self.wait()
                return vendedor
        except:
            self.navegador.back()
            self.wait()
            return f'Sem vendedor,produto {quantidade}'



    def recolher_parcelas(self,quantidade):
        try:
            parcelas = self.navegador.find_element(By.XPATH,f'(//li[@class="ui-search-layout__item"])[{quantidade}]'
                                                +'//span[contains(@class,"ui-search-item__group__element ui-search-installments")]')
            parcelas = parcelas.text
            parcelas = re.sub(r'\s+','',parcelas)
            parcelas = parcelas.replace('em',' ').split('x')
            parcelas = ' x '.join(parcelas)
    
            return parcelas
        except:
            return f'Erro'


if __name__ =='__main__':
    mercado = MercadoLivre()
    mercado.acessar_ambiente()
    mercado.escolher_produto('ps5')
    quantidade_produto = 1
    i = 1
    while quantidade_produto <= 80:
        if not mercado.valida_item_pag(i):
            mercado.trocar_pagina()
            i = 1

        avaliacao = mercado.recolher_avaliacao(i)
        nome_produto = mercado.recolher_nome_produto(i)
        valor = mercado.recolher_valor(i)
        vendedor= mercado.recolher_vendedor(i)
        parcelas = mercado.recolher_parcelas(i)

        i += 1
        quantidade_produto += 1

    # print(parcelas)
    # print(vendedor)
    # print(avaliacao)
    # print(nome_produto)
    # print(valor)
    # print('ok')
     

