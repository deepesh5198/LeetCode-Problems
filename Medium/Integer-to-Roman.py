# Problem Description:
# Convert an Integer value to its Roman value

# EXAMPLE:

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def intToRoman(num: int) -> str:
    res = ""
    mapping = {
                1000:'M',
                900:'CM',
                500:'D',
                400:'CD',
                100:'C',
                90:'XC',
                50:'L',
                40:'XL',
                10:'X',
                9:'IX',
                5:'V',
                4:'IV',
                1:'I'   
    }

    for k, val in mapping.items():
        d = num//k 
        num = num%k

        res += val*d

    return res


