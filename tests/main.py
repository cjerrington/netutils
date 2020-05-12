import netutil

print(f"Version: {netutil.__version__}")

google = netutil.PortCheck("google.com", 443)
google2 = netutil.PortCheck("google.com", 123)

facebook = netutil.PortCheck("facebook.com", 443)
website = netutil.PortCheck("claytonerrington.com", 443)

local = netutil.PortCheck("127.0.0.1", 85)


# Getting basic Information
print(f"Your hostname is: {netutil.host_name}")
print(f"Your local IP is: {netutil.host_ip}")

# Different testing

print(f"Testing {google.domain}... ")
if(google.isOpen()):
    print(f"    {google.domain}:{google.port} is Open!")
else:
    print(f"    {google.domain}:{google.port} is Closed!")


print(f"Testing {google2.domain}:{google2.port}... ")
if(google2.isOpen()):
    print(f"    {google2.domain}:{google2.port} is Open!")
else:
    print(f"    {google2.domain}:{google2.port} is Closed!")

print(f"Testing {facebook.domain}:{facebook.port}... {facebook.isOpen()}")
print(f"Testing {website.domain}:{website.port}... {website.isOpen()}")
print(local.isOpen())