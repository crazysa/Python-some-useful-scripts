import pyautogui
import random
import time 



s = pyautogui.size()  

while(True):
	p = pyautogui.position()# To get the present position of the pointer on the Screen
	movex , movey = random.randint(-300,300), random.randint(-300,300) #getting random integers to which will be the movement of the pointer in x and y direction
	if p[0]+movex <= 0 or p[0]+movex >= s[0]: # these if and else statments are because when the pointer moves beyond the screen size there is failsafe which gives an error so to keep the pointer within the limits of the screen
		movex = -(movex)
		
	elif p[1]+movey <= 0 or p[1]+movey >= s[1]:
		movey = -movey
		
	try:#To get to know any error if occurs 	
		pyautogui.moveRel(movex,movey ,  duration = 1)
	except:
		print(p , s , movex , movey)
		break
	time.sleep(1.5)#some sleeptime to give pause before each movement

	