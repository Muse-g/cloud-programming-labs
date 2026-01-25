
# task3b/S3_LAM_06.py

def map_values(d, fn):
    """
    Applies a given function `fn` to each value in the dictionary `d`,
    returning a new dictionary with the transformed values.
    Uses a dictionary comprehension.
    """
    # 1. Use a dictionary comprehension to iterate through items.
    # 2. Apply the function 'fn' to each value.
    return {k: fn(v) for k, v in d.items()}

def test_map_values():
    """
    Tests the map_values function.
    """
    print("--- Testing Mapping Dictionary Values ---")

    data = {
        "a": 1,
        "b": 2,
        "c": 3,
    }
    print(f"Original dictionary: {data}")

    # 1. Define a lambda function to double the values
    double_fn = lambda x: x * 2
    doubled_data = map_values(data, double_fn)
    expected_doubled = {"a": 2, "b": 4, "c": 6}
    print(f"Doubled values:    {doubled_data}")
    print(f"Expected doubled:  {expected_doubled}")
    assert doubled_data == expected_doubled

    # 2. Define a lambda function to convert values to strings
    to_string_fn = lambda x: str(x) + "!"
    stringified_data = map_values(data, to_string_fn)
    expected_stringified = {"a": "1!", "b": "2!", "c": "3!"}
    print(f"Stringified values: {stringified_data}")
    print(f"Expected stringified: {expected_stringified}")
    assert stringified_data == expected_stringified

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_map_values()
