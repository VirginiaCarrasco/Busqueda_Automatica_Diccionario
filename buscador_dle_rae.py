from selenium import webdriver
from selenium.webdriver.common.keys import Keys


palabra_buscada = str(input("Por favor, ingrese la palabra que desea buscar en el diccionario: "))
print("Excelente! Buscaremos la palabra ", palabra_buscada)


#Chromedriver 88
driver = webdriver.Chrome()
driver.get("https://dle.rae.es/")

busqueda_palabra = driver.find_element_by_name("w")
busqueda_palabra.send_keys(palabra_buscada)
busqueda_palabra.send_keys(Keys.ENTER)

definicion_palabra = driver.find_element_by_tag_name("article").text

#En linux no hay problema, en windows requiere encoding e ignorar errores de caracteres.
f = open ('Resultado_busqueda.txt','a',encoding='utf-8', errors='ignore')
f.write("Definiciones de " + palabra_buscada+"\n")
f.write(definicion_palabra)
f.write ("\n---------------------------------Fin definiciones de " + palabra_buscada + "--------------------------------------------------------")
f.close()


driver.quit()