import pyautogui
import time



toWait = 2

print("Start odliczania...")
pyautogui.alert("Start odliczania...")

while toWait>0:
	print(str(toWait))
	toWait -= 1
	time.sleep(1)
	
pyautogui.alert("Koniec odliczania")	
pyautogui.alert("Koniec odliczania")
pyautogui.alert("Koniec odliczania")

