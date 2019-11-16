# import time
# def timer():
#    now = time.localtime(time.time())
#    return now[5]

# run = raw_input("Start? > ")
# while run == "start":
#    minutes = 0
#    current_sec = timer()
#    #print current_sec
#    if current_sec == 59:
#       mins = minutes + 1
#       print (">>>>>>>>>>>>>>>>>>>>>", mins)

# number = [5,27,5,25,12]
# max = number[0]
# for max in (number):
#    if number > max:
#       max = number

# print(max)

def makearrayconsecutive(statues):
  # Result array
  result_array = []
  #Find max number of the array
  max_num = max(statues)
  #Find min number of the array
  min_num = min(statues)
  # Iterate from min to max
  for i in range(min_num,max_num):
    if i not in statues:
      result_array.append(i)

  result = len(result_array)
  print(result)

print(makearrayconsecutive([6,3]))

