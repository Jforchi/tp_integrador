from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select  

 
###Sacar el alerta de contraseña
opciones = webdriver.ChromeOptions()
opciones.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False, "profile.password_manager_leak_detection": False})
driver = webdriver.Chrome(options=opciones)
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()




####Caso 1-----------------------------------------------------------------------------------------
elemento = driver.find_element(By.CLASS_NAME, "product_sort_container")
desplegable = Select(elemento)
desplegable.select_by_value("lohi") #Lohi --> low to high 


precios = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

#devuelve los precios de menor a mayor pero en formato texto
anterior = 0
for precio in precios:
    actual = float(precio.text.replace("$", ""))#pasa de texto a float y elimina el signo
    print(actual)
    
    assert actual >= anterior   #verifica que el precio actual sea mayor o igual al anterior---> contemplando que lo acomodamos de low to high
    anterior = actual

time.sleep(15)
print(driver.current_url)
driver.quit()


