
# task3a/S3_DICT_05.py

def invert(d):
    """
    Inverts a dictionary, swapping keys and values.
    If multiple keys have the same value, the new value becomes a list of the
    original keys.
    """
    inverted_dict = {}
    # 1. Iterate through the key-value pairs of the original dictionary
    for key, value in d.items():
        # 2. Check if the value is already a key in our new dictionary
        if value in inverted_dict:
            # 3. If it is, we have a collision.
            # We need to make sure the value associated with this key is a list.
            current_val = inverted_dict[value]
            if isinstance(current_val, list):
                # If it's already a list, just append the new key.
                current_val.append(key)
            else:
                # If it's not a list, create a new list with the old key and the new one.
                inverted_dict[value] = [current_val, key]
        else:
            # 4. If there's no collision, just assign the key as the new value.
            inverted_dict[value] = key
            
    return inverted_dict

def test_invert():
    """
    Tests the invert function.
    """
    print("--- Testing Dictionary Inversion with Collisions ---")

    # Test case 1: No collisions
    dict1 = {"a": 1, "b": 2, "c": 3}
    expected1 = {1: "a", 2: "b", 3: "c"}
    result1 = invert(dict1)
    print(f"Input: {dict1} -> Inverted: {result1}")
    assert result1 == expected1

    # Test case 2: With collisions
    dict2 = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    expected2 = {1: ["a", "c"], 2: ["b", "e"], 3: "d"}
    result2 = invert(dict2)
    
    # Sort lists in result for consistent comparison
    if isinstance(result2.get(1), list): result2[1].sort()
    if isinstance(result2.get(2), list): result2[2].sort()

    print(f"Input: {dict2} -> Inverted: {result2}")
    assert result2 == expected2

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_invert()
