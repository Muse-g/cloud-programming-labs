
# task1/S1_VAR_08.py

def big_integer_demonstration():
    """
    Demonstrates Python's handling of arbitrarily large integers and contrasts
    it with the fixed precision of floating-point numbers.
    """
    print("--- Python's Arbitrary-Precision Integers ---")
    
    # 1. Compute a very large integer
    large_int = 10**100
    print(f"Value of 10**100 (Googol): {large_int}")
    print(f"Type of large_int: {type(large_int).__name__}")
    
    # To find the number of digits, we can convert it to a string
    num_digits = len(str(large_int))
    print(f"Number of digits in large_int: {num_digits}")

    print("\n--- Contrast with Floating-Point Precision ---")
    # 2. Convert the large integer to a float
    large_float = float(large_int)
    print(f"Large integer as a float: {large_float}")
    
    # 3. Add a comment on precision
    print("\n# Comment on Precision:")
    print("# Python's 'int' type supports arbitrary precision, meaning it can store")
    print("# integers of any size, limited only by available memory.")
    print("# In contrast, 'float' uses fixed-precision (usually 64-bit IEEE 754),")
    print("# which can lead to a loss of precision for very large numbers or")
    print("# for fractions that cannot be perfectly represented in binary.")

if __name__ == "__main__":
    big_integer_demonstration()
