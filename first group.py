import math
length = float(input("What's the pendulum length? "))
time = ((math.pi*2)*(math.sqrt(length/9.81)))
print(time)