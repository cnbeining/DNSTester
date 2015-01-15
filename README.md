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

0.0.2: The start of this.

Misc
-----

    legal disclaimer: Usage of DNSTester for attacking targets without prior mutual consent
    is illegal. It is the end user's responsibility to obey all applicable local, state and
    federal laws. Developers assume no liability and are not responsible for any misuse or
    damage caused by this program
    
    ONLY USE IF YOU KNOW WHAT YOU ARE DOING.
