import threading
import time
import random

# Simulate preparing food
def prepare_order(order_id):
    preparation_time = random.randint(2, 5)  # Simulating preparation time between 2 to 5 seconds
    print(f"Order {order_id}: Preparing food... (This will take {preparation_time} seconds)")
    time.sleep(preparation_time)  # Simulate food preparation time
    print(f"Order {order_id}: Food prepared. Ready for delivery!")

# Function to simulate receiving an order
def receive_order(order_id):
    print(f"Order {order_id}: Received and being processed...")
    thread = threading.Thread(target=prepare_order, args=(order_id,))
    thread.start()  # Start a new thread for preparing the order

def main():
    print("Welcome to the Food Ordering System!")
    orders_to_process = 5  # Number of orders to simulate
    for i in range(1, orders_to_process + 1):
        receive_order(i)
        time.sleep(random.randint(1, 3))  # Simulate delay between orders (random)

    print("All orders are being processed...")

if __name__ == "__main__":
    main()
