
# task1c/S1_MC_02.py
import sys

def run_command(cmd: str) -> str:
    """
    Routes a command string to a specific action using match/case.
    """
    if sys.version_info < (3, 10):
        # Fallback for older Python versions
        if cmd == "start": return "Command 'start' executed."
        if cmd == "stop": return "Command 'stop' executed."
        if cmd == "status": return "Command 'status' executed."
        return "UNKNOWN_COMMAND"

    # 1. Use match/case to route the command
    match cmd:
        case "start":
            # In a real app, you would call a function here
            return "Command 'start' executed."
        case "stop":
            return "Command 'stop' executed."
        case "status":
            return "Command 'status' executed."
        case _:
            return "UNKNOWN_COMMAND"

def test_command_router():
    """
    Tests the run_command function.
    """
    print("--- Testing Command Router ---")
    if sys.version_info < (3, 10):
        print("NOTE: Using if/elif/else fallback for Python < 3.10")

    test_cases = ["start", "status", "end", None, "STOP"]
    expected_results = [
        "Command 'start' executed.",
        "Command 'status' executed.",
        "UNKNOWN_COMMAND",
        "UNKNOWN_COMMAND",
        "UNKNOWN_COMMAND" # Match is case-sensitive
    ]

    for case, expected in zip(test_cases, expected_results):
        result = run_command(case)
        print(f"Input: {repr(case)} -> Result: '{result}'")
        assert result == expected, f"Failed for command {case}"

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_command_router()
