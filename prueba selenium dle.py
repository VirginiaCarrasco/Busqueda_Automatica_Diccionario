from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


palabra_buscada = str(input("Por favor, ingrese la palabra que desea buscar en el diccionario: "))
print("Excelente! Buscaremos la palabra ", palabra_buscada)

driver = webdriver.Chrome("/home/facundop/Python Virginia/chromedriver")
driver.get("https://www.google.com.ar")

barra_busqueda = driver.find_element_by_name("q")
barra_busqueda.send_keys("dle")
barra_busqueda.send_keys(Keys.ENTER)

link_dle = driver.find_element_by_class_name("yuRUbf")
link_dle.click()

busqueda_palabra = driver.find_element_by_name("w")
busqueda_palabra.send_keys(palabra_buscada)
busqueda_palabra.send_keys(Keys.ENTER)

definicion_palabra = driver.find_element_by_tag_name("article").text
print(definicion_palabra)

f = open ('pruebadiccionario.txt','a+')
f.write(definicion_palabra)
f.write ("-----------------------------------------------------------------------------------------")
f.close()

salir = input("Presione enter para salir")
driver.quit()