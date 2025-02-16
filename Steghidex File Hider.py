import socket
import threading
import logging

# Configure logging
logging.basicConfig(filename="honeyscan.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            sock.send(b"Hello")  # Send a probe message
            response = sock.recv(1024)
            logging.info(f"Port {port} is open. Response: {response.decode(errors='ignore')}")
            print(f"[+] Port {port} is open and responded!")
        else:
            print(f"[-] Port {port} is closed")
        
        sock.close()
    except Exception as e:
        logging.error(f"Error scanning port {port}: {e}")

def honeyscan(target, start_port, end_port):
    print(f"Starting HoneyScan on {target}...")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    honeyscan(target_ip, start_port, end_port)
    print("Scan complete. Check honeyscan.log for details.")
