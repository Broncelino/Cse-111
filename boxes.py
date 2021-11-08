items = int(input("how many items do you have? "))
box = int(input("how many items can you put in each box? "))
boxes = items/box

if items%box == 0:
    print(round(int(boxes)))
else:
    print(int(boxes)+1)
