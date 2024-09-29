import random
import time

# Generator function to emit pressure values
def emit_gel(step):
    pressure = 50  # Initial pressure
    current_step = random.uniform(0, step)  # Initial random step

    while True:
        # Emit the current pressure
        change = yield pressure
        
        # Reverse the step if the valve asks for it
        if change:
            current_step = -current_step
        
        # Adjust the pressure with the current step
        pressure += current_step
        current_step = random.uniform(0, step)

        # Exit if pressure is out of the safety limits
        if pressure < 10 or pressure > 90:
            print("Emergency break: Pressure out of range!")
            break

# Function to manage the valve and control pressure
def valve(gen):
    while True:
        try:
            pressure = next(gen)
            print(f"Pressure: {pressure}")

            if pressure < 20 or pressure > 80:
                # Send a signal to reverse the sign of the step
                gen.send(True)
            else:
                # Continue normally
                gen.send(False)
            
            # Adding a delay to simulate time between measurements
            time.sleep(0.5)
        
        except StopIteration:
            break

# Main function to run the system
def main():
    step = 10  # Adjust step size here
    gen = emit_gel(step)  # Initialize the generator
    
    # Prime the generator
    next(gen)
    
    # Run the valve controller
    valve(gen)

if __name__ == "__main__":
    main()
