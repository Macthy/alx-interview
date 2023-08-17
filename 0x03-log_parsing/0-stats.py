#!/usr/bin/python3
import sys

# Initialize variables to store statistics
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Read log entries from stdin
for line in sys.stdin:
    # Split the log entry into parts
    parts = line.split()

    # Check if the log entry format is valid
    if len(parts) >= 9:
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update statistics
        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

    # Check if 10 lines have been processed
    if len(status_counts.values()) >= 10:
        print("File size: {:d}".format(total_size))
        for code, count in sorted(status_counts.items()):
            if count > 0:
                print("{:d}: {:d}".format(code, count))

# Print the final statistics
print("File size: {:d}".format(total_size))
for code, count in sorted(status_counts.items()):
    if count > 0:
        print("{:d}: {:d}".format(code, count))

