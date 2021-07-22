"""
Given a valid IP address return a defanged version
where all the periods "." are replaced with [.]
"""

test = "1234.123.12.1"

# Input is a string containing an IP address
def defangedIP(ip):
    return ip.replace('.', '[.]')

print(defangedIP(test))