# Paste your python file here don't for get to upload it with your submission
#Part 2 a-c allows you to select what log file to read, on this case one was  made it all 5 of them, and extracts the time info with the count too 
#ofcourse you can secify the log component by seelcting what file 
import os
import re
import json

def read_log_file(filename):
    lines = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    return lines

def parse_log_line(line):
    pattern = r'^(.*?\d{2,3}) \| (.*?) \| (.*?) \| (.*)$'
    match = re.match(pattern, line)
    if match:
        timestamp = match.group(1)
        log_name = match.group(2)
        log_level = match.group(3)
        message = match.group(4)
        return timestamp, log_name, log_level, message
    else:
        return None

def count_log_levels(lines):
    log_counts = {}

    for line in lines:
        parsed = parse_log_line(line.strip())
        if parsed:
            _, _, log_level, message = parsed

            if log_level not in log_counts:
                log_counts[log_level] = {}

            if message not in log_counts[log_level]:
                log_counts[log_level][message] = 1
            else:
                log_counts[log_level][message] += 1
    return log_counts

def save_as_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"✅ Results saved to {filename}")

if __name__ == "__main__":
    # Read and combine all five log files
    all_lines = []
    log_files = ['frontend.log', 'backend.log', 'sqldb.log', 'authserver.log', 'system.log']

    for file in log_files:
        lines = read_log_file(file)
        all_lines.extend(lines)

    # Count across all logs
    log_counts = count_log_levels(all_lines)

    # Save combined results to a JSON file
    save_as_json(log_counts, 'Part2_combined_log_summary.json')
