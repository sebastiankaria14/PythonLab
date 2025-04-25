#without lock
import threading
import time

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # Withdraw function without locking (this will demonstrate a race condition)
    def withdraw(self, amount):
        if self.balance >= amount:
            print(f"Withdrawal of {amount} is being processed.")
            time.sleep(0.1)  # Simulate delay in processing
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance!")

def customer(bank_account, amount):
    bank_account.withdraw(amount)

def main():
    account = BankAccount(1000)  # Initial balance is 1000

    # Create two threads simulating two customers withdrawing money
    thread1 = threading.Thread(target=customer, args=(account, 600))
    thread2 = threading.Thread(target=customer, args=(account, 500))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print(f"Final balance: {account.balance}")

if __name__ == "__main__":
    main()


#with Lock
import threading
import time

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()  # Create a lock for synchronizing access to the balance

    # Withdraw function with a lock to prevent race conditions
    def withdraw(self, amount):
        with self.lock:  # Locking to ensure that only one thread can modify the balance at a time
            if self.balance >= amount:
                print(f"Withdrawal of {amount} is being processed.")
                time.sleep(0.1)  # Simulate delay in processing
                self.balance -= amount
                print(f"Withdrawal of {amount} successful. Remaining balance: {self.balance}")
            else:
                print("Insufficient balance!")

def customer(bank_account, amount):
    bank_account.withdraw(amount)

def main():
    account = BankAccount(1000)  # Initial balance is 1000

    # Create two threads simulating two customers withdrawing money
    thread1 = threading.Thread(target=customer, args=(account, 600))
    thread2 = threading.Thread(target=customer, args=(account, 500))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print(f"Final balance: {account.balance}")

if __name__ == "__main__":
    main()
