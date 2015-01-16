DNSTester
========

A most easy but powerful DNS pressure tester.

USE WITH YOUR OWN RISK!

THIS SCRIPT IS SOLELY INTENDED TO TEST THE PACKAGE OF ```scapy```!


Usage
------

    python dnsattack.py site-to-test.wtf 10000 100 127.0.0.1 nameservers.csv 15
    
    site-to-test.wtf: Site to test. Please use top domain.
    
    10000: Time to test.
    
    100: Thread number.
    
    127.0.0.1: The source of the package.
    
    nameservers.csv: List of nameservers.
                     Form as provided at http://public-dns.tk/.
                     If not set, will use nameservers.csv.
    
    15: The length of the record to be added.
                    If not set, will use random number from 6 to 32.
                    
    
    
    一个用来测试根DNS鲁棒性的脚本。
    目标是：
    鉴于对于简单测试已经有好的解决办法，同时考虑到单个公共DNS服务器有可能对单个IP之频率进行限制，这里通过在世界范围内查询随机前缀的DNS记录，尝试以较小的代价，在最大范围内对DNS服务器进行稳定性测试。同时，通过控制UDP包结构，让返回值可以在更大范围内被接收，达到更方便的监听的目的。
    在不完整测试中，其有可能造成4X的放大。
    请注意：不当配置有可能造成严重后果，乃至造成服务中断。
    一个典型配置不当的例子：
    
        sudo python dnsattack.py moejn.com 100000000 20 61.155.149.76
        
    有可能造成服务中断。

Requirement
-------

- Python 2.7
- scapy
- May need sudo

License
-----

GNUv2 license.

This program is provided **as is**, with absolutely no warranty.


History
----

0.0.21: Little bit of error handling.

0.0.2: The start of this.

Misc
-----

    legal disclaimer: Usage of DNSTester for attacking targets without prior mutual consent
    is illegal. It is the end user's responsibility to obey all applicable local, state and
    federal laws. Developers assume no liability and are not responsible for any misuse or
    damage caused by this program
    
    ONLY USE IF YOU KNOW WHAT YOU ARE DOING.
