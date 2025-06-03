def withdraw():
    print("Withdraw function called")

def deposit():
    print("Deposit function called")

def check_balance():
    print("Check balance function called")

actions = {
    1: withdraw,
    2: deposit,
    3: check_balance
}
print(actions)
choice = int(input("Enter your choice: "))
action = actions.get(choice)

if action:
    action()
else:
    print("Invalid choice")
    #add
