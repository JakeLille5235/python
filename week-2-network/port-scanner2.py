# simple yes/no if port is open
# library for multithreading
from concurrent.futures import ThreadPoolExecutor
import socket

# create dictionary for getBanner function
# Dictionary = IF connected to # 21, 25, 80, etc. send THIS message to receive response/test
# defines the "hello" message to each service, grabbable from the dictionary
BANNER_TRIGGERS = {
    21: b"HELP\r\n", # FTP
    25: b"EHLO test.com\r\n", #SMTP
    80: b"HEAD / HTTP/1.0\r\n\r\n", #HTTP
    110: b"USER test\r\n", #POP3
    143: b"a001 CAPABILITY\r\n", #IMAP
    3306: None, # MySQL
    5432: None, # Postgres default port
}


# port check function, host = ip address, portToCheck is specific port to check
def portCheck(host, portToCheck):
    try:
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scan.settimeout(1) # timeout for connection attempts to prevent stuck
        result = scan.connect_ex((host, portToCheck))
        if result == 0:
            print(f"Port {portToCheck} is open...")
            
            banner = getBanner(scan, portToCheck)
            # print the decoded message, remove whitespace with strip()
            print(banner)
        scan.close() # close the socket stream
    except socket.error:
        pass # ignore connection error

# intelligent banner grabbing (pass the socket instance object and specific port # from iteration...
# socket object analogy for reference: socket() = pull out phone, connect_ex() = dial the number, sock = live call, send() = say something, recv() =  hear response
def getBanner(socketObject, port):
    try:
        trigger = BANNER_TRIGGERS.get(port)

        # if trigger is not null/empty, send to socketObject
        if trigger:
            socketObject.send(trigger)
        # banner variable stores received message
        banner = socketObject.recv(1024)
        # decodes the message, errors="ignore" ignores unreadable letters
        return banner.decode(errors="ignore")
    
    except:
        return None

def main():

    hostIP = input("IP? ")
    port1 = int(input("Start port? "))
    port2 = int(input("End port? "))
    # max concurrent threads for ThreadPool
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




