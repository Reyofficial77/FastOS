#!/bin/bash
# FastOS Performance Benchmark Script
# This script measures the system's resource usage and boot performance.

REPORT_FILE="benchmark_report.txt"
echo "FastOS Performance Report - $(date)" > $REPORT_FILE
echo "========================================" >> $REPORT_FILE

echo "Running benchmarks... please wait."

# 1. Boot Time
echo "[1/6] Measuring boot time..."
BOOT_TIME=$(systemd-analyze)
echo "Boot Time: $BOOT_TIME" >> $REPORT_FILE

# 2. Idle RAM Usage
echo "[2/6] Measuring RAM usage..."
# Get used memory in MB
RAM_USED=$(free -m | awk '/^Mem:/{print $3}')
RAM_TOTAL=$(free -m | awk '/^Mem:/{print $2}')
echo "RAM Usage: ${RAM_USED}MB / ${RAM_TOTAL}MB" >> $REPORT_FILE

# 3. Idle CPU Usage (average over 60 seconds)
echo "[3/6] Measuring idle CPU usage (60s)..."
CPU_IDLE=$(vmstat 1 60 | tail -n 1 | awk '{print $15}')
CPU_USAGE=$((100 - CPU_IDLE))
echo "Idle CPU Usage: ${CPU_USAGE}%" >> $REPORT_FILE

# 4. Disk Usage
echo "[4/6] Measuring disk usage..."
DISK_USAGE=$(df -h / | awk 'NR==2 {print $3 "/" $2 " (" $5 ")"}')
echo "Disk Usage: $DISK_USAGE" >> $REPORT_FILE

# 5. Active Services
echo "[5/6] Counting active services..."
SERVICE_COUNT=$(systemctl list-units --type=service --state=running | grep -v "UNIT" | wc -l)
echo "Active Services: $SERVICE_COUNT" >> $REPORT_FILE

# 6. App Opening Time (FastWare)
echo "[6/6] Measuring FastWare launch time..."
# Using /usr/bin/time to measure execution time
# Note: This requires 'time' package to be installed
if command -v /usr/bin/time &> /dev/null; then
    LAUNCH_TIME=$(/usr/bin/time -f "%e" fastware 2>&1 | tail -n 1)
    echo "FastWare Launch Time: ${LAUNCH_TIME}s" >> $REPORT_FILE
else
    echo "FastWare Launch Time: N/A (time utility not found)" >> $REPORT_FILE
fi

echo "========================================" >> $REPORT_FILE
echo "Benchmark complete. Report saved to $REPORT_FILE"
cat $REPORT_FILE
