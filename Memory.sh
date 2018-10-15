 free -h
 cat /proc/meminfo
 ps -eo pid,ppid,%mem,%cpu,cmd --sort=-%mem | head -n10
 