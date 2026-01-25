
# task1c/S1_MC_01.py
import sys

def day_name(n: int) -> str | None:
    """
    Returns the name of the day for a given number (1-7) using match/case.
    Returns None for any other input.
    """
    # This check ensures we're using a compatible Python version.
    if sys.version_info < (3, 10):
        # Fallback for older Python versions
        if n == 1: return "Monday"
        if n == 2: return "Tuesday"
        if n == 3: return "Wednesday"
        if n == 4: return "Thursday"
        if n == 5: return "Friday"
        if n == 6: return "Saturday"
        if n == 7: return "Sunday"
        return None

    # 1. Use match/case for direct mapping
    match n:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:  # The wildcard case handles all other inputs
            return None

def test_day_name():
    """
    Tests the day_name function.
    """
    print("--- Testing Day Name Mapping ---")
    if sys.version_info < (3, 10):
        print("NOTE: Using if/elif/else fallback for Python < 3.10")

    test_cases = [1, 3, 7, 0, 8, "abc"]
    expected_results = ["Monday", "Wednesday", "Sunday", None, None, None]

    for case, expected in zip(test_cases, expected_results):
        result = day_name(case)
        print(f"Input: {case} -> Day: {result} (Expected: {expected})")
        assert result == expected, f"Failed for input {case}"

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_day_name()
