#movie ticket price calculator
age = int(input("Enter your age"))
if age<18:
    print("Your ticket price is $8.")
elif age>=18 and age<=60:
    mbs_stat = input("Do you have an member ship (Yes/no)").lower()
    if mbs_stat == "yes":
        print("Your ticket price is $10.")
    else:
        print("Your ticket price is $12.")
elif age>60:
    print("Your ticket price is $6.")

