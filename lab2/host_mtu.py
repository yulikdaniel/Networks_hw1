import os
from math import log2, ceil
import sys


def check_icmp():
    command = "cat /proc/sys/net/ipv4/icmp_echo_ignore_all"
    process = os.popen(command, 'r')
    if process.read().strip() == '0':
        return True
    return False


def ping(host, size, packets=1, retry=1):
    command = "ping -M do -s {} -c {} {} 2>&1"
    for _ in range(retry):
        try:
            process = os.popen(command.format(size, packets, host), 'r')
            res = process.read()
            prc = process.close()
            if prc is None:
                return True
            if res.find("mtu") != -1:
                return False
        except:
            pass
    return False


def host_mtu(host):
    l, r = 0, 10000
    while l + 1 < r:
        print("Approximately", ceil(log2(r - l)), "steps left")
        sys.stdout.flush()
        m = (l + r) // 2
        if ping(host, m):
            l = m
        else:
            r = m
    return l


if __name__ == "__main__":
    if not check_icmp():
        print("ICMP is blocked, sorry...")
    else:
        host = input("Enter the host: ")
        if not ping(host, size=1, packets=1, retry=5):
            print("Can't access host, sorry... Probably a typo?")
        else:
            print("The required mtu is {}".format(host_mtu(host)))