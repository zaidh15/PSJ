import subprocess
import concurrent.futures
import time

T1 = time.perf_counter()

hosts = ['192.168.0.1', '192.168.0.2', '192.168.0.6', '8.8.8.8', '8.8.4.4']
def check_host(ip):
    status, result = subprocess.getstatusoutput("ping -c1 " + ip)
    if (status == 0):
        return f'Host {ip} is UP'
    else:
        return f'Host {ip} is DOWN'

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(check_host, hosts)
    for results in results:
        print(results)

T2 = time.perf_counter()

print(f"selesai dalam : {round(T2 - T1, 2)} detik")