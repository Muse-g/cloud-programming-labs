
# task3a/S3_DICT_02.py

def merge_defaults(defaults, overrides):
    """
    Merges two dictionaries, creating a new dictionary.
    Keys in 'overrides' take precedence over 'defaults'.
    This is a shallow merge.
    """
    # 1. Use the dictionary unpacking syntax for a clean, readable merge.
    # The order is important: keys from the right-most dict win.
    return {**defaults, **overrides}

    # For Python 3.9+, you can also use the union operator:
    # return defaults | overrides

def test_merge_defaults():
    """
    Tests the merge_defaults function and illustrates its shallow nature.
    """
    print("--- Testing Dictionary Merging (Shallow) ---")

    defaults = {
        "font": "Arial",
        "size": 12,
        "color": "black",
        "style": {"bold": False, "italic": False}
    }
    
    overrides = {
        "size": 14,
        "style": {"italic": True} # This will completely replace the default 'style' dict
    }

    expected_merge = {
        "font": "Arial",
        "size": 14,
        "color": "black",
        "style": {"italic": True} # Note that "bold" is gone
    }

    merged = merge_defaults(defaults, overrides)
    
    print(f"Defaults:  {defaults}")
    print(f"Overrides: {overrides}")
    print(f"Merged:    {merged}")
    print(f"Expected:  {expected_merge}")
    
    assert merged == expected_merge

    print("\n--- Illustrating Shallow Merge ---")
    defaults_deep = {"a": 1, "b": {"x": 10, "y": 20}}
    overrides_deep = {"b": {"y": 99}} # We only want to change 'y'
    
    merged_deep = merge_defaults(defaults_deep, overrides_deep)
    
    print(f"Defaults:  {defaults_deep}")
    print(f"Overrides: {overrides_deep}")
    print(f"Shallow Merged: {merged_deep}")
    print("# Notice that the entire 'b' dictionary was replaced, not merged recursively.")
    print("# The 'x' key from the default 'b' dict is lost.")


if __name__ == "__main__":
    test_merge_defaults()
