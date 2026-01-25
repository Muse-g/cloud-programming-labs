
# task3b/S3_LAM_03.py

def make_adder(x):
    """
    This is a function factory. It creates and returns a new function (a lambda)
    that adds the number 'x' to any given argument.
    
    The returned lambda is a "closure" because it "closes over" the variable 'x'
    from its enclosing scope.
    """
    # The lambda 'remembers' the value of 'x' from when it was created.
    return lambda y: x + y

def test_adder_factory():
    """
    Tests the make_adder function factory.
    """
    print("--- Testing Closure Factory (make_adder) ---")

    # 1. Create a function that adds 10
    add10 = make_adder(10)
    print("Created 'add10' function (adds 10).")
    print(f"add10(5)  -> {add10(5)} (Expected: 15)")
    print(f"add10(-2) -> {add10(-2)} (Expected: 8)")
    assert add10(5) == 15

    # 2. Create another function that adds 3
    add3 = make_adder(3)
    print("\nCreated 'add3' function (adds 3).")
    print(f"add3(5)   -> {add3(5)} (Expected: 8)")
    print(f"add3(100) -> {add3(100)} (Expected: 103)")
    assert add3(5) == 8
    
    # 3. 'add10' is independent and still works as expected
    print("\n'add10' still works correctly:")
    print(f"add10(20) -> {add10(20)} (Expected: 30)")
    assert add10(20) == 30

if __name__ == "__main__":
    test_adder_factory()
