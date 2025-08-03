# simple yes/no if port is open
# library for multithreading
from concurrent.futures import ThreadPoolExecutor
import socket

# port check function, host = ip address, portToCheck is specific port to check
def portCheck(host, portToCheck):
    try:
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scan.settimeout(1) # timeout for connection attempts to prevent stuck
        result = scan.connect_ex((host, portToCheck))
        if result == 0:
            print(f"Port {portToCheck} is open...")
            # send to get head, not all services auto send header ie. MySQL, DNS, HTTP, etc. 
            scan.send(b"HEAD / HTTP/1.0\r\n\r\n")
            # banner to receive specific service information (size 1024 bytes)
            # method -> object
            banner = scan.recv(1024)
            # print the decoded message, remove whitespace with strip()
            print(banner.decode().strip())
        scan.close() # close the socket stream
    except socket.error:
        pass # ignore connection error

def main():

    hostIP = input("IP? ")
    port1 = int(input("Start port? "))
    port2 = int(input("End port? "))
    max_threads = 100

    print(f"Scanning ports {port1} to {port2} on {hostIP}...")
    
    # create thread pool (group of "workers" all doing the same task)
    # with ensures closing of threads / clean up when done
    # executor = task manager
    with ThreadPoolExecutor(max_threads) as executor:
        for port in range(port1, port2 + 1):
            # adds to task queue; each thread receives the function portCheck with the arguments hostIP and port (which increments in for loop of range)
            executor.submit(portCheck, hostIP, port)
    
    print("Scan complete!")


# automatically call main
if __name__ == "__main__":
    main()




