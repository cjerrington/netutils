import socket, time


__all__ = ['netutil']
__version__ = "0.0.7"
__author__ = "Clayton Errington"


class PortCheck:
    def __init__(self, domain, port):
        self.domain = domain
        self.port = port
        self.retry = 1
        self.delay = 5
        self.timeout = 3


    def __call__(self, domain, port):
        self.domain = domain
        self.port = port


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
            # If connects, then we are true
            return True
        else:
            # If connection fails, we are false
            return False


    def domain(self):
        # Allow for domain to be returned
        return self.domain


    def port(self):
        # Allow for port to be returned
        return self.port
     

# return variables for use
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name) 
isOpen = PortCheck.isOpen
domain = PortCheck.domain
port = PortCheck.port
