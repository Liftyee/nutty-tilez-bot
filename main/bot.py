# coding: UTF-8

import pyautogui
import pyperclip
pyautogui.PAUSE = 0.1
#1475,350
f = open("vocab.txt", "r")
splitf = f.read().split("\n")

# whether you want the code to find inputs automatically
autoFind = True
autoFind_that_damned_oe_button = True

found = False
rawword = []
eng = []
fre = []
freWord = ""
engWord = ""
indexno = 0
wordHalves = []
for i in range(len(splitf)):
	if splitf[i] != " " and splitf[i] != "":
		rawword.append(splitf[i])

for i in range(len(splitf)):
	
	if i % 2 == 0:
		#make all english lowercase, so it's not case sensitive
		eng.append(splitf[i].lower())
	else:
		fre.append(splitf[i])
	
print(eng)
print(fre)
eng.pop(-1)
while True:
	engWord = input("Input word:").lower()
	try:
		if engWord[0] == "#":
			freWord = engWord.split("#")[1]
			freWord = freWord.replace("1", "à")
			freWord = freWord.replace("2", "â")
			freWord = freWord.replace("3", "ç")
			freWord = freWord.replace("4", "é")
			freWord = freWord.replace("5", "è")
			freWord = freWord.replace("6", "ê")
			freWord = freWord.replace("7", "ù")
			freWord = freWord.replace("8", "û")
			freWord = freWord.replace("9", "ô")
			freWord = freWord.replace("0", "î")
			freWord = freWord.replace("oe", "œ")
		else:
			try:
				indexno = eng.index(engWord)
				freWord = fre[indexno]
				found = True
			except:
				print("Word not in list!")
				freWord = ""
				found = False
	except:
		print("What even did you do???")
	print("before hotkeys: " + freWord)
	
	# do hotkeys
	freWord = freWord.replace("à", "1")
	freWord = freWord.replace("â", "2")
	freWord = freWord.replace("ç", "3")
	freWord = freWord.replace("é", "4")
	freWord = freWord.replace("è", "5")
	freWord = freWord.replace("ê", "6")
	freWord = freWord.replace("ù", "7")
	freWord = freWord.replace("û", "8")
	freWord = freWord.replace("ô", "9")
	freWord = freWord.replace("î", "0")
	freWord = freWord.replace("oe", "œ")
	print("after hotkeys: " + freWord)
	
	# find and click word input box
#	try:
	
	if autoFind:
		im = pyautogui.screenshot(region=(0,0,1920,1080))
		x, y = pyautogui.locateCenterOnScreen("wordbox.png", grayscale=False)
		pyautogui.click(x, y)
	else:
		pyautogui.click(1475,350)
#	except:
#		print("No word box on screen!")
	
	# because pyautogui can't handle la sœur or oe words
	if "œ" in freWord or "oe" in freWord:
		
		#handle oe
		print("Sister detected!!!")
		wordHalves = freWord.split("œ")
		pyautogui.write(wordHalves[0])
		
		if autoFind_that_damned_oe_button:
			
			try:
				im2 = pyautogui.screenshot(region=(400,680,1520,1080))
				x, y = pyautogui.locateCenterOnScreen("that_damned_oe_button.png", grayscale=True)
				pyautogui.click(x,y)
			except:
				print(Exception)
				print("oe button not on screen!")
		else:
			pyautogui.click(1612,765)
		pyautogui.write(wordHalves[1])
		
	else:
		pyautogui.write(freWord)
	if found:
		pyautogui.press("enter")

	pyautogui.click(400,400)
print(eng)
print(fre)
