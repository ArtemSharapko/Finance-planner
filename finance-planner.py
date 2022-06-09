# Create a master account
nmast = None
nwish = None
nstor = None
print("Hi, I am your Financial planner, I will help you with the organization of your finances!")
print("if you want ADD amount to your account press: 1")
print("if you want LOOK on our balance account press: 2")
print("if you want END the program press 3")
comm =input("Press key: ")
if comm == "1":
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
        nmast = [mn, ma]
    elif n == w:
        mn = n
        nwish = [mn, ma]
    elif n == s:
        mn = n 
        nstor = [mn, ma]   
    else:
        print("You have entered an incorrect account name, will enter a name from the provided options!")
        exit()
    print(ma, mn)
elif comm == "2":
    print(nmast, nwish, nstor)
elif comm == "3":
    exit()

#Print("You can continue program")
#print("if you want add amount to your account press: 1")
#print("if you want look on our balance account press: 2")
#print("if you want END the program press 3")









