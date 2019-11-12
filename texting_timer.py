import time
def timer():
   now = time.localtime(time.time())
   return now[5]

run = raw_input("Start? > ")
while run == "start":
   minutes = 0
   current_sec = timer()
   #print current_sec
   if current_sec == 59:
      mins = minutes + 1
      print (">>>>>>>>>>>>>>>>>>>>>", mins)

