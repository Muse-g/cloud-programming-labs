
# task3c/S3_PIPE_01.py

def pipe(*fns):
    """
    Returns a function that applies a series of unary functions from left-to-right.
    Example: pipe(f, g, h)(x) == h(g(f(x))).
    """
    def piped_function(arg):
        result = arg
        for fn in fns:
            result = fn(result)
        return result
    return piped_function

def test_pipe():
    """
    Tests the pipe function with numeric transformations.
    """
    print("--- Testing Pipe Function ---")

    # Define some simple unary functions
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    square = lambda x: x * x

    # Create a pipeline: (x + 1) * 2 ^ 2
    pipeline1 = pipe(add_one, multiply_by_two, square)

    # Test with an initial value
    initial_value1 = 2
    result1 = pipeline1(initial_value1)
    # Expected: (2 + 1) * 2 = 6, 6 * 6 = 36
    expected1 = 36
    print(f"Pipe(add_one, multiply_by_two, square)({initial_value1}) -> {result1} (Expected: {expected1})")
    assert result1 == expected1

    # Another pipeline: x * 2 + 1
    pipeline2 = pipe(multiply_by_two, add_one)
    initial_value2 = 5
    result2 = pipeline2(initial_value2)
    # Expected: 5 * 2 = 10, 10 + 1 = 11
    expected2 = 11
    print(f"Pipe(multiply_by_two, add_one)({initial_value2}) -> {result2} (Expected: {expected2})")
    assert result2 == expected2

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_pipe()
