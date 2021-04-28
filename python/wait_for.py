import time, os, pyautogui

print("=========================================")
print("Plemiona 1.0")
print("#program poczeka okreslona ilosc czasu a potem wykona dzialanie na plemionach")
print()

godziny = int(input("Godziny: "))
minuty = int(input("Minuty: "))
sekundy = int(input("Sekundy: "))

godziny2 = godziny * 3600
minuty2 = minuty * 60
wynik = godziny2 + minuty2 + sekundy

print("Ilosc sekund: " + str(wynik))

counter = 0

while(counter < wynik):
	print(str(counter+1) + " z: " + str(wynik))
	counter += 1 
	time.sleep(1)
	
print("Program zakonczyl oczekiwanie i wykonuje kod...")


##TUTAJ KOD ==============================

os.system('python zbieractwo.py')
print("Włączam zbieractwo")

for i in range(3):
	pyautogui.alert("Zbieractwo zakończone")

##KONIEC KODU ==============================


print("Kod zostal wykonany!")