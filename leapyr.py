year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap yr")
        else:
            print("not a leap yr")
    else:
        print("leap yr")
else:
    print("not a leap yr")pgrm1.py
