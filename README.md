# System Health Monitor

A Python-based system monitoring tool that tracks CPU, memory, and disk usage in real time and logs alerts to a file.

## Features
- Monitors CPU, memory, and disk usage
- Logs stats with timestamps to a log file
- Triggers alerts when usage crosses thresholds

## Tech Used
- Python
- psutil library

## How to Run
pip install psutil
python monitor.py

## Sample Output
2026-06-09 00:20:16 | CPU: 3.5% | Memory: 85.7% | Disk: 94.3%
ALERT: High Memory usage!
ALERT: Low Disk Space!
