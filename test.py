import time
import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

print("取得元のurlを入力")
url = input()
print(url)

driver = webdriver.Chrome()
driver.implicitly_wait(1)

driver.get(url)




#elem = driver.find_element_by_id("ingredients").find_element_by_class_name("servings").find_element_by_class_name("recipe_heading").find_element_by_class_name("content").find_element_by_css_selector(".servings_for.yield")
ingred = driver.find_element_by_id("ingredients")
servings = ingred.find_element_by_css_selector(".servings_for.yield")
print(servings.text)

ing_row = driver.find_element_by_id("ingredients_list").find_elements_by_class_name("ingredient_row")

for a in ing_row:
  
    
    try:
        ing_cat = a.find_element_by_class_name("ingredient_category")
    except NoSuchElementException as e:
       ##print('catch NoSuchElementException:', e)
       pass
    else:
        print(ing_cat.text)
    
   
    try:
        name = a.find_element_by_class_name("name")
    except NoSuchElementException as e:
       ##print('catch NoSuchElementException:', e)
       pass
    else:
        print(name.text)
        print(a.find_element_by_css_selector(".ingredient_quantity.amount").text)


for a in driver.find_element_by_id("steps").find_elements_by_class_name("step_text"):
    try:
        s_text = a
    except NoSuchElementException as e:
        ##print('catch NoSuchElementException:', e)
        pass
    else:
        print(s_text.text)


driver.quit()

