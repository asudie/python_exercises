import threading
import time
import random

class Screwdriver:
    def __init__(self):
        self.lock = threading.Lock()

class Doctor(threading.Thread):
    def __init__(self, number, left_screwdriver, right_screwdriver):
        super().__init__()
        self.number = number
        self.left_screwdriver = left_screwdriver
        self.right_screwdriver = right_screwdriver

    def run(self):
        self.try_to_blast()

    def try_to_blast(self):
        with self.left_screwdriver.lock:
            with self.right_screwdriver.lock:
                self.blast()

    def blast(self):
        print(f"Doctor {self.number}: BLAST!")
        time.sleep(random.uniform(0.1, 1.0))

def main():
    screwdrivers = [Screwdriver() for _ in range(5)]

    doctors = [
        Doctor(9, screwdrivers[0], screwdrivers[1]),
        Doctor(10, screwdrivers[1], screwdrivers[2]),
        Doctor(11, screwdrivers[2], screwdrivers[3]),
        Doctor(12, screwdrivers[3], screwdrivers[4]),
        Doctor(13, screwdrivers[4], screwdrivers[0]),
    ]

    for doctor in doctors:
        doctor.start()

    for doctor in doctors:
        doctor.join()

    print("Experiment over!")

if __name__ == '__main__':
    main()
