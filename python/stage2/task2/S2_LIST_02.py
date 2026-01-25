
# task2/S2_LIST_02.py

def unique(values):
    """
    Returns a new list with duplicates removed, preserving the order
    of the first occurrence. Does not use the set() function.
    """
    unique_list = []
    seen = []  # To keep track of items we've already added
    for item in values:
        if item not in seen:
            unique_list.append(item)
            seen.append(item)
    return unique_list

def test_unique():
    """
    Tests the unique function.
    """
    test_data = [1, 2, "a", 3, 2, "b", "a", 1, 4]
    expected = [1, 2, "a", 3, "b", 4]

    print("--- Testing Deduplication (without set) ---")
    result = unique(test_data)
    print(f"Original list: {test_data}")
    print(f"Unique list:   {result}")
    print(f"Expected:      {expected}")

    assert result == expected, "Test failed!"
    print("\nTest passed!")

if __name__ == "__main__":
    test_unique()
