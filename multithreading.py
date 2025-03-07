import threading
import time

# Function to be executed by threads
def print_numbers():
    for i in range(1, 6):
        print(f"Thread {threading.current_thread().name}: {i}")
        time.sleep(1)  # Simulating some work

# Creating multiple threads
thread1 = threading.Thread(target=print_numbers, name="Thread-1")
thread2 = threading.Thread(target=print_numbers, name="Thread-2")

# Starting the threads
thread1.start()
thread2.start()

# Waiting for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished execution!")
