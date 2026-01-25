
# task2b/S2_FOR_04.py

def count_occurrences(values):
    """
    Counts the occurrences of each item in a list and returns a
    dictionary of the counts (a histogram).
    Does not use collections.Counter.
    """
    counts = {}
    # 1. Loop through each item in the list
    for item in values:
        # 2. If the item is already a key in the dictionary, increment its value
        if item in counts:
            counts[item] += 1
        # 3. If not, add it to the dictionary with a count of 1
        else:
            counts[item] = 1
    return counts

def test_count_occurrences():
    """
    Tests the count_occurrences function.
    """
    print("--- Testing Occurrence Counter (Histogram) ---")

    test_data = ["apple", "orange", "apple", "banana", "apple", "orange"]
    expected_counts = {"apple": 3, "orange": 2, "banana": 1}

    result = count_occurrences(test_data)
    
    print(f"Input list: {test_data}")
    print(f"Counts:     {result}")
    print(f"Expected:   {expected_counts}")

    # Sort the items to ensure comparison is order-independent
    assert sorted(result.items()) == sorted(expected_counts.items()), "Test failed!"
    print("\nTest passed!")

    # Test with numbers
    test_data_2 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    expected_counts_2 = {1: 1, 2: 2, 3: 3, 4: 4}
    result_2 = count_occurrences(test_data_2)
    print(f"\nInput list: {test_data_2}")
    print(f"Counts:     {result_2}")
    print(f"Expected:   {expected_counts_2}")
    assert sorted(result_2.items()) == sorted(expected_counts_2.items()), "Test failed!"
    print("\nTest passed!")

if __name__ == "__main__":
    test_count_occurrences()
