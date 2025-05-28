import time

def check_condition():
    # Simulated function to check a condition
    return False

def busy_waiting():
    while not check_condition():
        # Busy waiting loop
        print("Waiting for condition to be met...")
        time.sleep(1)  # Sleep for 1 second before checking again

busy_waiting()
print("Condition met. Continuing...")
