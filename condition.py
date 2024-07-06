a = int(input("Enter a number : "))
if (a % 3 == 0) & (a % 5 == 0):
    print("divisible by both 3 and 5")
elif a % 3 == 0:
    print(a % 3)
elif a % 3 == 0:
    print(a % 5)
else:
    print("not divisible by any of those 3 or 5")