# netutil - Checking Port Status

Python module to check the status of ports for local and websites the easy way. 

# Install
```shell
pip install netutil
```

# Usage
```python 
import netutil
google = netutil.PortCheck("google.com", 443)
print(google.domain)
print(google.port)
print(google.isOpen())
```

This will show:
```shell
google.com
443
True
```

Check out the tests\main.py for more examples.

For extra help I've added in variables to find the hostname and local IP address. 
- To get hostname: netutil.host_name
- To get Local IP: netutil.host_ip

# Links
- [PyPi](https://pypi.org/project/netutil/)
- [GitHub](https://github.com/cjerrington/netutils)
