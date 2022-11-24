# Problem Description:
# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, 
# and you need convert it to the form of 0+2i.

def complexNumberMultiply(num1: str, num2: str) -> str:
    # split the both num1 at '+'
    num1 = num1.split("+")

    # split the imaginary part into
    # ['number', 'i']
    num1[1] = num1[1].split("i")
    num1[1][1] = 'i'

    # split the both num2 at '+'
    num2 = num2.split("+")

    # split the imaginary part into
    # ['number', 'i']
    num2[1] = num2[1].split("i")
    num2[1][1] = 'i'

    # use eval to solve the parts of the strings    
    expr = (str(eval(num1[0]+'*'+num2[0]))+
            '+'+str(eval(num1[0] +'*'+num2[1][0]))+'i'+ 
            '+'+
            str(eval(num1[1][0]+'*'+num2[0]))+'i'+
            '+'+str(-(eval(num1[1][0]+'*'+num2[1][0]))))

    # split the expr at '+'
    expr = expr.split("+")

    # split the imaginary part into
    # ['number', 'i']
    expr[1] = expr[1].split('i')
    expr[1][1] = 'i'

    # split the imaginary part into
    # ['number', 'i']
    expr[2] = expr[2].split('i')
    expr[2][1] = 'i'

    # use eval to solve the parts of the strings in expr list
    # and make a string
    res = (str(eval(expr[0]+'+'+expr[-1]))
            +'+'+str(eval(expr[1][0]
            +'+'+expr[2][0]))+'i')
        
    # return the final solution string
    return res

print(complexNumberMultiply(num1 = "1+-1i", num2 = "1+-1i"))