
# task2b/S2_FOR_06.py

def sum_nested(matrix):
    """
    Sums all numbers in a nested list (matrix).
    Validates that the input is a list and each row is a list.
    Returns None if validation fails.
    """
    # 1. Validate that the outer structure is a list
    if not isinstance(matrix, list):
        return None

    total_sum = 0
    # 2. Outer loop to iterate through each row
    for row in matrix:
        # 3. Validate that each row is a list
        if not isinstance(row, list):
            return None
        # 4. Inner loop to sum the numbers in the row
        for number in row:
            # You might add a check here if you expect non-number data
            if isinstance(number, (int, float)):
                total_sum += number
    
    return total_sum

def test_sum_nested():
    """
    Tests the sum_nested function.
    """
    print("--- Testing Sum of Nested Lists (Matrix) ---")
    
    # Test case 1: Regular matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected1 = 45
    result1 = sum_nested(matrix1)
    print(f"Input: {matrix1} -> Sum: {result1} (Expected: {expected1})")
    assert result1 == expected1

    # Test case 2: Jagged matrix (rows with different lengths)
    matrix2 = [
        [1],
        [2, 3],
        [4, 5, 6]
    ]
    expected2 = 21
    result2 = sum_nested(matrix2)
    print(f"Input: {matrix2} -> Sum: {result2} (Expected: {expected2})")
    assert result2 == expected2

    # Test case 3: Invalid row type
    matrix3 = [
        [1, 2],
        "not a list",
        [3, 4]
    ]
    expected3 = None
    result3 = sum_nested(matrix3)
    print(f"Input: {matrix3} -> Sum: {result3} (Expected: {expected3})")
    assert result3 == expected3

    # Test case 4: Not a list input
    matrix4 = "not a matrix"
    expected4 = None
    result4 = sum_nested(matrix4)
    print(f"Input: '{matrix4}' -> Sum: {result4} (Expected: {expected4})")
    assert result4 == expected4

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_sum_nested()
