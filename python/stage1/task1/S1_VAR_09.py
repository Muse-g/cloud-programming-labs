
# task1/S1_VAR_09.py

def add(a: int, b: int) -> int:
    """
    This function is type-hinted to accept two integers and return an integer.
    However, these hints are not enforced at runtime by default Python.
    """
    return a + b

def demonstrate_type_hints():
    """
    Shows that type hints are not enforced at runtime by calling a function
    with arguments of an unexpected type.
    """
    print("--- Type Hints Demonstration ---")
    
    # 1. Call the function with the correct types (as intended)
    correct_result = add(5, 10)
    print(f"Calling add(5, 10):")
    print(f"  Result: {correct_result}, Type of Result: {type(correct_result).__name__}")

    # 2. Call the function with incorrect types (strings)
    print("\nCalling add('hello', ' world'):")
    try:
        incorrect_result = add("hello", " world")
        print(f"  Result: '{incorrect_result}', Type of Result: {type(incorrect_result).__name__}")
        print("  The operation succeeded because the '+' operator is defined for strings (concatenation).")
    except TypeError as e:
        print(f"  An error occurred: {e}")

    # This would cause a TypeError because you can't add an int and a string
    print("\nCalling add(5, ' world'):")
    try:
        add(5, " world")
    except TypeError as e:
        print(f"  An error occurred as expected: {e}")

    # 3. Add the required comment
    print("\n# Comment on Type Hints:")
    print("# Type hints in Python are primarily for static analysis tools (like mypy) and")
    print("# for improving code readability and maintainability. They do not provide")
    print("# automatic runtime type checking. The Python interpreter ignores them at runtime.")

if __name__ == "__main__":
    demonstrate_type_hints()
