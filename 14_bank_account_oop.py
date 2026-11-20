
# Bank Account System Using OOP

class BankAccount:

    def __init__(self, name, balance=0):

        self.name = name
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            print("Amount deposited successfully.")

        else:

            print("Invalid deposit amount.")

    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid withdrawal amount.")

        elif amount > self.balance:

            print("Insufficient balance.")

        else:

            self.balance -= amount

            print("Amount withdrawn successfully.")

    def display_balance(self):

        print("Account Holder:", self.name)

        print("Available Balance:", self.balance)


# Creating an object

name = input("Enter account holder name: ")

account = BankAccount(name)


while True:

    print("\n===== BANK ACCOUNT SYSTEM =====")

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        amount = float(input("Enter deposit amount: "))

        account.deposit(amount)

    elif choice == "2":

        amount = float(input("Enter withdrawal amount: "))

        account.withdraw(amount)

    elif choice == "3":

        account.display_balance()

    elif choice == "4":

        print("Thank you for using our bank system.")

        break

    else:

        print("Invalid choice.")
