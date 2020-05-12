'''
    Class to check if port connection is open or not. 
    
    Author: Clayton Errington
'''
import socket, time

host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 

class PortCheck:
    def __init__(self, domain, port):
        self.domain = domain
        self.port = port
        self.retry = 1
        self.delay = 5
        self.timeout = 3


    def checkOpen(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(self.timeout)
        try:
            s.connect((self.domain, int(self.port)))
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            return True
        except:
            return False
        finally:
            s.close()


    def checkHost(self):
        ipup = False
        for i in range(self.retry):
            if self.checkOpen():
                ipup = True
                break
            else:
                time.sleep(self.delay)
        return ipup
    
    
    def isOpen(self):
        if self.checkHost():
            #print(f"{self.domain}:{self.port} is {Fore.GREEN}OPEN {Fore.RESET}")
            return True
        else:
            #print(f"{Fore.RED}{self.domain}:{self.port} is CLOSED {Fore.RESET}")
            return False


if __name__ == "__main__":
    test = PortCheck("google.com", 443)
    test2 = PortCheck("google.com", 25).isOpen()
    print(test.isOpen())
    print(test2)
