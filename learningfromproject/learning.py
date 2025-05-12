import threading
import time
"""
Threading is nothing but in the sleep of 2 minutes it will do other tasks and then after 2 seconds its got executed
The main thread continues executing other tasks while the worker thread runs concurrently. This allows for background task execution without blocking the main thread.
"""

def name():
    print("working node is started")
    time.sleep(2)
    print("my name is sai murali")
thread = threading.Thread(target=name)
thread.start()

print("my task is completed running other tasks...........")
time.sleep(2)
print("my burger is going to end")