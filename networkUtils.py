#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:getNetworkStatus.py
show Windows or Linux network Nic status, such as MAC address, Gateway, IP address, etc
# python getNetworkStatus.py
Routing Gateway:               10.6.28.254
Routing NIC Name:              eth0
Routing NIC MAC Address:       06:7f:12:00:00:15
Routing IP Address:            10.6.28.28
Routing IP Netmask:            255.255.255.0
 """
import os
import sys
import netifaces

def get_net_work():
    routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    routingNicName = netifaces.gateways()['default'][netifaces.AF_INET][1]

    for interface in netifaces.interfaces():
        if interface == routingNicName:
            # print netifaces.ifaddresses(interface)
            routingNicMacAddr = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
            try:
                routingIPAddr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
                # TODO(Guodong Ding) Note: On Windows, netmask maybe give a wrong result in 'netifaces' module.
                routingIPNetmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
            except KeyError:
                pass
    dict = {"routingGateway":routingGateway,"routingNicName":routingNicName,"routingNicMacAddr":routingNicMacAddr,"routingIPAddr":routingIPAddr,routingIPAddr:"routingIPAddr","routingIPNetmask":routingIPNetmask}
    return dict

def get_ip_digit(netmask):
    result = ""
    for num in netmask.split('.'):
        temp = str(bin(int(num)))[2:]
        result = result + temp
    returnNum = len("".join(str(result).split('0')[0:1]))
    #print(returnNum)
    return returnNum