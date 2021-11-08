def num_rect():
    return int(input("how many rectangles: "))
def dimention_get():
    l = float(input("what's the length: "))
    w = float(input("what's the width: "))
    return l*w
def adding_area(areas):
    total = 0
    for i in range(len(areas)):
        total = total + areas[i]
    return total
def main():
    areas = []
    loops = num_rect()
    for i in range(loops):
        areas.append(dimention_get())
    print(adding_area(areas))
main()




