#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
from termcolor import colored

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
host    = input("Enter a host to scan: ")
hostIP  = socket.gethostbyname(host)


print ("-" * 50)
print ("Please wait, scanning remote host", hostIP)
print ("-" * 60)

start = datetime.now()

def main():
    
    try:
        for port in range(1-81):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((hostIP, port))
            if result == 0:
                print (colored("Port %s:      Open",'green') %port)
            else: 
                print (colored("Port %s:      Closed",'red') %port)
                
            sock.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting Now...')
        sys.exit()

    except socket.error:
        print ("An Error Occured ,Couldn't connect to server")
        sys.exit()


    end = datetime.now()

    total =  end - start


    print ('Scanning Completed in: ', total)

  

if __name__ == '__main__':
        main()
