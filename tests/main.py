import netutils

test = PortCheck("google.com", 443)
test2 = PortCheck("google.com", 25)

facebook = PortCheck("facebook.com", 443)
website = PortCheck("claytonerrington.com", 443)


# Getting basic Information
print(f"Your hostname is: {host_name}")
print(f"Your local IP is: {host_ip}")

# Different testing
print(f"Testing {test.domain}:{test.port}... ")
if(test.isOpen()):
    print(f"    {test.domain}:{test.port} is Open!")
else:
    print(f"    {test.domain}:{test.port} is Closed!")

print(f"Testing {test2.domain}:{test2.port}... ")
if(test2.isOpen()):
    print(f"    {test2.domain}:{test2.port} is Open!")
else:
    print(f"    {test2.domain}:{test2.port} is Closed!")

print(f"Testing {facebook.domain}:{facebook.port}... {facebook.isOpen()}")
print(f"Testing {website.domain}:{website.port}... {website.isOpen()}")

