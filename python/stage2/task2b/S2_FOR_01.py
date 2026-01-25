
# task2b/S2_FOR_01.py

def fizzbuzz(n):
    """
    Prints numbers from 1 to N, with the following rules:
    - Multiples of 3: print "Fizz"
    - Multiples of 5: print "Buzz"
    - Multiples of both 3 and 5: print "FizzBuzz"
    - Otherwise, print the number.
    """
    print(f"--- FizzBuzz for N = {n} ---")
    # 1. Loop from 1 to N (inclusive)
    for i in range(1, n + 1):
        # 2. Check for multiples of both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # 3. Check for multiples of 3
        elif i % 3 == 0:
            print("Fizz")
        # 4. Check for multiples of 5
        elif i % 5 == 0:
            print("Buzz")
        # 5. Otherwise, print the number
        else:
            print(i)

if __name__ == "__main__":
    # The exercise asks for N=30
    fizzbuzz(30)
