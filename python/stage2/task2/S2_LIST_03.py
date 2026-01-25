
# task2/S2_LIST_03.py

def chunk(lst, size):
    """
    Splits a list into a list of lists, where each sublist has a
    maximum length of 'size'.
    
    Returns None if size is not a positive integer.
    """
    # 1. Validate the size parameter
    if not isinstance(size, int) or size <= 0:
        return None

    # 2. Use a list comprehension with slicing
    # The range function generates the starting indices for each chunk.
    # The step 'size' ensures we jump from one chunk start to the next.
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def test_chunking():
    """
    Tests the chunk function with various inputs.
    """
    print("--- Testing List Chunking ---")
    
    # Test case 1: Divisible list
    lst1 = [1, 2, 3, 4, 5, 6]
    size1 = 2
    expected1 = [[1, 2], [3, 4], [5, 6]]
    result1 = chunk(lst1, size1)
    print(f"Input: {lst1}, Size: {size1} -> Chunks: {result1}")
    assert result1 == expected1

    # Test case 2: Non-divisible list (last chunk is smaller)
    lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
    size2 = 3
    expected2 = [[1, 2, 3], [4, 5, 6], [7, 8]]
    result2 = chunk(lst2, size2)
    print(f"Input: {lst2}, Size: {size2} -> Chunks: {result2}")
    assert result2 == expected2

    # Test case 3: Size larger than list
    lst3 = [1, 2, 3]
    size3 = 5
    expected3 = [[1, 2, 3]]
    result3 = chunk(lst3, size3)
    print(f"Input: {lst3}, Size: {size3} -> Chunks: {result3}")
    assert result3 == expected3

    # Test case 4: Invalid size
    lst4 = [1, 2, 3]
    size4 = 0
    expected4 = None
    result4 = chunk(lst4, size4)
    print(f"Input: {lst4}, Size: {size4} -> Result: {result4}")
    assert result4 == expected4

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_chunking()
