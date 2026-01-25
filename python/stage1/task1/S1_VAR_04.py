
# task1/S1_VAR_04.py

def identity_vs_equality():
    """
    Demonstrates the difference between 'is' (identity) and '==' (equality).
    """
    print("--- Comparing Lists ---")
    # 1. Create two lists with the same content
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a  # 'c' is a reference to the same object as 'a'

    print(f"a = {a}, b = {b}, c = {a}")
    print(f"a == b: {a == b}  # Equal content")
    print(f"a is b: {a is b}  # Different objects in memory")
    print(f"a == c: {a == c}  # Equal content")
    print(f"a is c: {a is c}  # Same object in memory")

    print("\n--- Comparing with None ---")
    # 2. Correctly check for None using 'is'
    my_variable = None
    
    # The recommended way
    print(f"my_variable is None: {my_variable is None}")
    
    # While '==' might work, 'is' is the convention for checking for the singleton None
    print(f"my_variable == None: {my_variable == None}")

    # 3. Add the required comment
    print("\n# Guideline:")
    print("# Use 'is' for identity checks (checking if two variables point to the same object).")
    print("# Use '==' for equality checks (checking if the values of two objects are the same).")
    print("# Always use 'is' or 'is not' to check for None, as None is a singleton object.")

if __name__ == "__main__":
    identity_vs_equality()
