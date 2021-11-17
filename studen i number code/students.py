def main():
    num = input("What is the I number you want to look up? ")
    look_name(num,read_dict())
    #print(read_dict())



def read_dict():
    f = open("C:/Users/bsojn/programs/studen i number code/students.csv","r")
    lines = f.readlines()
    number_list=[]
    for line in lines:
        name = line.split(",")
        dictionary={}
        dictionary[name[0]]=name[1].rstrip("\n")
        number_list.append(dictionary)
    number_list.pop(0)
    return(number_list)



def look_name(num, list):
    for i in list:
        if num in i:
            print(i[num])






main()

