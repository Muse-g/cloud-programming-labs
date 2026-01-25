
# task3a/S3_DICT_03.py

def pick(d, keys):
    """
    Creates a new dictionary containing only the keys specified in the 'keys' list.
    If a key from the 'keys' list does not exist in the original dictionary 'd',
    it is simply ignored.
    """
    # 1. Use a dictionary comprehension for a concise solution.
    # 2. Iterate through the desired 'keys'.
    # 3. Include the key-value pair only if the key exists in the original dict 'd'.
    return {key: d[key] for key in keys if key in d}

def test_pick():
    """
    Tests the pick function.
    """
    print("--- Testing Dictionary Key Picking ---")

    source_dict = {
        "id": 123,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "active": True
    }
    
    keys_to_pick = ["id", "name", "status"] # "status" does not exist

    expected_dict = {
        "id": 123,
        "name": "John Doe"
    }

    picked_dict = pick(source_dict, keys_to_pick)

    print(f"Source:   {source_dict}")
    print(f"Keys:     {keys_to_pick}")
    print(f"Picked:   {picked_dict}")
    print(f"Expected: {expected_dict}")

    assert picked_dict == expected_dict, "Test failed!"
    print("\nTest passed!")

if __name__ == "__main__":
    test_pick()
