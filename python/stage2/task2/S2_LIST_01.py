
# task2/S2_LIST_01.py

def clean_numbers(values):
    """
    Cleans a list of string values.
    - Trims each string.
    - Converts it to a float.
    - Drops any item that fails conversion.
    """
    cleaned_list = []
    for value in values:
        if isinstance(value, str):
            try:
                # 1. Trim whitespace and convert to float
                num = float(value.strip())
                cleaned_list.append(num)
            except ValueError:
                # 2. Skip items that cannot be converted
                continue
    return cleaned_list

def test_clean_numbers():
    """
    Tests the clean_numbers function.
    """
    test_data = [" 1 ", "x", "2.5", " -3.0 ", "a1", "1.0e2"]
    expected = [1.0, 2.5, -3.0, 100.0]
    
    print("--- Testing Number String Cleaning ---")
    result = clean_numbers(test_data)
    print(f"Input:    {test_data}")
    print(f"Cleaned:  {result}")
    print(f"Expected: {expected}")
    
    assert result == expected, "Test failed!"
    print("\nTest passed!")

if __name__ == "__main__":
    test_clean_numbers()
