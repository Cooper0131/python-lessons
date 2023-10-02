people = int(input("number in party"))
cost = int(input("meal cost"))
t1 = "$" + str(round(cost * float("1.15")))
t2 = t1.format("1.20")
t3 = t1.format("1.25")
if people > 8:
    print("For parties greater than 8 a 20% tip is automatically added, your total is " + t2)
else:
    print("tip options are:")
    print(t1)
    print(t2)
    print(t3)

