from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import io,sys

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


try:
    driver = webdriver.Chrome(
        executable_path='C:\selenium_drivers\chromedriver.exe', options=options)
except Exception:
    print("Error loading chrome webdriver " + sys.exc_info()[0])
    exit(1)


#driver = webdriver.Chrome(options=options,executable_path=r'C:\selenium_drivers\chromedriver.exe')
#ebay:
driver.get("https://www.onepeloton.com/shop/bike")
print(driver.page_source)

'''
          /html/body/div[4]/div[5]/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/div[3]/div[1]/span
//*[@id="srp-river-results"]/ul/li[1]/div/div[2]/div[3]/div[1]/span
'''

#table = driver.find_elements_by_tag_name("td")
r = driver.find_elements_by_xpath('//*[@id="root"]/div/div[2]/article/section[2]/section/div[1]/div/div[1]/div/p[@class="sc-dEZoUN fJrQnC price"]')
print(r)
#price = driver.find_element_by_xpath('/html/body/div[4]/div[5]/div[2]/div[1]/div[2]/ul/li[1]/div/div[2]/div[3]/div[1]/span[@class="s-item__price"]')

#element = driver.findElement(By.className("s-item__price"));
#print(element.getText())

#f = io.open("shopify.txt", mode="w", encoding="utf-8")
#print(price)
#for p in price:
#    print(Title.text)
    #f.write(Title.text+"\n")
#f.close()

driver.quit() 
