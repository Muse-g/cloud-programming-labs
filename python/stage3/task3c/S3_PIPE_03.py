
# task3c/S3_PIPE_03.py
import re # For collapsing multiple spaces

def pipe(*fns):
    """
    Helper function (copied from S3_PIPE_01) to build the pipeline.
    Applies functions from left-to-right.
    """
    def piped_function(arg):
        result = arg
        for fn in fns:
            result = fn(result)
        return result
    return piped_function

def normalize_string(text):
    """
    Normalizes a string by stripping whitespace, converting to lowercase,
    and collapsing multiple internal spaces to a single space.
    """
    # 1. Define the individual transformation functions
    f_strip = lambda s: s.strip()
    f_lower = lambda s: s.lower()
    # Use re.sub to replace one or more spaces with a single space
    f_collapse_spaces = lambda s: re.sub(r'\s+', ' ', s)

    # 2. Build the pipeline
    # The order is crucial: strip first, then lowercase, then collapse spaces
    pipeline = pipe(f_strip, f_lower, f_collapse_spaces)

    # 3. Apply the pipeline
    return pipeline(text)

def test_string_normalization():
    """
    Tests the string normalization pipeline.
    """
    print("--- Testing String Normalization Pipeline ---")

    test_string = "  Ala   Ma  Kota  "
    expected_string = "ala ma kota"
    
    result = normalize_string(test_string)
    
    print(f"Original string: '{test_string}'")
    print(f"Normalized string: '{result}' (Expected: '{expected_string}')")
    
    assert result == expected_string, "Test failed!"
    print("\nTest passed!")

    test_string_2 = "   HELLO   WORLD   PYTHON   "
    expected_string_2 = "hello world python"
    result_2 = normalize_string(test_string_2)
    print(f"Original string: '{test_string_2}'")
    print(f"Normalized string: '{result_2}' (Expected: '{expected_string_2}')")
    assert result_2 == expected_string_2, "Test 2 failed!"
    print("\nTest 2 passed!")


if __name__ == "__main__":
    test_string_normalization()
