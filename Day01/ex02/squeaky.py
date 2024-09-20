def squeaky(func):
    def wrapper(purse, *args, **kwargs):
        print("SQUEAK")
        return func(purse, *args, **kwargs)
    return wrapper

from ..ex00.ingots import add_ingot, empty, get_ingot

add_ingot = squeaky(add_ingot)
get_ingot = squeaky(get_ingot)
empty = squeaky(empty)

if __name__ == "__main__":
    purse = {"gold_ingots": 5}
    print(f"Initial purse: {purse}")

    purse = add_ingot(purse)
    print(f"After adding an ingot: {purse}")

    purse = get_ingot(purse)
    print(f"After getting an ingot: {purse}")

    purse = empty(purse)
    print(f"After emptying the purse: {purse}")
