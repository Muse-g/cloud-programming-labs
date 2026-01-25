
# task1/S1_VAR_10.py
import collections.abc

def inspect_value(v):
    """
    Inspects a given value and returns a dictionary of its properties.
    """
    # Check if the object is iterable
    is_iterable = isinstance(v, collections.abc.Iterable)
    
    # Check if the object is callable
    is_callable = callable(v)

    return {
        "value": repr(v),
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": is_callable,
        "is_iterable": is_iterable,
        "truthy": bool(v),
    }

def test_inspector():
    """
    Tests the inspect_value function with a variety of different values
    and pretty-prints the results.
    """
    test_values = [
        10,
        0.0,
        "Python",
        "",
        True,
        None,
        [1, 2],
        (),
        {},
        set(),
        lambda x: x,
        test_inspector, # A function is callable
    ]

    print("--- Mini Inspector Results ---")
    for i, value in enumerate(test_values):
        inspection_result = inspect_value(value)
        print(f"\n--- Test Case #{i+1} ---")
        for key, result in inspection_result.items():
            print(f"  {key:<12}: {result}")

if __name__ == "__main__":
    test_inspector()
