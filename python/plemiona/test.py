import pyautogui, time

czas = 1

ratusz = pyautogui.locateOnScreen('2.png')


while True:
	ratusz = pyautogui.locateOnScreen('2.png')
	if(ratusz==None):
		print("Nie ma")
	if(ratusz != None):
		pyautogui.click(ratusz.left + ratusz.width/2, ratusz.top + ratusz.height/2)
		print("JEST!")
		
	time.sleep(czas)
	
	
 


