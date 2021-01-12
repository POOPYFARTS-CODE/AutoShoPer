from selenium import webdriver
from selenium import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


print('''

░█████╗░  ██████╗░░█████╗░████████╗  ████╗██████╗░██╗░░░██╗
██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝  ██╔═╝██╔══██╗╚██╗░██╔╝
███████║  ██████╦╝██║░░██║░░░██║░░░  ██║░░██████╦╝░╚████╔╝░
██╔══██║  ██╔══██╗██║░░██║░░░██║░░░  ██║░░██╔══██╗░░╚██╔╝░░
██║░░██║  ██████╦╝╚█████╔╝░░░██║░░░  ████╗██████╦╝░░░██║░░░
╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═══╝╚═════╝░░░░╚═╝░░░

██╗░░░░░░█████╗░███╗░░██╗███████╗░██╗░░░░░░░██╗░█████╗░██╗░░░░░███████╗████╗
██║░░░░░██╔══██╗████╗░██║██╔════╝░██║░░██╗░░██║██╔══██╗██║░░░░░██╔════╝╚═██║
██║░░░░░██║░░██║██╔██╗██║█████╗░░░╚██╗████╗██╔╝██║░░██║██║░░░░░█████╗░░░░██║
██║░░░░░██║░░██║██║╚████║██╔══╝░░░░████╔═████║░██║░░██║██║░░░░░██╔══╝░░░░██║
███████╗╚█████╔╝██║░╚███║███████╗░░╚██╔╝░╚██╔╝░╚█████╔╝███████╗██║░░░░░████║
╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝░░░╚════╝░╚══════╝╚═╝░░░░░╚═══╝
  ''')

link = input('Enter Your Link[Format: https://example.com/us/product_name/product_code.html]:')
print('''

█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀   ▄▀█ █░█ ▄▀█ █ █░░ ▄▀█ █▄▄ █░░ █▀▀   █▀ █ ▀█ █▀▀ █▀ ░ ░ ░ ░
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█   █▀█ ▀▄▀ █▀█ █ █▄▄ █▀█ █▄█ █▄▄ ██▄   ▄█ █ █▄ ██▄ ▄█ ▄ ▄ ▄ ▄''')

def checkStock():
  try:
    options = webdriver.ChromeOptions()# options for driver
    options.add_argument('--ignore-certificate-errors')#argumen added
    options.add_argument('--ignore-ssl-errors')#argumen added 
    driver = webdriver.Chrome("E:/chromedriver_win32 (3)/chromedriver.exe", chrome_options= options )#initiaizing driver
    driver.get(link)#userapp
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'buy-section___yYtjH')))#wait till element specified is located
    username = driver.find_element_by_class_name('buy-section___yYtjH')#sizes element parent
    options = username.find_elements_by_tag_name('span')#element conatins sizes
    optionList = []#sizes array
    for option in options:
      optionList.append(option.get_attribute('innerHTML'))
    for sizes in range(len(optionList)-2):
        print("Size "+ optionList[sizes] + " for is available.")
  finally:
     driver.quit() 


def selectSize():
  input_user = int(input('Please Select your Size:'))
  base = 530 #this is base
  size = (input_user -4)*10
  final_size =  base + size
  # final_link = input_user + final_size
  return(final_size)


def linkWithSize():
  model_number = input('Enter Model Number[Example https://www.adidas.com/us/ultraboost-20-shoes/--->FZ0174<---.html] :')
  size_to_be_selected = selectSize()
  str_fina_one = '?forceSelSize='
  br_link = str(link)+str(str_fina_one)+str(model_number)+'_'+str(size_to_be_selected)
  return(br_link)


def bus():
  lol_link = linkWithSize() 
  return(lol_link)

def final_stage():
  link_ = bus()
  driver = webdriver.Chrome("E:/chromedriver_win32 (3)/chromedriver.exe" )
  driver.get(link_)
  element1 = driver.find_element_by_xpath("(//SPAN[@class='gl-cta__content'][text()='Add To Bag'][text()='Add To Bag'])[5]")
  element1.click()
  time.sleep(10)
  element2 = driver.find_element_by_xpath("//SPAN[@class='gl-cta__content'][text()='Checkout']")
  element2.click()
  time.sleep(15)


checkStock()
selectSize()
linkWithSize()
bus()
final_stage()


  #            *     ,MMM8&&&.            *
  #                 MMMM88&&&&&    .
  #                MMMM88&&&&&&&
  #    *           MMM88&&&&&&&&
  #                MMM88&&&&&&&&
  #                'MMM88&&&&&&'
  #                  'MMM8&&&'      *
  #         |\___/|
  #         )     (             .              '
  #        =\     /=
  #          )===(       *
  #         /     \
  #         |     |
  #        /       \
  #        \       /
  # _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  # |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  # |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  # |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  # |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  # |  |  |  |  |  |  |  |  |  |  |  |  |  |  |