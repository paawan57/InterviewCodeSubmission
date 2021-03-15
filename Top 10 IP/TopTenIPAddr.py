#!/usr/bin/env python

import re
from collections import Counter

#method to return top 10 IP addresses requesting a webserver
def FindTop10IpAddr(WebServerLogsFile):

    cnt = Counter()

    ipre = re.compile(r'^(?P<ip>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) - -')

    with open(WebServerLogsFile) as infile:
        for line in infile:
            m = ipre.match(line)
            if m is not None:
               ip = m.groupdict()['ip']
               cnt[ip] += 1

    #finding most common ip address using most_common function
    most_freq_ipaddr = cnt.most_common(10)
    return( most_freq_ipaddr )

#main method
def main():
    inputFile = 'access.log'
    Top10IpAddr = FindTop10IpAddr(inputFile)
    print("Top 10 Ip Addresses: ", Top10IpAddr)

if __name__ == '__main__':
    main()