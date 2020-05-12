# netutils

Python module to check the status of ports for local and websites. 

# Install
pip install netutils

# Usage
```python 
import netutils
google = netutils.PortCheck("google.com", 443)
google.isOpen()
```

For extra help I've added in variables to find the hostname and local IP address. 
- To get hostname: netutils.host_name
- To get Local IP: netutils.host_ip