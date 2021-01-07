import cv2 as cv
import numpy as np
import pyautogui
import time

rock_img = cv.imread("color.png", cv.IMREAD_COLOR)
full_img = cv.imread("full.png", cv.IMREAD_COLOR)

#Heading to Mine
a_img = cv.imread("a.png", cv.IMREAD_COLOR)
b_img = cv.imread("b.png", cv.IMREAD_COLOR)
c_img = cv.imread("c.png", cv.IMREAD_COLOR)
d_img = cv.imread("d.png", cv.IMREAD_COLOR)
e_img = cv.imread("e.png", cv.IMREAD_COLOR)
f_img = cv.imread("f.png", cv.IMREAD_COLOR)
g_img = cv.imread("g.png", cv.IMREAD_COLOR)
h_img = cv.imread("h.png", cv.IMREAD_COLOR)

#Heading to Bank
first_img = cv.imread("first.png", cv.IMREAD_COLOR)
second_img = cv.imread("second.png", cv.IMREAD_COLOR)
third_img = cv.imread("third.png", cv.IMREAD_COLOR)
fourth_img = cv.imread("fourth.png", cv.IMREAD_COLOR)
fifth_img = cv.imread("fifth.png", cv.IMREAD_COLOR)
bank_img = cv.imread("bank.png", cv.IMREAD_COLOR)
booth_img = cv.imread("booth.png", cv.IMREAD_COLOR)
depo_img = cv.imread("depo.png", cv.IMREAD_COLOR)




action = "mining"
step = "a"

while(True):

	screenshot = pyautogui.screenshot()
	screenshot = np.array(screenshot)
	screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

	cv.imwrite("state.png", screenshot)

	game_state = cv.imread("state.png", cv.IMREAD_COLOR)

	if(action == "mining"):
		print(action)

		if(step == "a"):
			print(step)

			result = cv.matchTemplate(game_state, a_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "b"
				time.sleep(5)
			else:
				step = "mine"

		elif(step == "b"):
			print(step)

			result = cv.matchTemplate(game_state, b_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "c"
				time.sleep(5)
			else:
				step = "a"

		elif(step == "c"):
			print(step)

			result = cv.matchTemplate(game_state, c_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "d"
				time.sleep(5)
			else:
				step = "b"

		elif(step == "d"):
			print(step)

			result = cv.matchTemplate(game_state, d_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "e"
				time.sleep(5)
			else:
				step = "c"

		elif(step == "e"):
			print(step)

			result = cv.matchTemplate(game_state, e_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "f"
				time.sleep(5)
			else:
				step = "d"

		elif(step == "f"):
			print(step)

			result = cv.matchTemplate(game_state, f_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "g"
				time.sleep(5)
			else:
				step = "e"

		elif(step == "g"):
			print(step)

			result = cv.matchTemplate(game_state, g_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "h"
				time.sleep(5)
			else:
				step = "f"

		elif(step == "h"):
			print(step)

			result = cv.matchTemplate(game_state, h_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "mine"
				time.sleep(5)
			else:
				step = "g"



		elif(step == "mine"):
			print(step)

			result = cv.matchTemplate(game_state, rock_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2 + 10), y=(max_loc[1]/2 + 10))
				time.sleep(1)
		
			else:
				print("iron not found")

			result = cv.matchTemplate(game_state, full_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				action = "banking"
				step = "first"



	elif (action == "banking"):
		print(action)

		if(step == "first"):
			print(step)

			result = cv.matchTemplate(game_state, first_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "second"
				time.sleep(5)

		elif(step == "second"):
			print(step)

			result = cv.matchTemplate(game_state, second_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "third"
				time.sleep(5)
			else:
				step = "first"

		elif(step == "third"):
			print(step)

			result = cv.matchTemplate(game_state, third_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "fourth"
				time.sleep(5)
			else:
				step = "second"

		elif(step == "fourth"):
			print(step)

			result = cv.matchTemplate(game_state, fourth_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "fifth"
				time.sleep(5)
			else:
				step = "third"

		elif(step == "fifth"):

			result = cv.matchTemplate(game_state, fifth_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "bank"
				time.sleep(5)
			else:
				step = "fourth"

		elif(step == "bank"):
			print(step)

			result = cv.matchTemplate(game_state, bank_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "booth"
				time.sleep(5)
			else:
				step = "fifth"

		elif(step == "booth"):
			print(step)

			result = cv.matchTemplate(game_state, bank_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				step = "depo"
				time.sleep(5)
			else:
				step = "bank"

		elif(step == "depo"):
			print(step)

			result = cv.matchTemplate(game_state, bank_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.8
			if max_val >= threshold:
				pyautogui.click(x=(max_loc[0]/2), y=(max_loc[1]/2))
				action = "mining"
				step = "a"
				time.sleep(5)
			else:
				step = "booth"


			




	

print("done")

#draw rect
'''

top_left = max_loc
bottom_right = (top_left[0] + iron_img.shape[1], top_left[1] + iron_img.shape[0])


cv.rectangle(game_state, top_left, bottom_right,
	color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

cv.imshow("vision", game_state)

cv.waitKey()

'''
