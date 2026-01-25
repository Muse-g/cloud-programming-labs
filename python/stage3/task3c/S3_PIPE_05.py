
# task3c/S3_PIPE_05.py
import re

def process_log_lines(log_lines):
    """
    Processes log lines through a pipeline:
    1. Parses lines into dictionaries (e.g., "INFO: user=42 action=login").
    2. Filters only "INFO" entries.
    3. Extracts user IDs as integers, dropping invalid ones.
    Returns a list of user IDs.
    """

    def parse_log_line(line):
        """Parses a single log line into a dictionary."""
        parts = line.split(': ', 1)
        if len(parts) < 2:
            return None # Malformed line
        log_type = parts[0]
        message_parts = parts[1].split(' ')
        
        parsed_data = {"type": log_type.strip()}
        for part in message_parts:
            if '=' in part:
                key, value = part.split('=', 1)
                parsed_data[key.strip()] = value.strip()
        return parsed_data

    def filter_info_logs(parsed_logs):
        """Filters for log entries of type 'INFO'."""
        for log_entry in parsed_logs:
            if log_entry and log_entry.get("type") == "INFO":
                yield log_entry

    def extract_user_ids(info_logs):
        """Extracts user IDs as integers, skipping invalid ones."""
        for log_entry in info_logs:
            user_id_str = log_entry.get("user")
            if user_id_str:
                try:
                    yield int(user_id_str)
                except ValueError:
                    pass # Skip if user ID is not a valid integer

    # Build the pipeline
    parsed = map(parse_log_line, log_lines)
    filtered = filter_info_logs(parsed)
    user_ids = extract_user_ids(filtered)

    return list(user_ids) # Materialize the generator into a list

def test_log_pipeline():
    """
    Tests the process_log_lines function.
    """
    print("--- Testing Log Line Processing Pipeline ---")

    log_data = [
        "INFO: user=42 action=login duration=100ms",
        "ERROR: code=500 message='Server error'",
        "INFO: user=101 action=logout",
        "WARNING: low disk space",
        "INFO: user=invalid action=failed", # Invalid user ID
        "INFO: action=anonymous", # No user ID
        "MALFORMED_LINE",
        "INFO: user=123 action=click",
    ]
    
    # Expected user IDs: 42, 101, 123
    expected_ids = [42, 101, 123]

    result_ids = process_log_lines(log_data)
    
    print("Log lines processed:")
    for line in log_data:
        print(f"  {line}")
    print(f"\nExtracted User IDs: {result_ids}")
    print(f"Expected IDs:       {expected_ids}")
    
    assert result_ids == expected_ids, "Test failed!"
    print("\nTest passed!")

if __name__ == "__main__":
    test_log_pipeline()
