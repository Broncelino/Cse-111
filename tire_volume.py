import os
import math
import datetime
day = datetime.datetime.now()
w = float(input("enter the width "))
a = float(input("enter the aspect ratio "))
d = float(input("enter the diameter "))
v = round((math.pi*w*w*a*(w*a+2540*d))/10000000000,2)
empty = os.path.getsize('volumes.txt')

with open('volumes.txt',"at") as f:
    if empty > 0:
        f.write("\n"+str(day.strftime("%x"))+", "+str(int(w))+", "+str(int(a))+", "+str(int(d))+", "+str(v))
    else:
        f.write(str(day.strftime("%x"))+", "+str(int(w))+", "+str(int(a))+", "+str(int(d))+", "+str(v))
f.close()
print("the volume in the tire is about "+str(v)+" liters")