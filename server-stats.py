#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import serial
import time
import datetime
import psutil
import logging
import datetime
import json
from hurry.filesize import size
from subprocess import check_output

# ___________________VARIABLES___________________#
sys_disk = "/dev/mmcblk1p1"
eth_interface = "eth0"
# _______________________________________________#


def run_cmd(cmd):
    return check_output(cmd, shell=True).decode('utf-8')


esp = serial.Serial('/dev/ttyUSB0', 9600)

cpu_usage = psutil.cpu_percent(interval=0, percpu=False)

ram_percent = psutil.virtual_memory().percent
ram_total = size(psutil.virtual_memory().total)
ram_used = size(psutil.virtual_memory().used)

sys_disk_total = size(psutil.disk_usage(sys_disk).total)
sys_disk_free = size(psutil.disk_usage(sys_disk).free)

up_from = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(
    "%Y-%m-%d %H:%M:%S"
)


def uptime():
    time = run_cmd("uptime | awk 'NR==1{printf $3}' | tr -d ','")
    return time


net_stats = psutil.net_io_counters(pernic=True, nowrap=True)[eth_interface]
net_in = size(
    psutil.net_io_counters(pernic=True, nowrap=True)[eth_interface].bytes_recv
)
net_out = size(
    psutil.net_io_counters(pernic=True, nowrap=True)[eth_interface].bytes_sent
)


def hostaname():
    name = run_cmd("hostname")
    return name

# def host_ip():
#     ip = run_cmd("ip -o addr show scope global | awk 'NR==1{split($4, a, "/"); print $2" : "a[1]}'")
#     return ip


def host_ip():
    ip = run_cmd("uname -r")
    return ip


def get_data():
    return {
        "cpu_usage": str(cpu_usage),
        "ram_percent": str(ram_percent),
        "ram_total": str(ram_total),
        "ram_used": str(ram_used),
        "up_from": str(up_from),
        "uptime": str(uptime()),
        "net_in": str(net_in),
        "net_out": str(net_out),
    }

# for i in all_data:
    # esp.write(i.encode())
    # print(i.encode())
    # time.sleep(1)
# esp.close()


def main():
    while True:
        print(datetime.datetime.now())
        # print(json.loads(json.dumps(get_data)))
        print(get_data())
        time.sleep(3)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('Exited')
