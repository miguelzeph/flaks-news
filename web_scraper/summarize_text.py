from config import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


####### Driver Constants Settings ########
DRIVER_PATH = config.get("browser_driver.path")
URL_SUMMARIZER = config.get("browser_driver.url_summarizer")


# Thi way I can avoid to scroll down
def set_zoom_level(driver, zoom_percent):
    zoom_script = f"document.body.style.zoom='{zoom_percent}%'"
    driver.execute_script(zoom_script)

#####  Driver Instance & Configuration #####
service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(URL_SUMMARIZER)
# Maximizar a janela do navegador
driver.maximize_window()
set_zoom_level(driver, 50)  # Set zoom to 50%
#############################################



def summarize_text(text: str) -> str:

    sleep(3) 
    text_area = driver.find_element(By.ID, 'textArea')
    # Always Clean
    text_area.clear()
    text_area.send_keys(text)
    
    sleep(3) 

    # Rolar para baixo para garantir que o botão "Summarize Text" esteja visível
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.execute_script("window.scrollBy(0, 400);")
    
    
    # # Localize o botão "Accept" usando uma das abordagens
    # accept_button = driver.find_element(By.XPATH, "//button[@title='Accept' and @aria-label='Accept']")

    # if accept_button:
    #     accept_button.click()


    # Localize e clique no botão "Summarize Text"
    summarize_button = driver.find_element(By.CSS_SELECTOR, '.scoreButton')
    summarize_button.click()

    # Aguarde um pouco para o resultado aparecer
    sleep(3)

    # Localize o elemento com o texto resumido
    result_span = driver.find_element(By.CSS_SELECTOR, '.result-text')
    summarized_text = result_span.text

    return summarized_text
