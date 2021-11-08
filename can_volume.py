import math
def main():
    cans = [
        ["#1 Picnic",6.83,10.16],
        ["#1 Tall",7.78,11.91],
        ["#2",8.73,11.59],
        ["#2.5",10.32,11.91],
        ["#3 Cylinder",10.79,17.78],
        ["#5",13.02,14.29],
        ["#6z",5.40,8.89],
        ["#8Z short",6.83,7.62],
        ["#10",15.72,17.78],
        ["#211",6.83,12.38],
        ["#300",7.62,11.27],
        ["#303",8.10,11.11]
    ]
    for i in range(len(cans)):
        #print(cans[i][0])
        vol = round(cylinder_volume(cans[i][1],cans[i][2]),3)
        sur = round(cylinder_surface_area(cans[i][1],cans[i][2]),3)
        eff = vol/sur
        
        print(str(cans[i][0])+" "+str(round(eff,2)))
    '''for can in cans:
        for canitem in can:
            print(canitem)'''

def cylinder_volume(radius,height):
    volume = math.pi*(radius**2)*height
    return volume
    


def cylinder_surface_area(radius,height):
    #Formula for cylinder surface area
    surface_area= 2*math.pi*radius*(radius+height)
    
    return surface_area


main()
