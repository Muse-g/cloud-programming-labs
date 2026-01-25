
# task3b/S3_LAM_01.py

def test_lambdas():
    """
    Defines and tests several lambda functions.
    """
    print("--- Testing Basic Lambda Functions ---")

    # 1. Lambda for squaring a number
    square = lambda n: n * n
    print("\nTesting 'square' lambda:")
    print(f"square(5)  -> {square(5)} (Expected: 25)")
    print(f"square(-2) -> {square(-2)} (Expected: 4)")
    print(f"square(0)  -> {square(0)} (Expected: 0)")
    assert square(5) == 25

    # 2. Lambda for checking if a number is odd
    is_odd = lambda n: n % 2 != 0
    print("\nTesting 'is_odd' lambda:")
    print(f"is_odd(5) -> {is_odd(5)} (Expected: True)")
    print(f"is_odd(4) -> {is_odd(4)} (Expected: False)")
    print(f"is_odd(0) -> {is_odd(0)} (Expected: False)")
    assert is_odd(5) is True

    # 3. Lambda for greeting someone
    greet = lambda name: f"Hello, {name}!"
    print("\nTesting 'greet' lambda:")
    print(f"greet('Alice') -> \"{greet('Alice')}\"")
    print(f"greet('World') -> \"{greet('World')}\"")
    print(f"greet('')      -> \"{greet('')}\"")
    assert greet("Alice") == "Hello, Alice!"

if __name__ == "__main__":
    test_lambdas()
