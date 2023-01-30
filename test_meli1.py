
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

def wait(t = 1):
    if t == 1:
        seconds = 1
    else:
        seconds = t
    time.sleep(seconds)
    
DT = 2

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument("--remote-debugging-port=9222")  # this

driver_path = 'C:\\Users\\JoseAntonioToroOspin\\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(driver_path,chrome_options=options)

https = "https://www.mercadolibre.com.co/publicar/vehiculos/30254754-listmot-4f2e335e2990/step_one"

def prepText():
    wait()
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'input#title')))\
        .send_keys(Keys.CONTROL + "a")
    WebDriverWait(driver, 1)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'input#title')))\
        .send_keys(Keys.DELETE)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'input#title')))\
        .send_keys('chevrolet aveo')
    # Confirmar marca modelo
    xPathClick = '/html/body/main/div/div/div/div/div/form/div/div[2]/div[2]/button/span'
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                          xPathClick)))\
        .click()
        
    wait()
    
    xPathCyC = '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[2]/div/ul/li[3]/div[1]/div/span'
    # carro y camioneta
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                          xPathCyC)))\
        .click()
        
def scrapMake(number):
    xPathMake = '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[3]/div[4]/ul/li[' + str(number) + ']/div[1]/div/span'
    wait()
    WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      xPathMake)))\
    .click()


def scrapModel(number):
    xPathModel = '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[2]/div/ul/li[' + str(number) + ']/div[1]/div/span'
    xPathModel1= '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[3]/div/ul/li[' + str(number) + ']/div[1]/div/span'
    xPathModel2= '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[3]/div[4]/ul/li[' + str(number) + ']/div[1]/div/span'
    xPathValidation = '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[3]/div[3]'
    
    wait()
    try:
        WebDriverWait(driver, DT)\
            .until(EC.visibility_of_element_located((By.XPATH,
                                               xPathValidation)))
        WebDriverWait(driver, DT)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                              xPathModel2)))\
            .click()
    except:
        try:
            WebDriverWait(driver, DT)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                   xPathModel)))\
                .click()
        except:
            WebDriverWait(driver, DT)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                   xPathModel1)))\
                .click()
    
def scrapYear(number):
    xPathYear = '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[2]/div/ul/li[' + str(number) + ']/div[1]/div/span'
    xPathYear1= '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[3]/div[4]/ul/li[' + str(number) + ']/div[1]/div/span'
    xPathYear2= '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[3]/div/ul/li[' + str(number) + ']/div[1]/div/span'
    xPathValidation = '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[3]/div[3]'
    wait()
    try:
        WebDriverWait(driver, DT)\
            .until(EC.visibility_of_element_located((By.XPATH,
                                               xPathValidation)))
        WebDriverWait(driver, DT)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                              xPathYear1)))\
            .click()
    except:
        try:
            WebDriverWait(driver, DT)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                   xPathYear)))\
                .click()
        except:
            WebDriverWait(driver, DT)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                   xPathYear2)))\
                .click()
        

def scrapTrim(number):
    xPathModel = '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[3]/div/ul/li[' + str(number) + ']/div[1]/div/span'
    xPathModel1= '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/div/div[2]/div/div[2]/div/ul/li[' + str(number) + ']/div[1]/div/span'
    wait(0.6)
    DT = 1.1
    try:
        WebDriverWait(driver, DT)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                               xPathModel)))
        texto_columnas = driver.find_elements(By.XPATH, xPathModel)
        texto_final = ([texto.text for texto in texto_columnas][0] + "\n").split("\n")[0]
    except:
        WebDriverWait(driver, DT)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                               xPathModel1)))
        texto_columnas = driver.find_elements(By.XPATH, xPathModel1)
        texto_final = ([texto.text for texto in texto_columnas][0] + "\n").split("\n")[0]
        
    return texto_final

