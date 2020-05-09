def fun(Number):
    Sum = 0
    while(Number > 0):
        Reminder = Number % 10
        Sum = Sum + Reminder
        Number = Number //10
    return Sum

Number = int(input("Please Enter any Number: "))
Sum = fun(Number)
print("\n Sum=",Sum)