import cv2 as cv
import numpy as np
import pyautogui
import time
from PIL import Image
import random
import os

def showRect(background, img, max_loc):
	top_left = max_loc
	bottom_right = (top_left[0] + img.shape[1], top_left[1] + img.shape[0])


	cv.rectangle(background, top_left, bottom_right,
		color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

	cv.imshow("vision", background)

	time.sleep(10)

def minimapMove(direction):

	print(direction)

	window_coords = (0, 0)
	minimap_coords = (0, 0)

	result = cv.matchTemplate(game_state, window_img, cv.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

	threshold = 0.8
	if max_val >= threshold:
		window_coords = (max_loc[0]/2, max_loc[1]/2)

		minimap_coords = (window_coords[0] + 600, window_coords[1] + 65)

		minimap = pyautogui.screenshot(region=(minimap_coords[0]*2, minimap_coords[1]*2, 175, 175))
		minimap = np.array(minimap)
		minimap = cv.cvtColor(minimap, cv.COLOR_RGB2BGR)

		cv.imwrite("minimap.png", minimap)

		minimap_img = cv.imread("minimap.png", cv.IMREAD_COLOR)

		#Check minimap with full map with route

		result = cv.matchTemplate(map_img, minimap_img, cv.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

		threshold = 0.2
		if max_val > threshold:

			#Locate offset from drawn route

			routeMap = Image.open("map.png")

			route = routeMap.crop((max_loc[0], max_loc[1], max_loc[0] + 250, max_loc[1] + 250))
			route.save("route.png")

			route_img = cv.imread("route.png", cv.IMREAD_COLOR)

			result = cv.matchTemplate(route_img, heart_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

			threshold = 0.5
			if max_val >= threshold:
				if direction == "right":
					x = 0
					y = 0

				if direction == "left":
					x = 1000
					y = 0

				if direction == "down":
					x = 0
					y = 0

				if direction == "up":
					x = 0
					y = 1000

				moveLoc = (0, 0)
				locations = np.where(result >= threshold)
				locations = list(zip(*locations[::-1]))

				for loc in locations:

					if direction == "right":
						if loc[0] > x:
							x = loc[0]
							moveLoc = loc

					if direction == "left":
						if loc[0] < x:
							x = loc[0]
							moveLoc = loc

					if direction == "down":
						if loc[1] > y:
							y = loc[1]
							moveLoc = loc

					if direction == "up":
						if loc[1] < y:
							y = loc[1]
							moveLoc = loc


				pyautogui.click(x=minimap_coords[0] + moveLoc[0]/2, y=minimap_coords[1] + moveLoc[1]/2)



rock_img = cv.imread("rock.png", cv.IMREAD_COLOR)
full_img = cv.imread("full.png", cv.IMREAD_COLOR)


booth_img = cv.imread("booth.png", cv.IMREAD_COLOR)
bank_img = cv.imread("bank.png", cv.IMREAD_COLOR)

window_img = cv.imread("rswindow.png", cv.IMREAD_COLOR)
map_img = cv.imread("map.png", cv.IMREAD_COLOR)

heart_img = cv.imread("heart.png", cv.IMREAD_COLOR)



action = "mining"

while(True):

	print(action)

	screenshot = pyautogui.screenshot()
	screenshot = np.array(screenshot)
	screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

	cv.imwrite("state.png", screenshot)

	game_state = cv.imread("state.png", cv.IMREAD_COLOR)

	if action == "mining":

		minimapMove("down")
		time.sleep(random.uniform(2.5, 6.5))

		result = cv.matchTemplate(game_state, rock_img, cv.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

		threshold = 0.7
		if max_val >= threshold:
			action = "mine"


	if action == "mine":

		result = cv.matchTemplate(game_state, rock_img, cv.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
		print(max_val)

		threshold = 0.7
		if max_val >= threshold:
			pyautogui.click(x=max_loc[0]/2, y=max_loc[1]/2)

		result = cv.matchTemplate(game_state, full_img, cv.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

		if max_val >= threshold:
			minimapMove("up")
			time.sleep(random.uniform(3.5, 5.5))
			minimapMove("up")
			time.sleep(random.uniform(3.5, 5.5))
			minimapMove("up")
			time.sleep(random.uniform(3.5, 5.5))
			minimapMove("up")
			time.sleep(random.uniform(3.5, 5.5))

			action = "banking"

		time.sleep(random.uniform(1.5, 2.5))

	if action == "bank":

		result = cv.matchTemplate(game_state, bank_img, cv.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
		print(max_val)

		threshold = 0.8
		if max_val >= threshold:
			pyautogui.rightClick(x=max_loc[0]/2 + 430, y=max_loc[1]/2 + 210)
			time.sleep(random.uniform(0.2, 0.5))
			pyautogui.move(5, 100, random.uniform(0.5, 1))
			pyautogui.click()
			time.sleep(random.uniform(0.2, 0.5))
			action = "mining"
			minimapMove("right")
			time.sleep(random.uniform(2.5, 5.5))
			minimapMove("right")
			time.sleep(random.uniform(2.5, 5.5))
			minimapMove("right")
			time.sleep(random.uniform(2.5, 5.5))
			minimapMove("right")
			time.sleep(random.uniform(2.5, 5.5))


		else:
			action = "banking"

	if action == "banking":

		result = cv.matchTemplate(game_state, booth_img, cv.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

		threshold = 0.6
		if max_val >= threshold:
			pyautogui.click(x=max_loc[0]/2 + 20, y=max_loc[1]/2 + 20)
			time.sleep(random.uniform(4.5, 5.5))
			action = "bank"

		else:
			minimapMove("left")
			time.sleep(random.uniform(3.5, 5.5))





			



			

			


















		





		


	

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
