import random
import time

def emit_gel(step):
    pressure = 50
    current_step = random.uniform(0, step)

    while True:
        change = yield pressure
        
        if change:
            current_step = -current_step
        
        pressure += current_step
        current_step = random.uniform(0, step)

        if pressure < 10 or pressure > 90:
            print("Emergency break: Pressure out of range!")
            break

def valve(gen):
    while True:
        try:
            pressure = next(gen)
            print(f"Pressure: {pressure}")

            if pressure < 20 or pressure > 80:
                gen.send(True)
            else:
                gen.send(False)
            
            time.sleep(0.5)
        
        except StopIteration:
            break

def main():
    step = 10
    gen = emit_gel(step)
    
    next(gen)
    
    valve(gen)

if __name__ == "__main__":
    main()
