#!/usr/bin/python3

# _*_ coding=utf-8 _*_
import logging
from queue import Queue

from scapy.layers.l2 import ARP, Ether

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
print("first")

if __name__ == "__main__":
    queue = Queue()
    queue.put({"ip":1,"mac":2})
    queue.put({"ip":2,"mac":3})
    queue.put({"ip":3,"mac":4})
    print(queue.qsize())
    while not queue.empty():
        ipAndMac = queue.get();
        print("IP %s Mac %s"%(1, 2))
