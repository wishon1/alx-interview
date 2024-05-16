#!/usr/bin/python3
import sys
import re
from collections import defaultdict

# Regular expression pattern to match the log format
log_pattern = re.compile(
    r'(?P<ip>\S+) - \[(?P<date>.+?)\] '
    r'"GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)')

# Initialize metrics
total_bytes = 0
status_counts = defaultdict(int)
line_count = 0


def print_metrics(total, counts):
    """Function to print the metrics."""
    print(f"File size: {total}")
    for status_code in sorted(counts):
        print(f"{status_code}: {counts[status_code]}")


try:
    # Iterate over each line of input from standard input
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            log_data = match.groupdict()
            status_code = int(log_data['status'])
            byte_size = int(log_data['size'])

            # Update metrics
            total_bytes += byte_size
            status_counts[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            # Print metrics every 10 lines
            print_metrics(total_bytes, status_counts)

except KeyboardInterrupt:
    pass
finally:
    # Print final metrics
    print_metrics(total_bytes, status_counts)
