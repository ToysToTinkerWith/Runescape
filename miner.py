import cv2 as cv
import numpy as np
import pyautogui
import time
from PIL import Image

def showRect(background, img, max_loc):
	top_left = max_loc
	bottom_right = (top_left[0] + img.shape[1], top_left[1] + img.shape[0])


	cv.rectangle(background, top_left, bottom_right,
		color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

	cv.imshow("vision", background)

	time.sleep(10)


rock_img = cv.imread("rock.png", cv.IMREAD_COLOR)
full_img = cv.imread("full.png", cv.IMREAD_COLOR)


booth_img = cv.imread("booth.png", cv.IMREAD_COLOR)
depo_img = cv.imread("depo.png", cv.IMREAD_COLOR)

window_img = cv.imread("rswindow.png", cv.IMREAD_COLOR)
map_img = cv.imread("map.png", cv.IMREAD_COLOR)

heart_img = cv.imread("heart.png", cv.IMREAD_COLOR)



action = "mining"
window_coords = (0, 0)
minimap_coords = (0, 0)

while(True):

	screenshot = pyautogui.screenshot()
	screenshot = np.array(screenshot)
	screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

	cv.imwrite("state.png", screenshot)

	game_state = cv.imread("state.png", cv.IMREAD_COLOR)

	if(action == "mining"):
		print(action)

		#Locate RS Window and Minimap

		result = cv.matchTemplate(game_state, window_img, cv.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

		threshold = 0.8
		if max_val >= threshold:
			window_coords = (max_loc[0]/2, max_loc[1]/2)
			print(window_coords)

			minimap_coords = (window_coords[0] + 600, window_coords[1] + 55)
			print(minimap_coords)

			minimap = pyautogui.screenshot(region=(minimap_coords[0]*2, minimap_coords[1]*2, 175, 175))
			minimap = np.array(minimap)
			minimap = cv.cvtColor(minimap, cv.COLOR_RGB2BGR)

			cv.imwrite("minimap.png", minimap)

			minimap_img = cv.imread("minimap.png", cv.IMREAD_COLOR)

			#Check minimap with full map with route

			result = cv.matchTemplate(map_img, minimap_img, cv.TM_CCOEFF_NORMED)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
			print(max_val)

			threshold = 0.25
			if max_val > threshold:

				#Locate offset from drawn route

				routeMap = Image.open("map.png")

				route = routeMap.crop((max_loc[0], max_loc[1], 250, 250))
				route.save("route.png")

				route_img = cv.imread("route.png", cv.IMREAD_COLOR)

				result = cv.matchTemplate(route_img, heart_img, cv.TM_CCOEFF_NORMED)
				min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
				print(max_val)

				threshold = 0.7
				if max_val >= threshold:
					x = 0
					y = 0
					moveLoc = (0, 0)
					locations = np.where(result >= threshold)
					locations = list(zip(*locations[::-1]))

					for loc in locations:

						if loc[0] > x:
							x = loc[0]
							moveLoc = loc


					pyautogui.moveTo(minimap_coords[0] + moveLoc[0]/2, minimap_coords[1] + moveLoc[1]/2)

					time.sleep(10)




		


	

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
