import optparse
import nmap
from datetime import datetime
from termcolor import colored





def networkScanner(targetH,tPort):
    print ("-" * 65)
    print ("Please wait, while we scanning remote host", targetH)
    print ("-" * 55)
    startTime = datetime.now()
    nmpScan = nmap.PortScanner()
    nmpScan.scan(targetH,tPort)
    
    
    
    # nmpScan['127.0.0.1'].hostname() # get one hostname for host 127.0.0.1, usualy the user record
    # nmpScan['127.0.0.1'].hostnames() # get list of hostnames for host 127.0.0.1 as a list of dict
    for host in nmpScan.all_hosts():
         print(colored(colored('HOST  : %s (%s)','yellow') % (host, nmpScan[host].hostname())))
         print(colored(colored('STATE : %s','yellow') % nmpScan[host].state()))
         print(colored("---------------------------------",'cyan'))

         
         for protokol in nmpScan[host].all_protocols():
             print(colored("*********************************",'cyan'))
             print("PROTOCOL %s "%protokol)
             print(colored("*********************************",'cyan'))

             # print(colored("---------------------------------",'cyan'))

             
             host_ports = nmpScan[host][protokol].keys() 
             
             for hports in host_ports:
                 if nmpScan[host][protokol][hports]['state'] == 'open':
                  print (colored('[+] port : %s\t state : %s' % (hports, nmpScan[host][protokol][hports]['state'])+"\n",'green'))
                 else:
                  print (colored('[-] port : %s\t state : %s' % (hports, nmpScan[host][protokol][hports]['state'])+"\n",'red'))

                  
    endTime = datetime.now()
    total =  endTime - startTime
    print ('Scanning Completed in: ', total)

    
    
def main():
    parser = optparse.OptionParser('USAGE:'+'-H < Target Host > -p < Target port >')
    parser.add_option('-H', dest='tHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tPort', type='string', help='specify target ports  either range or list e.g 21-443 | 1,2,4... ')
    (options,args) = parser.parse_args()
    
    tHost = options.tHost
    tPort = options.tPort
    
    
    if (tHost == None) | (tPort == None):
        print (parser.usage)
        exit(0)
        
    networkScanner(tHost, tPort)
    
    
    
    

if __name__ == '__main__':
        main()
