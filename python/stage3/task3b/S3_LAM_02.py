
# task3b/S3_LAM_02.py

def sort_people_by_age():
    """
    Sorts a list of people (dictionaries) by their age using a lambda function.
    """
    people = [
        {"name": "Charlie", "age": 35},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 45},
        {"name": "David", "age": 25},
    ]

    print("--- Sorting Dictionaries with a Lambda Key ---")
    print("Original list of people:")
    for person in people:
        print(f"  {person}")

    # 1. Use the sorted() function with a lambda for the 'key' argument.
    # The lambda tells sorted() to look at the 'age' value of each dictionary.
    sorted_people = sorted(people, key=lambda p: p["age"])

    print("\nList sorted by age (ascending):")
    for person in sorted_people:
        print(f"  {person}")
        
    # Example for assertion
    expected_ages = [25, 25, 35, 45]
    result_ages = [p['age'] for p in sorted_people]
    assert result_ages == expected_ages
    print("\nAssertion passed: Ages are correctly sorted.")

if __name__ == "__main__":
    sort_people_by_age()
