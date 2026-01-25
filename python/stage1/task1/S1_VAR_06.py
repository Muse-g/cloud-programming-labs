
# task1/S1_VAR_06.py

def to_int_or_none(s):
    """
    Safely converts a string to an integer, returning None if conversion fails.
    Handles None input gracefully.
    """
    # 1. Handle None input
    if s is None:
        return None
    
    # 2. Try to convert the string to an integer
    try:
        # Using float first to handle string representations of floats, e.g., "12.0"
        # then converting to int. If you only want to parse strings that look
        # like integers, you can just use int(s).
        return int(float(s.strip()))
    except (ValueError, TypeError):
        # ValueError for bad conversions like "12x"
        # TypeError if 's' is not a string or number
        return None

def test_safe_conversion():
    """
    Tests the to_int_or_none function with various inputs.
    """
    test_cases = ["12", " 12 ", "12.0", "12.5", "12x", "", None, " -5 "]

    print("--- Testing Safe Integer Conversion ---")
    for case in test_cases:
        result = to_int_or_none(case)
        print(f"Input: {repr(case):<8} -> Output: {result}")

if __name__ == "__main__":
    test_safe_conversion()
