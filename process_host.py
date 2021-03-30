import subprocess
import multiprocessing
import time

T1 = time.perf_counter()
i = 0
hosts = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '8.8.8.8', '8.8.4.4']

def check_host():
    status, result = subprocess.getstatusoutput("ping -c 1" + hosts[i])
    if (status == 0):
        print(f'Host {hosts[i]} is UP')
    else:
        print(f'Host {hosts[i]} id DOWN')
Processes = []

for x in range(len(hosts)):
    P = multiprocessing.Process(target = check_host)
    P.start()
    Processes.append(P)
    i += 1

for process in Processes:
    process.join()

T2 = time.perf_counter()
print(f"Selesai dalam : {round(T2 - T1, 2)} Detik")
