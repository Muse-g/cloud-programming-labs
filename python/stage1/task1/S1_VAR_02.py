
# task1/S1_VAR_02.py

def demonstrate_dynamic_typing():
    """
    Demonstrates dynamic typing by re-assigning a variable to different types.
    """
    # 1. Initialize a variable 'x'
    x = 100
    print(f"Value: {x}, Type: {type(x).__name__}")

    # 2. Re-assign 'x' to a string
    x = "Now I'm a string"
    print(f"Value: {x}, Type: {type(x).__name__}")

    # 3. Re-assign 'x' to a list
    x = [1, 2, 3]
    print(f"Value: {x}, Type: {type(x).__name__}")

    # 4. Re-assign 'x' to a boolean
    x = False
    print(f"Value: {x}, Type: {type(x).__name__}")

    # 5. Add a comment explaining dynamic typing
    print("\n# Dynamic Typing Explanation:")
    print("# In Python, variables are just labels for memory locations.")
    print("# The type is associated with the object in memory, not the variable name.")
    print("# This allows the variable 'x' to be reassigned to objects of different types.")

if __name__ == "__main__":
    demonstrate_dynamic_typing()
