
# task2b/S2_FOR_03.py

def sum_until(nums, threshold):
    """
    Sums numbers from a list in order until adding the next number
    would exceed the given threshold.
    Returns the final sum.
    """
    current_sum = 0
    # 1. Loop through the numbers
    for num in nums:
        # 2. Check if adding the next number would exceed the threshold
        if current_sum + num > threshold:
            # 3. If so, break the loop
            break
        # 4. Otherwise, add the number to the sum
        current_sum += num
    
    return current_sum

def test_sum_until():
    """
    Tests the sum_until function.
    """
    print("--- Testing Sum Until Threshold ---")

    # Test case 1
    nums1 = [1, 5, 2, 8, 4]
    threshold1 = 10
    expected1 = 8 # 1 + 5 + 2 = 8. Adding 8 would be 16, which is > 10.
    result1 = sum_until(nums1, threshold1)
    print(f"Input: {nums1}, Threshold: {threshold1} -> Sum: {result1} (Expected: {expected1})")
    assert result1 == expected1

    # Test case 2: Threshold is never reached
    nums2 = [10, 20, 30]
    threshold2 = 100
    expected2 = 60 # 10 + 20 + 30 = 60
    result2 = sum_until(nums2, threshold2)
    print(f"Input: {nums2}, Threshold: {threshold2} -> Sum: {result2} (Expected: {expected2})")
    assert result2 == expected2

    # Test case 3: First number already exceeds threshold
    nums3 = [20, 1, 1]
    threshold3 = 15
    expected3 = 0
    result3 = sum_until(nums3, threshold3)
    print(f"Input: {nums3}, Threshold: {threshold3} -> Sum: {result3} (Expected: {expected3})")
    assert result3 == expected3

    # Test case 4: Empty list
    nums4 = []
    threshold4 = 50
    expected4 = 0
    result4 = sum_until(nums4, threshold4)
    print(f"Input: {nums4}, Threshold: {threshold4} -> Sum: {result4} (Expected: {expected4})")
    assert result4 == expected4

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_sum_until()
