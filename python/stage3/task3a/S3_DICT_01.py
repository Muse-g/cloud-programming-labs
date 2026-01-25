
# task3a/S3_DICT_01.py

def get_path(obj, path, fallback=None):
    """
    Safely retrieves a value from a nested dictionary using a dotted path.
    
    Example: get_path(data, "a.b.c") is like data['a']['b']['c']
    
    If any key is missing or a value along the path is not a dictionary,
    it returns the fallback value.
    """
    # 1. Split the path string into a list of keys
    keys = path.split('.')
    
    current_level = obj
    # 2. Loop through each key in the path
    for key in keys:
        # 3. Check if the current level is a dictionary and contains the key
        if isinstance(current_level, dict) and key in current_level:
            current_level = current_level[key]
        else:
            # 4. If not, the path is broken, so return the fallback
            return fallback
            
    # 5. If the loop completes, we've found the value
    return current_level

def test_get_path():
    """
    Tests the get_path function.
    """
    print("--- Testing Safe Get by Dotted Path ---")
    
    data = {
        "a": {
            "b": {
                "c": 100
            },
            "d": 200
        }
    }

    # Test case 1: Successful path
    path1 = "a.b.c"
    expected1 = 100
    result1 = get_path(data, path1)
    print(f"Path: '{path1}' -> Value: {result1} (Expected: {expected1})")
    assert result1 == expected1

    # Test case 2: Path with a missing key
    path2 = "a.x.c"
    expected2 = None # Default fallback
    result2 = get_path(data, path2)
    print(f"Path: '{path2}' -> Value: {result2} (Expected: {expected2})")
    assert result2 == expected2

    # Test case 3: Path where an intermediate value is not a dict
    path3 = "a.d.c" # 'd' is an integer, not a dict
    expected3 = "Not Found" # Custom fallback
    result3 = get_path(data, path3, fallback="Not Found")
    print(f"Path: '{path3}' -> Value: '{result3}' (Expected: '{expected3}')")
    assert result3 == expected3

    # Test case 4: Simple, non-nested path
    path4 = "a.d"
    expected4 = 200
    result4 = get_path(data, path4)
    print(f"Path: '{path4}' -> Value: {result4} (Expected: {expected4})")
    assert result4 == expected4

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_get_path()
