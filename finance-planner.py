# Create a master account
print("Hi, I am your Financial planner, I will help you with the organization of your finances!")
print("In order for me to save your data, you need to enter the amount and name of the account: 'master' for the main account; the 'wish' to raise money to buy something you really want; 'storage' this is your extra account on which you put money to buy something in the future")
print("You can only use the following account names: ")
print("master")
print("wish")
print("storage")
m = "master"
w = "wish"
s = "storage"
a = input("Enter the amount: ")
n = input("Enter the name of the account: ")
try:
    ma = float(a)
except:
    print("You entered an incorrect amount, enter a numeric value!")
    exit()

if n == m:
    mn = n
elif n == w:
    mn = n 
elif n == s:
    mn = n    
else:
    print("You have entered an incorrect account name, will enter a name from the provided options!")
    exit()

print(ma, mn)