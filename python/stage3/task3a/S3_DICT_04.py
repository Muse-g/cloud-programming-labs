
# task3a/S3_DICT_04.py

def omit(d, keys_to_omit):
    """
    Creates a new dictionary that excludes the keys specified in the 
    'keys_to_omit' list.
    """
    # 1. Use a dictionary comprehension.
    # 2. Iterate through all key-value pairs in the original dictionary 'd'.
    # 3. Include a key-value pair only if the key is NOT in the 'keys_to_omit' list.
    return {key: value for key, value in d.items() if key not in keys_to_omit}

def test_omit():
    """
    Tests the omit function.
    """
    print("--- Testing Dictionary Key Omitting ---")

    source_dict = {
        "id": 123,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "active": True
    }
    
    keys_to_omit = ["email", "active", "password"] # "password" does not exist

    expected_dict = {
        "id": 123,
        "name": "John Doe"
    }

    omitted_dict = omit(source_dict, keys_to_omit)

    print(f"Source:   {source_dict}")
    print(f"To Omit:  {keys_to_omit}")
    print(f"Omitted:  {omitted_dict}")
    print(f"Expected: {expected_dict}")

    assert omitted_dict == expected_dict, "Test failed!"
    print("\nTest passed!")

if __name__ == "__main__":
    test_omit()
