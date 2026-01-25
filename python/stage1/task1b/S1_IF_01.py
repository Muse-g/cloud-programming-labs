
# task1b/S1_IF_01.py

def shipping_cost(weight_kg, is_member):
    """
    Calculates the shipping cost based on weight and membership status.

    - Returns None for invalid weight (not a number or <= 0).
    - Members get a 20% discount.
    """
    # 1. Validate weight
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        return None

    # 2. Determine base cost based on weight
    if weight_kg <= 1:
        cost = 10
    elif weight_kg <= 5:
        cost = 20
    else:
        cost = 30

    # 3. Apply membership discount
    if is_member:
        cost *= 0.8  # Apply 20% discount

    return cost

def test_shipping_cost():
    """
    Tests the shipping_cost function with various inputs, including boundary values.
    """
    test_cases = [
        # (weight, is_member), expected_cost
        (0.5, False), # Under 1kg, non-member
        (1, True),   # Exactly 1kg, member
        (3, False),  # Between 1kg and 5kg
        (5, True),   # Exactly 5kg, member
        (10, False), # Over 5kg
        (10, True),  # Over 5kg, member
        (-1, False), # Invalid weight
        ("abc", True), # Invalid weight type
        (0, False),  # Invalid weight (must be > 0)
    ]

    print("--- Testing Shipping Cost ---")
    for (weight, is_member), expected in [
        ((0.5, False), 10),
        ((1, True), 8.0),
        ((3, False), 20),
        ((5, True), 16.0),
        ((10, False), 30),
        ((10, True), 24.0),
        ((-1, False), None),
        (("abc", True), None),
        ((0, False), None),
    ]:
        result = shipping_cost(weight, is_member)
        print(f"Weight: {weight}, Member: {is_member} -> Cost: {result} (Expected: {expected})")
        assert result == expected, f"Test failed for weight {weight}, member {is_member}"
    
    print("\nAll tests passed!")

if __name__ == "__main__":
    test_shipping_cost()
