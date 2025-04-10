import sys
from collections import defaultdict
from typing import List, Dict

# 1 Func to parse a single log into components
def parse_log_line(line: str) -> dict:
    # Split into 4 parts
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3],
    }

# 2 Func to read the file and return list of log entries
def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, 'r', encoding="UTF-8") as fh:
            for ln in fh:
                log = parse_log_line(ln)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f'File not found {file_path}.')
    except Exception as e:
        print(f'Error occured: {e}')
    return logs

# 3 Func to filter logs
def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda x: x['level'] == level.upper(), logs))

# 4  Func to count how many logs exists per level
def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)

# 5 Func to display the count of levels
def display_log_counts(counts: Dict[str, int]):
    print("Log Level       | Count")
    print("----------------|-------")
    for level in sorted(counts.keys()):
        print(f'{level:<15} | {counts[level]}')

# MAIN entry point
def main():
    if len(sys.argv) < 2:
        print("Please enter: python3 main.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        print(f'\nLog details for level "{level_filter.upper()}":')
        filtered_logs = filter_logs_by_level(logs, level_filter)
        for lg in filtered_logs:
            print(f"{lg['date']} {lg['time']} - {lg['message']}")


if __name__ == "__main__":
    main()
