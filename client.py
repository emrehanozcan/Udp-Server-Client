import socket
import time

with open("targethosts.txt") as f:
    dosya = f.read().splitlines() 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
count=1
for ip in dosya:
    server_addr = (ip,12345)
    sock.settimeout(1)
    print("#"+str(count)+". Target: "+ip)
    count+=1

    for i in range(1, 6):
       start = int(time.time() * 1000)
       message = b"Ping"
       try:
           sent = sock.sendto(message, server_addr)
           data, server = sock.recvfrom(4096)
           print("#"+str(i)+". => UDP:"+ip)
           end = int(time.time() * 1000)
           rtt_time = end - start
           print("#"+str(i)+". <= RTT: "+str(rtt_time)+"ms")
       except socket.timeout:
           print("#"+str(i)+". Packet Loss")
