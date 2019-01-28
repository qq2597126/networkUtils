#!/usr/bin/python3
# _*_ coding=utf-8 _*_

# 可以封装成函数，方便 Python 的程序调用
import socket


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def get_ip_num(netmask):
    result = ""
    for num in netmask.split('.'):
        temp = str(bin(int(num)))[2:]
    result = result + temp

    len("".join(str(result).split('0')[0:1]))
    return result


if __name__ == '__main__':

    get_host_ip()
    netmask = '255.255.255.0'

    result = ""

    print
    netmask
    for num in netmask.split(","):
        temp = str(bin(int(num)))[2:]
        result = result + temp
    print
    len("".join(str(result).split('0')[0:1]))
