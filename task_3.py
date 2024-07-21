import sys
from collections import defaultdict


def parse_log_line(line):
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {'date': date, 'time': time, 'level': level, 'message': message}


def load_logs(file_path):
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу {file_path}: {e}")
    return logs


def filter_logs_by_level(logs, level):
    return [log for log in logs if log['level'].lower() == level.lower()]


def count_logs_by_level(logs):
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts


def display_log_counts(counts):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<8}")


def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до файлу логів.")
        return

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
