
# task1c/S1_MC_03.py
import sys

def calc(a, op: str, b):
    """
    A simple calculator that uses match/case to perform an operation.
    Validates inputs and handles division by zero.
    """
    # 1. Validate that 'a' and 'b' are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None

    # This check ensures we're using a compatible Python version.
    if sys.version_info < (3, 10):
        # Fallback for older Python versions
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0: return None
            return a / b
        return None

    # 2. Use match/case for the operation
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            # 3. Handle division by zero
            if b == 0:
                return None
            return a / b
        case _:
            # Return None for any unknown operator
            return None

def test_calculator():
    """
    Tests the calc function with various inputs.
    """
    print("--- Testing Simple Calculator ---")
    if sys.version_info < (3, 10):
        print("NOTE: Using if/elif/else fallback for Python < 3.10")

    test_cases = [
        (10, "+", 5),
        (10, "-", 5),
        (10, "*", 5),
        (10, "/", 5),
        (10, "/", 0),    # Division by zero
        (10, "%", 5),    # Invalid operator
        ("a", "+", 5),   # Invalid number
    ]
    
    expected_results = [15, 5, 50, 2.0, None, None, None]

    for (a, op, b), expected in zip(test_cases, expected_results):
        result = calc(a, op, b)
        print(f"Input: {a} {op} {b} -> Result: {result} (Expected: {expected})")
        assert result == expected, f"Failed for {a} {op} {b}"

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_calculator()
