def add_ingot(purse: dict) -> dict:
    new_purse = purse.copy()
    
    if "gold_ingots" not in new_purse:
        new_purse["gold_ingots"] = 0
    
    new_purse["gold_ingots"] += 1
    return new_purse

def get_ingot(purse: dict) -> dict:
    new_purse = purse.copy()
    
    if new_purse.get("gold_ingots", 0) > 0:
        new_purse["gold_ingots"] -= 1
    
    if new_purse.get("gold_ingots", 0) == 0:
        new_purse.pop("gold_ingots", None)
    
    return new_purse

def empty(purse: dict) -> dict:
    return {}

if __name__ == "__main__":
    purse = {}
    
    print(f"Initial purse: {purse}")
    print(f"Empty purse: {empty(purse)}")

    purse = add_ingot(purse)
    print(f"After adding 1 ingot: {purse}")
    purse = add_ingot(purse)
    print(f"After adding another ingot: {purse}")

    purse = get_ingot(purse)
    print(f"After getting 1 ingot: {purse}")
    purse = get_ingot(purse)
    print(f"After getting another ingot: {purse}")
    purse = get_ingot(purse)
    print(f"After trying to get from empty purse: {purse}")

    purse = empty(purse)
    print(f"After emptying the purse: {purse}")
