
# task3c/S3_PIPE_02.py

def compose(*fns):
    """
    Returns a function that applies a series of unary functions from right-to-left.
    Example: compose(f, g, h)(x) == f(g(h(x))).
    """
    def composed_function(arg):
        result = arg
        # Apply functions in reverse order
        for fn in reversed(fns):
            result = fn(result)
        return result
    return composed_function

def pipe(*fns):
    """
    Helper function (copied from S3_PIPE_01) to compare against compose.
    Applies functions from left-to-right.
    """
    def piped_function(arg):
        result = arg
        for fn in fns:
            result = fn(result)
        return result
    return piped_function

def test_compose():
    """
    Tests the compose function and compares its results with pipe.
    """
    print("--- Testing Compose Function ---")

    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    square = lambda x: x * x

    # Compose: f(g(h(x))) -> add_one(multiply_by_two(square(x)))
    composed_pipeline = compose(add_one, multiply_by_two, square)
    initial_value = 2
    composed_result = composed_pipeline(initial_value)
    # Expected: square(2) = 4, multiply_by_two(4) = 8, add_one(8) = 9
    expected_composed = 9
    print(f"Compose(add_one, multiply_by_two, square)({initial_value}) -> {composed_result} (Expected: {expected_composed})")
    assert composed_result == expected_composed

    # Compare with Pipe: h(g(f(x))) -> square(multiply_by_two(add_one(x)))
    piped_pipeline = pipe(add_one, multiply_by_two, square)
    piped_result = piped_pipeline(initial_value)
    # Expected: add_one(2) = 3, multiply_by_two(3) = 6, square(6) = 36
    expected_piped = 36
    print(f"Pipe(add_one, multiply_by_two, square)({initial_value}) -> {piped_result} (Expected: {expected_piped})")
    assert piped_result == expected_piped

    print("\n# Comparison: Pipe applies functions in the order they are given (f then g then h).")
    print("# Compose applies functions in reverse order (h then g then f) from the mathematical definition.")

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_compose()
