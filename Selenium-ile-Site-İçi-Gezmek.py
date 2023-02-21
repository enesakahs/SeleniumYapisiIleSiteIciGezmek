from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
#selenıum uzerıden erıstıgımız sıtelerde klavye ıle ıslem yapmak ıstedıgımızde ımport etmemız gereken yapı. Örn: klavyeden enter a bas
import time

driver=webdriver.Chrome("C:/Users/enes_/OneDrive/Masaüstü/Python Egitimleri/ChromeDriver/chromedriver.exe")
url="https://www.dr.com.tr/"
driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(2)
kitap=driver.find_element("xpath","/html/body/div[1]/header/div[4]/div[2]/ul/li[1]/a")
kitap.click()
time.sleep(2)
kitapara=driver.find_element(By.CSS_SELECTOR, "body > div.site-container > header > div.site-header-center.bg-c255.py-10 > div > div > div.search.col-12.col-lg-7.mt-10.mt-lg-0.dr-flex > div.search-wrapper.col-12.col-lg-10.p-0 > input")
#kitap menusune tıkladıktan sonra sayfanın yukarısında cıkan arama kısmı 
kitapara.send_keys("şiir") #arama kısmına otomatık olarak siir yazsın
kitapara.send_keys(Keys.ENTER) #entera bassın arama gerceklessın

for i in range(1,10): #ilk 10 kitap
    bilgi=driver.find_element("xpath","/html/body/div/div/div/div/main/div[4]/div[1]/div[{}]/div/div[2]/div[1]/a".format(i)) #siir seklınde aratınca cıkan ılk 10 kıtapı döndürdük
    kitapücret=driver.find_element("xpath","/html/body/div/div/div/div/main/div[4]/div[1]/div[{}]/div/div[2]/div[1]/div[2]/div".format(i)) #siir seklınde aratınca cıkan ılk 10 kıtapın ücretlerini döndürdük
    print(f"Kitap İsimleri: {bilgi.text}, Kitap Ücret :{kitapücret.text}")
time.sleep(500) #chrome hemen kapanmasın diye
driver.close()

#şiir diye arattıktan sonra acılan sayfada ilk kitapların isimlerine incele dedik ve xpath yapılarını kopyaladık.
# /html/body/div/div/div/div/main/div[4]/div[1]/div[1]/div/div[2]/div[1]/a
# /html/body/div/div/div/div/main/div[4]/div[1]/div[2]/div/div[2]/div[1]/a
# /html/body/div/div/div/div/main/div[4]/div[1]/div[3]/div/div[2]/div[1]/a
#/html/body/div/div/div/div/main/div[4]/div[1]/div[i]/div/div[2]/div[1]/a seklınde i degiskenini atayıp döngüye alıp tüm kitapların adını alabiliriz
#ctrl K C toplu yorum satırı

'''
https://selenium-python.readthedocs.io/locating-elements.html
element yapılarını nasıl kullanacagımız burada
'''