
# task1b/S1_IF_03.py

def normalize_name(x):
    """
    Normalizes a user name.
    - If the input is falsy, returns "Anonymous".
    - Strips whitespace from the name.
    - If the stripped name is empty, returns "Anonymous".
    """
    # 1. Check if the input is falsy (e.g., None, empty string)
    if not x:
        return "Anonymous"
    
    # 2. Ensure it's a string before stripping, just in case
    if not isinstance(x, str):
        # Decide how to handle non-string, non-falsy inputs.
        # Here we'll convert to string, but you could also return "Anonymous".
        x = str(x)

    # 3. Strip whitespace
    stripped_name = x.strip()

    # 4. Check if the stripped name is empty
    if not stripped_name:
        return "Anonymous"
    
    return stripped_name

def test_name_normalization():
    """
    Tests the normalize_name function with various inputs.
    """
    test_cases = [
        "",         # Falsy, should be Anonymous
        " ",        # Strips to empty, should be Anonymous
        None,       # Falsy, should be Anonymous
        "  Ola  ",  # Should be stripped
        "John Doe", # Should remain the same
    ]
    
    expected_results = [
        "Anonymous",
        "Anonymous",
        "Anonymous",
        "Ola",
        "John Doe",
    ]

    print("--- Testing Name Normalization ---")
    for case, expected in zip(test_cases, expected_results):
        result = normalize_name(case)
        print(f"Input: {repr(case):<8} -> Normalized: '{result}' (Expected: '{expected}')")
        assert result == expected, f"Failed for input {repr(case)}"

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_name_normalization()
