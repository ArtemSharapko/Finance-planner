# Create a master account
print("Hi, I am your Financial planner, I will help you with the organization of your finances!")
m = "master"
a = input("Enter the amount: ")
n = input("Enter the name of the account: ")
try:
    ma = float(a)
except:
    print("You entered an incorrect amount, enter a numeric value!")
    exit()

if n == m:
    mn = n
else:
    print("You have entered an incorrect account name, will enter a name from the provided options!")
    exit()

print(ma, mn)