import pygame
import time
import threading
from threading import Thread


pygame.init()

#variables 






display_width =800
display_height =600

black = (0,0,0)
white = (255,255,255)

carImage1 = pygame.image.load('aaa.png')
carImage2 = pygame.image.load('bbb.png')

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

def car(img,x,y):
	gameDisplay.blit(img,(x,y))



x = (display_width * 0.45)
y = (display_height * 0.8)

x1 = (display_width * 0.65)
y1 = (display_height * 0.8)

x_changeA = 0
y_changeA = 0

x_changeB = 0
y_changeB = 0




def gameA():
	global x,y,x_changeA,x_changeB,x1,y1,y_changeB,y_changeA
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_changeA =- 5

			if event.key == pygame.K_RIGHT:
				x_changeA =+ 5

			if event.key == pygame.K_UP:
				y_changeA =- 5

			if event.key == pygame.K_DOWN:
				y_changeA =+ 5

		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP):
				x_changeA = 0
				y_changeA = 0

	x += x_changeA
	y += y_changeA




	#gameDisplay.fill(black)
	car(carImage1,x,y)
	##pygame.display.flip()
	#clock.tick(60)



###################################

def gameB():
	global x,y,x_changeA,x_changeB,x1,y1,y_changeB,y_changeA
	for event in pygame.event.get():
		print(event)
		if(event.type == pygame.QUIT):
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_a:
				x_changeB =- 5

			if event.key == pygame.K_d:
				x_changeB =+ 5

			if event.key == pygame.K_w:
				y_changeB =- 5

			if event.key == pygame.K_s:
				y_changeB =+ 5	


		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_w):
				x_changeB = 0
				y_changeB = 0

	x1 += x_changeB
	y1 += y_changeB


	#gameDisplay.fill(black)
	car(carImage2,x1,y1)
	#pygame.display.flip()
	#clock.tick(60)

##################################	



def gameLoop():



	game_exit = False

	while not game_exit:
		gameDisplay.fill(black)
		#gameB()
		#gameA()
		Thread(target = gameA).start()
		Thread(target = gameB).start()



		pygame.display.flip()
		clock.tick(60)
    	


gameLoop()
pygame.quit()
quit()