def textToDf():
    wait()
    
    CSS = 'ol.andes-breadcrumb'
    WebDriverWait(driver, 3)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           CSS)))
    

    xPath = '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/nav/ol'
    texto_columnas = driver.find_elements(By.XPATH, xPath)

    texto_final = ([texto.text for texto in texto_columnas][0] + "\n").split("\n")
    
    i = 0
    for texto in texto_final:
        i = i + 1
        if i == 1:
            continue
        elif i == 2:
            make = texto
        elif i == 3:
            model = texto
        elif i == 4:
            year = texto
    
    trim = ''
    trimNumber = 1
    catalog_parcial = pd.DataFrame(columns=['make','model','trim','year'])
    
    while trim != 'Otros':
        trim = scrapTrim(trimNumber)
        trimNumber = trimNumber + 1
        
        catalog_proceso = pd.DataFrame([[make,model,trim,year]],columns=['make','model','trim','year'])

        catalog_parcial =  pd.concat([catalog_parcial, catalog_proceso], ignore_index=True)
    
    
    return catalog_parcial
    
    
def yearRetunr():
    xPath = '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/nav/ol/li[4]/a'
    wait()
    try:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                               xPath)))
        WebDriverWait(driver, DT)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                               xPath)))\
            .click()
    except:
        print('imposible retornar del year')
    

#iniciamos navegador

driver.get(https) 

# escribimos un marca modelo para iniciar el proceso
prepText()
    
scrap = True

makeNumber = 18
modelNumber = 68
yearNumber = 1
trimNumber = 1

catalog_final = pd.DataFrame(columns=['make','model','trim','year'])

while scrap == True:
    scrapMake(makeNumber)
    try:
        scrapModel(modelNumber)
    except:
        make = 'Otras marcas'
        year = 'Otros'
        model = 'Otros modelos'
    try: 
        scrapYear(yearNumber)
    except:
        year = 'Otros'
        model = 'Otros modelos'
        print('se llega a final de Model')
    try:
        catalog_proceso = textToDf()
        yearNumber = yearNumber + 1 
        year = catalog_proceso.iloc[0]['year']
        make = catalog_proceso.iloc[0]['make']
        model = catalog_proceso.iloc[0]['model']
    except:
        print('Se debe cambiar el modelo finalizamos year')
        
    print(catalog_proceso)
    
    
 
    
    if year < '2010' and year != '':
        modelNumber = modelNumber + 1 
        yearNumber = 1
    else:
        if year != 'Otros' and year != '':
            catalog_final =  pd.concat([catalog_final, catalog_proceso], ignore_index=True)
        while year != 'Otros':
            print('bucle de year')
            yearRetunr()
            try: 
                scrapYear(yearNumber)
            except:
                print('se llega a final de Model')
            try:
                catalog_proceso = textToDf()
                yearNumber = yearNumber + 1 
                year = catalog_proceso.iloc[0]['year']
            except:
                year = 'Otros'
                print('Se debe cambiar el modelo finalizamos year')
            
            print(catalog_proceso)
            
                
            make = catalog_proceso.iloc[0]['make']
            model = catalog_proceso.iloc[0]['model']
            
            if make == 'Otras marcas':
                year = 'Otros'
            if year == 'Otros':
                yearNumber = 1
            if year == '':
                yearNumber = yearNumber - 1 
            elif year < '2010' and year != '':
                year = 'Otros'
                yearNumber = 1
            else:
                catalog_final =  pd.concat([catalog_final, catalog_proceso], ignore_index=True)
            
            
        
    print('salida bucle year')

    if make == 'Otras marcas':
        scrap = False
            
    if year == 'Otros':
        modelNumber = modelNumber + 1 
        yearNumber = 1
    
    if model == 'Otros modelos':
        makeNumber = makeNumber + 1 
        modelNumber = 1
        yearNumber = 1
    
    wait()

    #Devolverse
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/nav/ol/li[2]/a')))\
        .click()


catalog_final=catalog_final[catalog_final["trim"] != 'Otros'] 
catalog_final=catalog_final[catalog_final["year"] != 'Otros'] 
catalog_final=catalog_final[catalog_final["year"] > '2009'] 
catalog_final=catalog_final[catalog_final["model"] != 'Otros modelos'] 

catalog_final.to_excel('catalogo_meli2.xlsx', index=False)




WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/main/div/div/div/div/div/form[2]/div/div[2]/nav/ol/li[1]/a')))\
    .click()



wait()
driver.close()
driver.quit()
