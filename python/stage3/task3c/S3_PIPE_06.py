
# task3c/S3_PIPE_06.py

def pipe_safe(*fns):
    """
    Returns a function that applies a series of unary functions from left-to-right.
    If any function in the pipeline raises an exception, the pipeline stops,
    and returns a dictionary {"ok": False, "error": "..."}.
    If all functions succeed, returns {"ok": True, "value": result}.
    """
    def safe_piped_function(arg):
        result = arg
        for fn in fns:
            try:
                result = fn(result)
            except Exception as e:
                # Capture the exception and return an error object
                return {"ok": False, "error": str(e)}
        # If all functions succeed, return the final value
        return {"ok": True, "value": result}
    return safe_piped_function

def test_safe_pipeline():
    """
    Tests the pipe_safe function with functions that can raise exceptions.
    """
    print("--- Testing Safe Pipeline (pipe_safe) ---")

    # Define some functions
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    
    def divide_by_x(divisor, value):
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return value / divisor
        
    divide_by_five = lambda x: divide_by_x(5, x)
    divide_by_zero = lambda x: divide_by_x(0, x) # This will raise an error

    # --- Test Case 1: Successful pipeline ---
    safe_pipeline_success = pipe_safe(add_one, multiply_by_two, divide_by_five)
    initial_value1 = 4
    result1 = safe_pipeline_success(initial_value1)
    # Expected: (4 + 1) * 2 / 5 = 5 * 2 / 5 = 10 / 5 = 2.0
    expected1 = {"ok": True, "value": 2.0}
    print(f"Pipeline 1 (success) on {initial_value1} -> {result1}")
    assert result1 == expected1

    # --- Test Case 2: Pipeline with an error ---
    safe_pipeline_error = pipe_safe(add_one, multiply_by_two, divide_by_zero, add_one)
    initial_value2 = 4
    result2 = safe_pipeline_error(initial_value2)
    # Expected: (4 + 1) * 2 = 10. Then divide_by_zero(10) will raise an error.
    expected2 = {"ok": False, "error": "Cannot divide by zero!"}
    print(f"Pipeline 2 (error) on {initial_value2} -> {result2}")
    assert result2 == expected2

    # --- Test Case 3: Empty pipeline ---
    empty_pipeline = pipe_safe()
    initial_value3 = "hello"
    result3 = empty_pipeline(initial_value3)
    expected3 = {"ok": True, "value": "hello"}
    print(f"Pipeline 3 (empty) on '{initial_value3}' -> {result3}")
    assert result3 == expected3
    
    print("\nAll tests passed!")

if __name__ == "__main__":
    test_safe_pipeline()
