
# task1/S1_VAR_01.py

def catalog_types():
    """Creates a catalog of different Python types and prints their details."""
    # 1. Create variables of different types
    int_var = 10
    float_var = 3.14
    str_var = "Hello, Python!"
    bool_var = True
    none_var = None
    list_var = [1, 2, 3]
    tuple_var = (4, 5, 6)
    dict_var = {"a": 1, "b": 2}
    set_var = {7, 8, 9}
    def func_var():
        pass

    # 2. Store them in a list of tuples for easy iteration
    variables = [
        ("int_var", int_var),
        ("float_var", float_var),
        ("str_var", str_var),
        ("bool_var", bool_var),
        ("none_var", none_var),
        ("list_var", list_var),
        ("tuple_var", tuple_var),
        ("dict_var", dict_var),
        ("set_var", set_var),
        ("func_var", func_var),
    ]

    # 3. Print the table header
    print(f"{'Name':<12} | {'Value':<20} | {'type(x)':<25} | {'type(x).__name__':<15}")
    print("-" * 80)

    # 4. Print details for each variable
    for name, value in variables:
        # Truncate long values for cleaner output
        value_str = repr(value)
        if len(value_str) > 18:
            value_str = value_str[:15] + "..."
        
        type_info = str(type(value))
        type_name = type(value).__name__
        
        print(f"{name:<12} | {value_str:<20} | {type_info:<25} | {type_name:<15}")

if __name__ == "__main__":
    catalog_types()
