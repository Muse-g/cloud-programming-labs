
# task1/S1_VAR_03.py

def list_vs_tuple_mutability():
    """
    Demonstrates the difference in mutability between lists and tuples.
    """
    # 1. Create a list and modify it
    print("--- List (Mutable) ---")
    lst = [1, 2, 3]
    print(f"Original list: {lst}")
    
    try:
        lst[1] = 99  # Modify an element
        print(f"Modified list: {lst}")
        print("Modification successful.")
    except TypeError as e:
        print(f"Modification failed: {e}")

    print("\n--- Tuple (Immutable) ---")
    # 2. Create a tuple and attempt to modify it
    tup = (1, 2, 3)
    print(f"Original tuple: {tup}")

    try:
        tup[1] = 99  # Attempt to modify an element
        print(f"Modified tuple: {tup}")
    except TypeError as e:
        print(f"Modification failed as expected: {e}")
        
    # 3. Explain the difference
    print("\n# Explanation:")
    print("# Lists are mutable, meaning their contents can be changed after creation.")
    print("# Tuples are immutable; their contents cannot be altered once defined.")

if __name__ == "__main__":
    list_vs_tuple_mutability()
