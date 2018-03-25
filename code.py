
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
driver = Firefox(executable_path='/home/sergey/Downloads/geckodriver')


# ссылка на конкретного цитирующего 
driver.get('https://elibrary.ru/author_items.asp?authorid=804138')

#инфа, где хочу вытащить имя, универ, факультет, город 
nom_univ_fac = driver.find_elements(By.XPATH,'//div')[1]

# здесь хочу найти элемент b в nom_univ_fac - это имя фамилия  
#item = {}
#for i in nom_univ_fac: 
#    item['nom'] = driver.find_elements(By.XPATH,'//b')
    
   
# я оставил часть вверху решил начать с другого: Вытащить на конкретной странице имя, вуз, кафедру.    

#конкретная стр.
drver.get('https://elibrary.ru/author_items.asp?authorid=804138')

item = {}
item['nom'] = driver.find_elements(By.XPATH,'/html/body/div[3]/table/tbody/tr/td/table[1]/tbody/tr/td[2]/form/table/tbody/tr[2]/td[1]/table/tbody/tr/td/div[1]/font/b')
item['univer'] = driver.find_elements(By.XPATH,'/html/body/div[3]/table/tbody/tr/td/table[1]/tbody/tr/td[2]/form/table/tbody/tr[2]/td[1]/table/tbody/tr/td/div[1]/a')
item['fac'] = driver.find_elements(By.XPATH,'/html/body/div[3]/table/tbody/tr/td/table[1]/tbody/tr/td[2]/form/table/tbody/tr[2]/td[1]/table/tbody/tr/div[1]')

# цикл для проверки
for i in item['fac']: 
    print(i.text)
    
nom - сработало нормально 
univer - тоже 
fac - не могу вытащить элемент 
