import socket
import threading

def port_scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        print(f"[+] Port {port} is open!")
    except:
        print(f"[-] Port {port} is closed!")
    finally:
        s.close()

ip = input("Enter the IP address you want to scan: ")
threads = []

for port in range(1, 100):  # 扫描1-100常用端口
    thread = threading.Thread(target=port_scan, args=(ip, port))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()