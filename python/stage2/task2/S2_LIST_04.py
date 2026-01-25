
# task2/S2_LIST_04.py

def flatten1(nested_list):
    """
    Flattens a list by exactly one level.
    Does not use any itertools functions.
    """
    flat_list = []
    for item in nested_list:
        # 1. Check if the item is a list
        if isinstance(item, list):
            # If it's a list, extend the new list with its elements
            flat_list.extend(item)
        else:
            # If it's not a list, just append the item itself
            flat_list.append(item)
    return flat_list

def test_flattening():
    """
    Tests the flatten1 function.
    """
    print("--- Testing One-Level List Flattening ---")

    # Test case 1: Mixed items and lists
    test_data1 = [1, [2, 3], 4, [5, 6, 7], 8]
    expected1 = [1, 2, 3, 4, 5, 6, 7, 8]
    result1 = flatten1(test_data1)
    print(f"Input:    {test_data1}")
    print(f"Flattened: {result1}")
    print(f"Expected:  {expected1}")
    assert result1 == expected1

    # Test case 2: Includes nested lists (should only flatten one level)
    test_data2 = [1, [2, [3, 4]], 5]
    expected2 = [1, 2, [3, 4], 5]
    result2 = flatten1(test_data2)
    print(f"\nInput:    {test_data2}")
    print(f"Flattened: {result2}")
    print(f"Expected:  {expected2}")
    assert result2 == expected2
    
    # Test case 3: No nested lists
    test_data3 = [1, 2, 3, 4, 5]
    expected3 = [1, 2, 3, 4, 5]
    result3 = flatten1(test_data3)
    print(f"\nInput:    {test_data3}")
    print(f"Flattened: {result3}")
    print(f"Expected:  {expected3}")
    assert result3 == expected3

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_flattening()
