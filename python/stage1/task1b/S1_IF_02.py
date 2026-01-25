
# task1b/S1_IF_02.py

def grade(score):
    """
    Converts a numerical score (0-100) to a letter grade.
    Returns None if the score is outside the valid range.
    """
    # 1. Validate score is within the 0-100 range
    if not isinstance(score, (int, float)) or not (0 <= score <= 100):
        return None

    # 2. Determine the grade using if/elif/else
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def test_grader():
    """
    Tests the grade function with boundary values.
    """
    test_scores = [
        101, 100, 90, 89, 80, 79, 70, 69, 60, 59, 0, -1
    ]
    
    expected_grades = [
        None, "A", "A", "B", "B", "C", "C", "D", "D", "F", "F", None
    ]

    print("--- Testing Score to Grade Conversion ---")
    for score, expected in zip(test_scores, expected_grades):
        result = grade(score)
        print(f"Score: {score:<4} -> Grade: {result} (Expected: {expected})")
        assert result == expected, f"Failed for score {score}"

    print("\nAll boundary tests passed!")

if __name__ == "__main__":
    test_grader()
