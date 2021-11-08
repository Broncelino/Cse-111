import datetime
day = datetime.datetime.today().weekday()
cost = float(input("what is the subtotal? "))
if day == 1 or day == 2 and cost >= 50:
    disc = cost/100*10
    cost = cost-disc
    print("discount is $" +str(disc))
tax = cost*.06
final = cost+tax
print("the cost after $"+str(tax)+" in sales tax is $" + str(round(final,2)))