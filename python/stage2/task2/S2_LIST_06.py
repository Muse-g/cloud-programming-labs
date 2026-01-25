
# task2/S2_LIST_06.py

def transform_users(users):
    """
    Given a list of user records, returns the names of active users,
    uppercased and sorted alphabetically.
    """
    # 1. Use a list comprehension to filter and transform
    # - Filter for active users (user["active"] is True)
    # - Extract the name and convert to uppercase
    active_user_names = [
        user["name"].upper() for user in users if user.get("active")
    ]

    # 2. Sort the resulting list
    return sorted(active_user_names)

def test_transform_users():
    """
    Tests the transform_users function.
    """
    users = [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "bob", "active": False},
        {"id": 3, "name": "Charlie", "active": True},
        {"id": 4, "name": "david", "active": True},
        {"id": 5, "name": "Eve", "active": False},
        {"id": 6, "name": "Frank", "active": True},
    ]

    expected = ["ALICE", "CHARLIE", "DAVID", "FRANK"]
    
    print("--- Testing User Record Transformation ---")
    result = transform_users(users)
    print(f"Input users: {users}")
    print(f"Transformed names: {result}")
    print(f"Expected:          {expected}")

    assert result == expected, "Test failed!"
    print("\nTest passed!")

if __name__ == "__main__":
    test_transform_users()
