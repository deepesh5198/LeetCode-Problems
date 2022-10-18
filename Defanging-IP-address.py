# Problem Description: Given a valid (IPv4) IP address,
# return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

#EXAMPLE:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


def defangIPaddress(address):
    address = address.replace(".","[.]")

    return address

print(defangIPaddress("1.1.1.1"))