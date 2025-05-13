import re

"""
2025-05-12 10:00:00 INFO: User 'Alice' logged in.
2025-05-12 10:05:30 WARNING: File not found: 'data.txt'
2025-05-12 10:12:45 ERROR: Database connection failed.

"""
line = "2025-05-12 10:05:30 WARNING: File not found: 'data.txt"

#m = re.match(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (.*))', line)
match = re.match(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+): (.*)', line)
if match:
    timestamp, level, message, log = match.groups()
print(f"Timestamp: {timestamp}, Level: {level}, Message: {message} Log:{log}" )


line2 = '127.0.0.1 - - [12/May/2025:10:30:00 +0000] "GET / HTTP/1.1" 200 1234 "-" "Mozilla/5.0"'

match = re.match(r'(\S+) \S+ \S+ \[([^\]]+)\] "(\w+) ([^"]+) HTTP/\d\.\d" (\d+) (\d+) "([^"]*)" "([^"]*)"', line2)
if match:
    ip_address, timestamp, method, resource, status, bytes_sent, referrer, user_agent = match.groups()
print(f"IP: {ip_address}, Timestamp: {timestamp}, Method: {method}, Resource: {resource}, Status: {status}")

\[([^\])\]