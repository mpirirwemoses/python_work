class BankAccount:
    def __init__(self, account_number, balance, card_number):
        self.account_number = account_number
        self.balance = balance
        self.card_number = card_number

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self):
        withdraw_amount = int(input("Enter amount to withdraw: "))
        if withdraw_amount > self.balance:
            print(f"Insufficient funds. Balance: {self.balance}")
        else:
            self.balance -= withdraw_amount
            print(f"Transaction successful. New balance: {self.balance}")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

def main():
    account = BankAccount("123456", 5000, "987654")
    while True:
        print("\n1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            account.withdraw()
        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()
