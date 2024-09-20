class Key:
    def __init__(self):
        self.passphrase = "zax2rulez"
    
    def __len__(self):
        # This makes len(key) return 1337
        return 1337
    
    def __getitem__(self, index):
        # This makes key[404] return 3
        if index == 404:
            return 3
        raise IndexError("Key only has the 404th element.")

    def __gt__(self, other):
        # This makes key > 9000 true
        return other < 9000

    def __str__(self):
        # This makes str(key) return "GeneralTsoKeycard"
        return "GeneralTsoKeycard"

# Testing the assertions
if __name__ == "__main__":
    key = Key()
    assert len(key) == 1337, "Length of key is not 1337!"
    assert key[404] == 3, "404th element of key is not 3!"
    assert key > 9000, "Key is not greater than 9000!"
    assert key.passphrase == "zax2rulez", "Passphrase is incorrect!"
    assert str(key) == "GeneralTsoKeycard", "String representation is incorrect!"
    print("All tests passed!")
