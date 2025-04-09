import sys
from collections import defaultdict
from typing import List, Dict

# Function to parse a single log line into components
def parse_log_line(line: str) -> dict:
    # Split into 4 parts: date, time, level, message
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return {}  # skip malformed lines
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3]
    }

# Function to read the log file and return a list of parsed log entries
def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    return logs

# Function to filter logs by a specific level
def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda x: x['level'] == level.upper(), logs))

# Function to count how many logs exist per level
def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)

# Function to display the count of log levels in a table format
def display_log_counts(counts: Dict[str, int]):
    print("Log Level       | Count")
    print("----------------|-------")
    for level in sorted(counts.keys()):
        print(f"{level:<15} | {counts[level]}")

# Main script entry point
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        print(f"\nLog details for level '{level_filter.upper()}':")
        filtered_logs = filter_logs_by_level(logs, level_filter)
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
