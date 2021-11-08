def main():
    start = input("What were the starting miles on the odometer? ")
    end = input("What were the ending miles on the odometer? ")
    gall = input("How many gallons were used? ")
    mpg = milespg(start, end, gall)
    lt = ltp100k(mpg)
    print(str(mpg)+" miles per gallon")
    print(str(lt)+" liters per 100 kilometers")

def milespg(start,end,gall):
    return round((int(end)-int(start))/float(gall),1)
def ltp100k(mpg):
    return round(235.215/mpg,2)
main()
