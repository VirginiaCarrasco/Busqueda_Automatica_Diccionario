from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = True

def Escribir_txt (definicion_palabra, palabra_buscada):
    #En linux no hay problema, en windows requiere encoding e ignorar errores de caracteres.
    f = open ('Resultado_busqueda.txt','a',encoding='utf-8', errors='ignore')
    f .write("Definiciones de " + palabra+"\n")
    f.write(definicion_palabra)
    f.write ("\n---------------------------------Fin definiciones de " + palabra + "--------------------------------------------------------")
    f.close()

print("Por favor, ingrese la palabra que desea buscar en el diccionario. Si desea terminar escriba 'Esc' ")
palabra= str(input())
while palabra != "Esc":
    print("Excelente! Buscaremos la palabra ", palabra)
    #Chromedriver 88
    driver = webdriver.Chrome("/home/facundop/Python Virginia/Busqueda_Automatica_Diccionario-main/chromedriver",chrome_options=options)
    driver.get("https://dle.rae.es/")
    busqueda_palabra = driver.find_element_by_name("w")
    busqueda_palabra.send_keys(palabra)
    busqueda_palabra.send_keys(Keys.ENTER)
    definicion_palabra = driver.find_element_by_tag_name("article").text
    Escribir_txt(definicion_palabra, palabra)
    driver.quit()
    print("Por favor, ingrese la palabra que desea buscar en el diccionario. Si desea terminar escriba 'Esc' ")
    palabra= str(input())
    if palabra == "Esc":
        break