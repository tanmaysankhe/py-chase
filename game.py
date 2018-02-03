import pygame
import time
from threading import Thread

pygame.init()

#variables 

display_width =800
display_height =600
object_size = 67

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
seconds = 1


tom = pygame.image.load('Images/tom.png')
jerry = pygame.image.load('Images/jerry.png')

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Chase')
clock = pygame.time.Clock()


###########################################
def timeCount():
	global seconds
	while(seconds > 0):
		#print(seconds)
		time.sleep(1)
		seconds += 1
		print(seconds)


def jerrywins():
	message_display("Jerry Wins")




def button(msg,x,y,w,h,c,action=None):
		
	pygame.draw.rect(gameDisplay,c,(x,y,w,h))
	# pygame.draw.rect(gameDisplay,green,(250,450,100,50))
	# pygame.draw.rect(gameDisplay,red,(450,450,100,50))

	mouse = pygame.mouse.get_pos()

	click = pygame.mouse.get_pressed()

	if(mouse[0] > x and mouse[0] < x+100):
		if(mouse[1] > y and mouse[1] < y+50):
			pygame.draw.rect(gameDisplay,blue,(x,y,w,h))
			if click[0] == 1:
				if action == 'play':
					
					gameLoop()

				if action == 'quit':
					pygame.quit()
					quit()

	# if (450 < mouse[0] < 550 and 450 < mouse[1] < 500):
	# 	pygame.draw.rect(gameDisplay,blue,(450,450,100,50))					

	smallText = pygame.font.Font('freesansbold.ttf',20)

	TextSurf, TextRect = text_objects(msg, smallText)
	TextRect.center = ((x+50,y+28))
	gameDisplay.blit(TextSurf, TextRect)		


def timer(count):
	font = pygame.font.SysFont(None,25)
	text = font.render("Time:" + str(count),True,red)
	gameDisplay.blit(text,(0,0))




def car(x,y):
	gameDisplay.blit(carImg,(x,y))

def tomwins():
	message_display("Tom wins")


def game_intro():
	#t.stop()
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf',115)
		TextSurf, TextRect = text_objects("The Chase", largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf, TextRect)
		
		
		#button(msg,x,y,w,h,c):
		button("Start",250,450,100,50,green,'play')
		button("Exit",450,450,100,50,red,'quit')


		pygame.display.update()
		clock.tick(60)



def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)

	game_intro()

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()


###########################################





def car(img,x,y):
	gameDisplay.blit(img,(x,y))



def gameLoop():
	x = (display_width * 0.3) - object_size
	y = (display_height * 0.8)

	x1 = (display_width * 0.7)
	y1 = (display_height * 0.8)

	x_changeA = 0
	y_changeA = 0

	x_changeB = 0
	y_changeB = 0
	i = 0

	game_exit = False

	while not game_exit:
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				t.stop()
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

				if event.key == pygame.K_a:
					x_changeB =- 5

				if event.key == pygame.K_d:
					x_changeB =+ 5

				if event.key == pygame.K_w:
					y_changeB =- 5

				if event.key == pygame.K_s:
					y_changeB =+ 5	


			if event.type == pygame.KEYUP:
				if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP or
				 event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_w):
					x_changeA = 0
					y_changeA = 0
					x_changeB = 0
					y_changeB = 0

		x += x_changeA
		y += y_changeA

		x1 += x_changeB
		y1 += y_changeB

		
		if( x1 < x < x1+object_size or x1 < x+object_size < x1+object_size):
			if(y1 < y < y1+object_size or y1 < y+object_size < y1+object_size):
				#print("crash",i)
				#i+=1
				
				tomwins()

		if (x < 5 or x+object_size > 795 or y < 20 or y+object_size > 595):
			jerrywins()		


		if (x1 < 5 or x1+object_size > 795 or y1 < 20 or y1+object_size > 595):
			tomwins()		


		if(seconds > 10000):
			jerrywins()


		gameDisplay.fill(white)

		#borders
		pygame.draw.line(gameDisplay,red,(5,20),(5,595),1)
		pygame.draw.line(gameDisplay,red,(5,20),(795,20),1)
		pygame.draw.line(gameDisplay,red,(795,20),(795,595),1)
		pygame.draw.line(gameDisplay,red,(5,595),(795,595),1)

		car(tom,x,y)
		car(jerry,x1,y1)

		#t = Thread(target = timeCount).start()
		timer(seconds)
		pygame.display.flip()
		clock.tick(60)

game_intro()

pygame.quit()
quit()
