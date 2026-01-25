
# task2b/S2_FOR_02.py

def find_first_even(nums):
    """
    Returns the first even number in a list of numbers.
    If no even number is found, it returns None.
    Uses a for loop and does not use next() with a generator.
    """
    # 1. Loop through each number in the list
    for num in nums:
        # 2. Check if the number is even
        if num % 2 == 0:
            # 3. If it is, return it immediately (early stop)
            return num
    
    # 4. If the loop completes without finding an even number, return None
    return None

def test_find_first_even():
    """
    Tests the find_first_even function.
    """
    print("--- Testing Find First Even ---")
    
    # Test case 1: Even number present
    data1 = [1, 3, 5, 8, 9, 10]
    expected1 = 8
    result1 = find_first_even(data1)
    print(f"Input: {data1} -> First Even: {result1} (Expected: {expected1})")
    assert result1 == expected1

    # Test case 2: No even numbers
    data2 = [1, 3, 5, 7, 9]
    expected2 = None
    result2 = find_first_even(data2)
    print(f"Input: {data2} -> First Even: {result2} (Expected: {expected2})")
    assert result2 == expected2

    # Test case 3: First number is even
    data3 = [10, 2, 4, 6]
    expected3 = 10
    result3 = find_first_even(data3)
    print(f"Input: {data3} -> First Even: {result3} (Expected: {expected3})")
    assert result3 == expected3
    
    # Test case 4: Empty list
    data4 = []
    expected4 = None
    result4 = find_first_even(data4)
    print(f"Input: {data4} -> First Even: {result4} (Expected: {expected4})")
    assert result4 == expected4

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_find_first_even()
