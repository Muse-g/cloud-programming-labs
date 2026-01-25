
# task2b/S2_FOR_05.py

def multiplication_table(n=10):
    """
    Prints a multiplication table of size n x n using nested loops.
    Includes optional column alignment for readability.
    """
    print(f"--- {n}x{n} Multiplication Table ---")

    # 1. Outer loop for the rows (multiplicand)
    for i in range(1, n + 1):
        row_values = []
        # 2. Inner loop for the columns (multiplier)
        for j in range(1, n + 1):
            product = i * j
            # Use f-string formatting to align the numbers
            # We calculate the max width needed for alignment
            max_width = len(str(n*n))
            row_values.append(f"{product:>{max_width}}")
        
        # 3. Print the formatted row
        print(" | ".join(row_values))

if __name__ == "__main__":
    multiplication_table(10)
