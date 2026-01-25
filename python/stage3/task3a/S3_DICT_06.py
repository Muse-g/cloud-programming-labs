
# task3a/S3_DICT_06.py

def group_by(items, key):
    """
    Groups a list of dictionaries by the value of a specified key.
    
    Returns a dictionary where each key is a value of the grouping property,
    and each value is a list of the original dictionaries that have that property value.
    """
    grouped_dict = {}
    # 1. Iterate through each dictionary (item) in the list
    for item in items:
        # 2. Get the value of the key we want to group by. Use .get() for safety.
        grouping_value = item.get(key)
        
        # 3. If this value is already a key in our grouped dictionary, append the item
        if grouping_value in grouped_dict:
            grouped_dict[grouping_value].append(item)
        # 4. Otherwise, create a new list for this key with the current item
        else:
            grouped_dict[grouping_value] = [item]
            
    return grouped_dict

def test_group_by():
    """
    Tests the group_by function.
    """
    print("--- Testing Group By Property ---")

    users = [
        {"name": "Alice", "role": "admin", "id": 1},
        {"name": "Bob", "role": "user", "id": 2},
        {"name": "Charlie", "role": "admin", "id": 3},
        {"name": "David", "role": "guest", "id": 4},
        {"name": "Eve", "role": "user", "id": 5},
    ]

    # Group by the "role" property
    grouped_by_role = group_by(users, "role")

    print("Original list:")
    for user in users:
        print(f"  {user}")
        
    print("\nGrouped by 'role':")
    for role, user_list in grouped_by_role.items():
        print(f"  '{role}':")
        for user in user_list:
            print(f"    {user}")

    # Basic assertion to check if keys are correct
    assert sorted(grouped_by_role.keys()) == ["admin", "guest", "user"]
    # Check if counts are correct
    assert len(grouped_by_role["admin"]) == 2
    assert len(grouped_by_role["user"]) == 2
    assert len(grouped_by_role["guest"]) == 1
    
    print("\nTest passed!")

if __name__ == "__main__":
    test_group_by()
