
# task3c/S3_PIPE_04.py

def iterable_pipeline(strings):
    """
    Processes a list of strings through a generator-based pipeline:
    strip -> convert to float (skip failures) -> double -> sum.
    """
    
    def strip_gen(data):
        """Strips whitespace from each string."""
        for s in data:
            if isinstance(s, str):
                yield s.strip()
            else:
                yield s # Pass non-strings through

    def to_float_gen(data):
        """Converts strings to floats, skipping failures."""
        for s_stripped in data:
            try:
                yield float(s_stripped)
            except (ValueError, TypeError):
                pass # Skip items that cannot be converted to float

    def double_gen(data):
        """Doubles each number."""
        for num in data:
            if isinstance(num, (int, float)):
                yield num * 2
            else:
                yield num # Pass non-numbers through if desired, though to_float_gen should handle

    # Build the pipeline
    # The output of one generator becomes the input of the next.
    stripped = strip_gen(strings)
    floats = to_float_gen(stripped)
    doubled = double_gen(floats)
    
    # The final step is to sum the results
    return sum(doubled)

def test_iterable_pipeline():
    """
    Tests the iterable_pipeline function.
    """
    print("--- Testing Iterable Pipeline (Generator-based) ---")

    test_data = [" 1.0 ", " 2 ", "x", "3.5", "  4.0  ", "invalid"]
    # Expected: (1.0*2) + (2*2) + (3.5*2) + (4.0*2) = 2.0 + 4.0 + 7.0 + 8.0 = 21.0
    expected_sum = 21.0
    
    print(f"Input: {test_data}")

    # Intermediate results (for demonstration, usually not explicitly materialized)
    print("\nIntermediate results (conceptual steps):")
    stripped_results = list(s.strip() for s in test_data if isinstance(s,str))
    print(f"1. Stripped: {stripped_results}")

    float_results = []
    for s in stripped_results:
        try:
            float_results.append(float(s))
        except (ValueError, TypeError):
            pass
    print(f"2. Floats (skipped failures): {float_results}")

    doubled_results = list(x * 2 for x in float_results)
    print(f"3. Doubled: {doubled_results}")

    result = iterable_pipeline(test_data)
    print(f"\nFinal sum from pipeline: {result} (Expected: {expected_sum})")
    
    assert result == expected_sum, "Test failed!"
    print("\nTest passed!")

if __name__ == "__main__":
    test_iterable_pipeline()
