from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


# specifier l'emplaement de  chromedriver.exe
driver = webdriver.Chrome('/Users/HP/AppData/Local/Temp/Rar$EXa13844.32941/chromedriver.exe')

#Full screen
driver.maximize_window()

# redirect a log in page de Linkdein
driver.get('https://www.linkedin.com')
sleep(3)

# Importer donnees a partir de fichier separer 
cordonne=[]
filename="/Users/HP/Desktop/S2 SSI/py/web scraping/cord.txt"
with open(filename) as file:
    for line in file:
        cordonne.append(line.strip())

# Chercher name input dans log in  page
username = driver.find_element_by_id('session_key')
username.send_keys(cordonne[0])
sleep(3)

# Chercher password input dans log in page
password = driver.find_element_by_id('session_password')
password.send_keys(cordonne[1])
sleep(3)

# Determiner l'emplacement de submit button par xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# Click button
sign_in_button.click()
sleep(3)

# Deplacer dans l'url ou il est notre emplois
driver.get('https://www.linkedin.com/jobs/search/?keywords=reactjs')

# Lists dans lesquelles on va stockes nos donnees
jobs_title_list=[]
companies_names_list=[]
locations_names_list=[]
Url_all=[]

# Fonction parcouris les blocks html afin de les rendre a la forme de text 
def remplir(bs4_parse):
    dt=[]
    for item in bs4_parse:
        dt.append(item.get_text().strip().replace("  "," ").replace("\n",'').replace(",","|"))
    return dt

# Fonction rassemble données qui nous intéressent
def getDATAFromPages():  
    # parsing page
    bs = BeautifulSoup(driver.page_source)

    # Donnees rasemblees 
    jobs_title=bs.find_all('a',{"class":"disabled ember-view job-card-container__link job-card-list__title"})
    companies_names=bs.find_all('a',{"class":"job-card-container__company-name"})
    locations_names=bs.find_all('ul',{"class":"job-card-container__metadata-wrapper"})

    # Stocker les donnees rasemblees 
    jobs_title_list.extend(remplir(jobs_title))
    companies_names_list.extend(remplir(companies_names))
    locations_names_list.extend(remplir(locations_names))

    # Parcourir les jobs title pour extraire href attribut
    for job in jobs_title:
        Url_all.append("https://www.linkedin.com"+job.attrs['href'])


# Chercher le nombre des pages 
bs = BeautifulSoup(driver.page_source)
pages=bs.find_all('li',{"class":"artdeco-pagination__indicator"})
number=len(pages)
# Descendre au bas de la page  
ele =driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div')

# Fonction de collectiondes donnees
for i in range(1,number):
    getDATAFromPages()
    sleep(2)

    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", ele)
    sleep(2)

    # Click button pour aller a la prochaine page
    next_page =driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/section/div/ul/li['+str(i+1)+']/button')
    next_page.click()

# Descendre a le bas de la page 
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", ele)
sleep(3)


# Cree les lignes des donnees a partir des listes dans lesquelles on a stocke les donnes qui nous intéressent 
file_list=[jobs_title_list,companies_names_list,locations_names_list,Url_all]
exported= zip_longest(*file_list)

# Stock les donnees dans fichier CSV
with open("/Users/HP/Desktop/S2 SSI/py/web scraping/linkedinData.csv", "w") as myfile:
    wr=csv.writer(myfile)
    myrow=["job title","company name","location","url"]
    wr.writerow(myrow) 
    wr.writerows(exported)