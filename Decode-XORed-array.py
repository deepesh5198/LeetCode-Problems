def decodeXORed(encoded, first):
    #encoded = [6,2,7,3], first = 4
    #decoded = [4,2,0,7,4]
    
    #decoded[0] = first
    #decoded[1] = encoded[0]-decoded[0]
    #decoded[2] = encoded[1]-decoded[1]
    #decoded[3] = encoded[2]-decoded[2]
    #decoded[4] = encoded[3]-decoded[3]
        
    decoded = []
    decoded.append(first)
    
    if len(encoded) == 1:
        decoded.append((encoded[0] + decoded[0]))
        return decoded
    else:
        for i in range(len(encoded)):
            decoded.append(abs(encoded[i] - decoded[i]))
            
        return decoded

print(decodeXORed(encoded = [6], first = 1))