#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import serial
import time
import datetime
import psutil
import logging
import datetime
import json
import socket
from hurry.filesize import size
from subprocess import check_output

# ___________________VARIABLES___________________#
# sys_disk = "/dev/mmcblk1p1"
# eth_interface = "eth0"
# com = "/dev/ttyUSB0"

# Windows variables
sys_disk = "C:/"
eth_interface = "Ethernet"
com = "COM20"
# _______________________________________________#

target = serial.Serial(com, 9600)


def run_cmd(cmd):
    return check_output(cmd, shell=True).decode('utf-8')


def cpu_usage():
    cpuUsage = psutil.cpu_percent(interval=0, percpu=False)
    return cpuUsage


def ram_percent():
    cpuPercent = psutil.virtual_memory().percent
    return cpuPercent


def ram_total():
    ramTotal = size(psutil.virtual_memory().total)
    return ramTotal


def ram_used():
    ramUsed = size(psutil.virtual_memory().used)
    return ramUsed


def sys_disk_total():
    sysDiskTotal = size(psutil.disk_usage(sys_disk).total)
    return sysDiskTotal


def sys_disk_free():
    sysDiskFree = size(psutil.disk_usage(sys_disk).free)
    return sysDiskFree


def up_from():
    upFrom = datetime.datetime.fromtimestamp(
        psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return upFrom


def uptime():
    upTime = datetime.timedelta(
        seconds=round(time.time() - psutil.boot_time()))
    return upTime


def net_stats():
    netStats = psutil.net_io_counters(pernic=True, nowrap=True)[eth_interface]
    return netStats


def net_in():
    netIn = size(psutil.net_io_counters(
        pernic=True, nowrap=True)[eth_interface].bytes_recv)
    return netIn


def net_out():
    netOut = size(psutil.net_io_counters(
        pernic=True, nowrap=True)[eth_interface].bytes_sent)
    return netOut


def hostaname():
    name = run_cmd("hostname")
    return name


def host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
    local_ip = s.getsockname()[0]
    return local_ip


def get_data():
    data = {
        "hostname": str(hostaname()),
        "ip": str(host_ip()),
        "uptime": str(uptime()),
        "cpu_usage": str(cpu_usage()),
        "ram_percent": str(ram_percent()),
        "ram_total": str(ram_total()),
        "ram_used": str(ram_used()),
        "sys_disk_total": str(sys_disk_total()),
        "sys_disk_free": str(sys_disk_free()),
        "up_from": str(up_from()),
        "net_in": str(net_in()),
        "net_out": str(net_out()),
    }
    return json.dumps(data)


def main():
    while True:
        print(datetime.datetime.now())
        print(get_data().encode('ascii'))
        target.write(get_data().encode('ascii'))
        time.sleep(0.5)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('Exited')
