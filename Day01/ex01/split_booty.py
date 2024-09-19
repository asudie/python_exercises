# from Day01.ex00.ingots import add_ingot, empty
from ..ex00.ingots import add_ingot, empty

def split_booty(*purses: dict) -> tuple:
    # Step 1: Calculate the total number of gold ingots
    total_gold = sum(purse.get("gold_ingots", 0) for purse in purses)
    
    # Step 2: Create three empty purses
    purse1, purse2, purse3 = empty({}), empty({}), empty({})
    
    # Step 3: Distribute the gold as evenly as possible
    for _ in range(total_gold):
        if purse1.get("gold_ingots", 0) <= purse2.get("gold_ingots", 0) and purse1.get("gold_ingots", 0) <= purse3.get("gold_ingots", 0):
            purse1 = add_ingot(purse1)
        elif purse2.get("gold_ingots", 0) <= purse1.get("gold_ingots", 0) and purse2.get("gold_ingots", 0) <= purse3.get("gold_ingots", 0):
            purse2 = add_ingot(purse2)
        else:
            purse3 = add_ingot(purse3)
    
    # Step 4: Return the three new purses
    return purse1, purse2, purse3

# Test cases (run only when the script is executed directly)
if __name__ == "__main__":
    purse1 = {"gold_ingots": 3, "apples": 10}
    purse2 = {"gold_ingots": 2}
    purse3 = {"stones": 5}
    
    result = split_booty(purse1, purse2, purse3)
    print(result)
    
    purse4 = {"gold_ingots": 7}
    purse5 = {"gold_ingots": 4}
    
    result = split_booty(purse4, purse5)
    print(result)

# python -m Day01.ex01.split_booty