class Account:
    def __init__(self, acc_no, name, balance=0.0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount of {amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Amount of {amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def display(self):
        print(f"Account No: {self.acc_no}")
        print(f"Name      : {self.name}")
        print(f"Balance   : {self.balance}")
        print("-" * 30)


class Bank:
    def __init__(self):
        self.accounts = {}

    def new_account(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            print("Account already exists.")
            return
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Deposit: "))
        self.accounts[acc_no] = Account(acc_no, name, balance)
        print("New account created successfully.")

    def deposit_amount(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            amount = float(input("Enter amount to deposit: "))
            self.accounts[acc_no].deposit(amount)
        else:
            print("Account not found.")

    def withdraw_amount(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            amount = float(input("Enter amount to withdraw: "))
            self.accounts[acc_no].withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            print(f"Current Balance: {self.accounts[acc_no].balance}")
        else:
            print("Account not found.")

    def show_all_accounts(self):
        if self.accounts:
            for account in self.accounts.values():
                account.display()
        else:
            print("No accounts to display.")


# Menu-driven program
def main():
    bank = Bank()

    while True:
        print("\n====== Bank Menu ======")
        print("1. New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Show All Accounts")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            bank.new_account()
        elif choice == '2':
            bank.deposit_amount()
        elif choice == '3':
            bank.withdraw_amount()
        elif choice == '4':
            bank.check_balance()
        elif choice == '5':
            bank.show_all_accounts()
        elif choice == '6':
            print("Exiting program. Thank you.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
