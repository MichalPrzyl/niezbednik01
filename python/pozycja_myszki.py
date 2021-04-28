import pyautogui, time

counter = 0

x1 = 600
y1 = 150

x2 = 950
y2 = 520

x3 = 790
y3 = 315

x4 = 1190
y4 = 470

x5 = 835
y5 = 880


while True:

	screenWidth, screenHeight = pyautogui.size()
	currentMouseX, currentMouseY = pyautogui.position()


	print("X: " + str(currentMouseX))
	print("Y: " + str(currentMouseY))
	print("Counter: " + str(counter))
	print("==================")
	
	#pyautogui.moveTo(100, 150)
	counter += 1
	time.sleep(0.01)
	




#pyautogui.click() -klika
#pyautogui.moveTo(X, Y) - rusza myszka

