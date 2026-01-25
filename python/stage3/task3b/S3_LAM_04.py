
# task3b/S3_LAM_04.py
from functools import reduce

def sum_of_squares_of_evens(nums):
    """
    Calculates the sum of the squares of even numbers in a list using
    a pipeline of filter, map, and reduce/sum.
    """
    print(f"--- Processing list: {nums} ---")

    # 1. Filter: Keep only the even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, nums))
    print(f"Step 1 (filter for evens): {even_numbers}")

    # 2. Map: Square each of the even numbers
    squared_evens = list(map(lambda x: x * x, even_numbers))
    print(f"Step 2 (map to squares):   {squared_evens}")

    # 3. Reduce (Sum): Add up all the squared numbers
    # The 'sum()' function is often a more readable alternative to reduce for simple addition.
    total = sum(squared_evens)
    print(f"Step 3 (sum):              {total}")

    # You could also use functools.reduce for the final step:
    # total_reduce = reduce(lambda acc, x: acc + x, squared_evens, 0)
    # print(f"Step 3 (reduce):           {total_reduce}")

    return total

def test_pipeline():
    """
    Tests the sum_of_squares_of_evens function.
    """
    numbers = [1, 2, 3, 4, 5, 6]
    # Expected: 2*2 + 4*4 + 6*6 = 4 + 16 + 36 = 56
    expected_result = 56
    
    result = sum_of_squares_of_evens(numbers)
    
    print(f"\nFinal Result: {result}")
    print(f"Expected:     {expected_result}")
    
    assert result == expected_result, "Test failed!"
    print("\nTest passed!")

if __name__ == "__main__":
    test_pipeline()
