#!/usr/bin/python3

# _*_ coding=utf-8 _*_



#   清除报错

import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *



#构造发送数据包并接受响应函数，两个参数，一个IP地址，一个队列，默认为None

def arp_request(ip_address,queue=None):

    #发送二层数据帧

    result_raw=srp(Ether(dst='FF:FF:FF:FF:FF:FF')/ARP(op=1,hwdst='00:00:00:00:00:00',pdst=ip_address,timeout=1,verbose=False))

    try:

        #把响应的数据包对，产生清单

        result_list=result_raw[0].res

        #[0]第一组响应数据包

        #[1]接收到的包，[0]为发送的数据包

        #[1]ARP头部字段中的['hwsrc']字段，作为返回值返回

        if queue==None:

            return result_list[0][1].getlayer(ARP).fields['hwsrc']

        else:

            queue.put((ip_address,result_list[0][1].getlayer(ARP).fields['hwsrc']))

    except: 

        return


if __name__=='__main__':

    import sys

    print(arp_request(sys.argv[1]))

#-