import time
from threading import Thread 

seconds = 60
def timeCount():
	global seconds
	while(seconds > 0):
		print("seconds", seconds)
		time.sleep(1)
		seconds -= 1

def avi():
	print("time")


Thread(target = timeCount).start()
avi()