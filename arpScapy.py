#!/usr/bin/python3

# _*_ coding=utf-8 _*_


import logging

from concurrent.futures.thread import ThreadPoolExecutor
from queue import Queue
from arpUtils.getIP import get_host_ip
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp

from arpUtils.networkUtils import get_net_work, get_ip_digit

logging.getLogger('scapy.runtime').setLevel(logging.ERROR)

import ipaddress


def arp_scan(network):
    threadPool = ThreadPoolExecutor(3)
    queue = Queue()

    net = ipaddress.ip_network(network, False)
    print(net)
    for ip in net:
        ip_addr = str(ip)
        print(ip_addr)
        threadPool.submit(arp_request(ip_addr, queue))
    threadPool.shutdown()
    return queue


def arp_request(ip_address, queue=None):
    # 发送二层数据帧

    result_raw = srp(Ether(dst='FF:FF:FF:FF:FF:FF') / ARP(op=1, hwdst='00:00:00:00:00:00', pdst=ip_address),
                     timeout=1, verbose=False)

    try:

        # 把响应的数据包对，产生清单

        result_list = result_raw[0].res

        # [0]第一组响应数据包

        # [1]接收到的包，[0]为发送的数据包

        # [1]ARP头部字段中的['hwsrc']字段，作为返回值返回
        hwsrc = result_list[0][1].getlayer(ARP).fields['hwsrc']
        if queue is None:

            print("MAC", hwsrc)
            return hwsrc
        else:
            print("MAC", hwsrc)
            queue.put({"ip": ip_address, "mac": hwsrc})
    except:
        return


if __name__ == '__main__':
    active_ip_mac = arp_scan(get_net_work()["routingIPAddr"]+"/"+str(get_ip_digit(get_net_work()["routingIPNetmask"])))
    print('活动IP与MAC地址如下:')
    while not active_ip_mac.empty():
        print("ip：%s  mac:%s"%(active_ip_mac.get()['ip'],active_ip_mac.get()['mac']))

    print('总个数为：' + str(active_ip_mac.qsize()))
