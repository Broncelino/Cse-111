import random

def append_random_numbers(number_list, quantity):
    for i in range(quantity):
        number_list.append(round(random.uniform(0,10),1))

def main():
    randnums = [40.6,12.6,86.5] 
    print(randnums)
    append_random_numbers(randnums,1)
    print(randnums)
    append_random_numbers(randnums,2)
    print(randnums)

main()