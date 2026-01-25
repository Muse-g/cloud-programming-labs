
# task2/S2_LIST_05.py

def stats(nums):
    """
    Calculates statistics for a list of numbers.
    Returns a dictionary with min, max, avg, and sum.
    Returns None if the list is empty or invalid.
    """
    # 1. Handle empty or invalid list
    if not nums or not isinstance(nums, list):
        return None

    # Verify all items are numbers, otherwise the functions might fail
    if not all(isinstance(n, (int, float)) for n in nums):
        # Or you could filter out non-numbers, depending on requirements
        return None

    # 2. Calculate the statistics
    total_sum = sum(nums)
    count = len(nums)
    
    return {
        "min": min(nums),
        "max": max(nums),
        "sum": total_sum,
        "avg": total_sum / count,
    }

def test_stats():
    """
    Tests the stats function.
    """
    print("--- Testing List Statistics ---")

    # Test case 1: Positive integers
    data1 = [1, 2, 3, 4, 5]
    expected1 = {"min": 1, "max": 5, "sum": 15, "avg": 3.0}
    result1 = stats(data1)
    print(f"Input: {data1} -> Stats: {result1}")
    assert result1 == expected1

    # Test case 2: Including negative numbers and floats
    data2 = [-10, 0, 10, 2.5]
    expected2 = {"min": -10, "max": 10, "sum": 2.5, "avg": 0.625}
    result2 = stats(data2)
    print(f"Input: {data2} -> Stats: {result2}")
    assert result2 == expected2

    # Test case 3: Empty list
    data3 = []
    expected3 = None
    result3 = stats(data3)
    print(f"Input: {data3} -> Stats: {result3}")
    assert result3 == expected3
    
    # Test case 4: Single item list
    data4 = [100]
    expected4 = {"min": 100, "max": 100, "sum": 100, "avg": 100.0}
    result4 = stats(data4)
    print(f"Input: {data4} -> Stats: {result4}")
    assert result4 == expected4

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_stats()
