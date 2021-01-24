from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui, time

x1=441 
y1=553

x2=321
y2=335

x3=681
y3=492

x4=535	
y4=906


driver = webdriver.Chrome()




driver.get("http://plemiona.pl")

inputElement1 = driver.find_element_by_id("user")
inputElement2 = driver.find_element_by_id("password")

inputElement1.send_keys('Mr.Cross')
inputElement2.send_keys('hotweels12')

inputElement2.send_keys(Keys.ENTER)

time.sleep(2)

for i in range(21):
	pyautogui.press('tab')
	time.sleep(0.01)
	
pyautogui.press('enter')

time.sleep(5)

pyautogui.moveTo(x1,y1)
pyautogui.click()
time.sleep(3)

pyautogui.moveTo(x2,y2)
pyautogui.click()
time.sleep(2)

pyautogui.moveTo(x3,y3)
pyautogui.click()
time.sleep(2)

pyautogui.moveTo(x4,y4)
pyautogui.click()
time.sleep(1)

pyautogui.alert("Process ended with succes!!!")












#inputElement.send_keys('1')