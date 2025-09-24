from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import data_inicio, data_fim, email, senha

def executar_auto():

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # remove alguns logs chatos

    driver = webdriver.Chrome()
    driver.maximize_window()


    # Inicializa o driver do Chrome
    # driver = webdriver.Chrome()

    # Acessa o site
    driver.get("Link para site Syngoo Talk")

    # Espera 5 segundos para o site carregar
    time.sleep(5)

    # Exemplo de interagir com um elemento (clicar em um botão, por exemplo)

    # Encontra o elemento pelo seu ID e clica nele
    element = driver.find_element(by=By.NAME, value="email")
    element.send_keys(email)

    element=driver.find_element(by=By.NAME,value="password")
    element.send_keys(senha)

    time.sleep(2)

    element=driver.find_element(by=By.XPATH,value='//*[@id="q-app"]/div/div/div[1]/div[1]/div[2]/form/button')
    element.click()

    # Espera para ver o efeito da interação
    print("entrei no sistema")
    time.sleep(5)

    #Clica no sidebar 
    element=driver.find_element(by=By.CLASS_NAME,value="sidebar-toggle")
    element.click()
    print("Menu")
    time.sleep(3)

    ####-----------------------------------Gerar Relatório ____________________________________
    #escolhe Relatórios
    element = driver.find_element(by=By.XPATH,value= "//span[@class='item-text' and normalize-space()='Relatórios']")
    element.click()
    time.sleep(3)

    try:
        element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='text-item' and normalize-space()='Variáveis']"))
        )
        element.click()
        print("✅ Clicou em 'Variáveis'")
    except:
        print("❌ Não foi possível encontrar a opção 'Variáveis'")

    driver.execute_script("alert('Você tem 10 segundos para colocar as datas');")
    time.sleep(15)

    # #Campo de datas
    # campo_data = driver.find_element(by=By.ID,value="Periods-input")

    # # remove o atributo readonly e insere as datas
    # driver.execute_script("arguments[0].removeAttribute('readonly')", campo_data)
    # driver.execute_script("arguments[0].value = arguments[1]", campo_data, f"{data_inicio} - {data_fim}")
    # time.sleep(2)

    # seleciona o elemento <select>
    # clica no dropdown para abrir
    dropdown = driver.find_element(by=By.ID,value= "report-inputs-tag")
    driver.execute_script("arguments[0].parentElement.click()", dropdown)
    time.sleep(1)

    # clica na opção NOTA_AGENTE
    opcao = driver.find_element(by=By.XPATH,value= "//div[@class='item' and @data-value='NOTA_AGENTE']")
    opcao.click()

    time.sleep(1)

    # clica no primeiro botão (pesquisa)
    primeiro = driver.find_element(by=By.XPATH,value= "(//div[@class='sixteen wide column right aligned d-flex justify-end']//button)[1]")
    primeiro.click()
    time.sleep(2)  # espera o resultado carregar

    # clica no segundo botão (XLSX), para criar um arquivo de exportação xlsx
    segundo = driver.find_element(By.XPATH,value= "(//div[@class='sixteen wide column right aligned d-flex justify-end']//button)[2]")
    segundo.click()
    time.sleep(5)


    ####---------------------------------Exporta Relatório ---------------------------------------------------------
    #Escolhe a opção Exportações
    element = driver.find_element(by=By.XPATH,value= "//span[@class='text-item' and normalize-space()='Exportações']")
    element.click()

    # 1 - clicar no dropdown (ícone com as três barras)
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div[2]/table/tbody/tr[1]/td[7]/div'))
    )
    dropdown.click()

#Download
    time.sleep(2)
    opcao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//table//tr[1]/td[7]//a'))
    )
    opcao.click()



    time.sleep(10)

    # Fecha o navegador
    driver.quit()

# executar_auto()