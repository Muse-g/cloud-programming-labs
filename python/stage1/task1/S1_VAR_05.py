
# task1/S1_VAR_05.py

def is_truthy(v):
    """Returns True if the value 'v' is truthy, False otherwise."""
    return bool(v)

def test_truthiness():
    """
    Tests the truthiness of a predefined list of values and prints the results.
    """
    # 1. Define a list of values to test
    test_values = [
        0, 
        1, 
        "", 
        "0", 
        [], 
        [0], 
        {}, 
        None
    ]

    print("--- Testing Truthiness ---")
    # 2. Iterate through the values and print their truthiness
    for value in test_values:
        # repr() gives a developer-friendly representation of the value
        print(f"The value {repr(value):<8} is {'Truthy' if is_truthy(value) else 'Falsy'}")

if __name__ == "__main__":
    test_truthiness()
