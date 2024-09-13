# Function to add a gold ingot to the purse
def add_ingot(purse: dict) -> dict:
    # Create a copy of the purse to avoid modifying the original
    new_purse = purse.copy()
    
    # Check if "gold_ingots" is in the purse, if not, initialize with 0
    if "gold_ingots" not in new_purse:
        new_purse["gold_ingots"] = 0
    
    # Add one gold ingot
    new_purse["gold_ingots"] += 1
    return new_purse

# Function to get (remove) a gold ingot from the purse
def get_ingot(purse: dict) -> dict:
    # Create a copy of the purse to avoid modifying the original
    new_purse = purse.copy()
    
    # Check if there are any gold ingots in the purse
    if new_purse.get("gold_ingots", 0) > 0:
        # Remove one gold ingot
        new_purse["gold_ingots"] -= 1
    
    # If all gold ingots are taken, remove the key
    if new_purse.get("gold_ingots", 0) == 0:
        new_purse.pop("gold_ingots", None)
    
    return new_purse

# Function to empty the purse
def empty(purse: dict) -> dict:
    # Return an empty dictionary (a new object)
    return {}

# Test cases (run only when the script is executed directly)
if __name__ == "__main__":
    # Initial empty purse
    purse = {}
    
    # Test empty purse
    print(f"Initial purse: {purse}")
    print(f"Empty purse: {empty(purse)}")

    # Adding ingots
    purse = add_ingot(purse)
    print(f"After adding 1 ingot: {purse}")
    purse = add_ingot(purse)
    print(f"After adding another ingot: {purse}")

    # Getting ingots
    purse = get_ingot(purse)
    print(f"After getting 1 ingot: {purse}")
    purse = get_ingot(purse)
    print(f"After getting another ingot: {purse}")
    purse = get_ingot(purse)
    print(f"After trying to get from empty purse: {purse}")

    # Emptying the purse
    purse = empty(purse)
    print(f"After emptying the purse: {purse}")
