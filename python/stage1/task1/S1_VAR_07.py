
# task1/S1_VAR_07.py
import math

def explore_nan():
    """
    Creates and demonstrates properties of NaN (Not a Number).
    """
    print("--- Exploring NaN ---")
    
    # 1. Create NaN in two ways
    nan1 = float("nan")
    
    nan2 = float("nan") # Fallback
    try:
        # This operation would raise a ZeroDivisionError
        # In some contexts (like NumPy), it might produce NaN directly
        # For standard Python, we catch the error and use the fallback
        nan_from_div = 0.0 / 0.0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError when trying 0.0 / 0.0. Using float('nan') as fallback.")
        nan_from_div = float("nan")

    print(f"nan1: {nan1}")
    print(f"nan_from_div: {nan_from_div}")

    # 2. Demonstrate NaN's unique comparison properties
    print("\n--- NaN Comparisons ---")
    # A key property of NaN is that it never equals anything, including itself.
    print(f"nan1 == nan1: {nan1 == nan1}")
    print(f"nan1 == nan_from_div: {nan1 == nan_from_div}")
    print(f"nan1 is nan1: {nan1 is nan1} (Identity can be true)")

    # 3. Use math.isnan() to correctly detect NaN
    print("\n--- Detecting NaN with math.isnan() ---")
    print(f"math.isnan(nan1): {math.isnan(nan1)}")
    print(f"math.isnan(nan_from_div): {math.isnan(nan_from_div)}")
    print(f"math.isnan(1.0): {math.isnan(1.0)}")

if __name__ == "__main__":
    explore_nan()
