
# task3b/S3_LAM_05.py

def at_least(min_value):
    """
    A higher-order function that returns a new function (a predicate).
    The returned predicate checks if a given number is greater than or
    equal to 'min_value'.
    """
    return lambda x: x >= min_value

def test_predicate_factory():
    """
    Tests the at_least higher-order function with filter().
    """
    print("--- Testing Higher-Order Predicate (at_least) ---")

    numbers = [10, 25, 5, 40, 15, 30]
    print(f"Original list: {numbers}")

    # 1. Create a predicate function to find numbers >= 20
    is_at_least_20 = at_least(20)
    
    # 2. Use this predicate with the filter() function
    filtered_numbers = list(filter(is_at_least_20, numbers))
    
    expected = [25, 40, 30]
    
    print(f"\nFiltering for numbers >= 20...")
    print(f"Result:   {filtered_numbers}")
    print(f"Expected: {expected}")
    assert filtered_numbers == expected

    # You can also use it directly inside filter for a more compact form:
    filtered_inline = list(filter(at_least(30), numbers))
    expected_inline = [40, 30]
    print(f"\nFiltering for numbers >= 30 (inline):")
    print(f"Result:   {filtered_inline}")
    print(f"Expected: {expected_inline}")
    assert filtered_inline == expected_inline

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_predicate_factory()
