temperatures = [44,35,67,81,94,70,48,33,61,36,95,99,83,83,90,68,39,41,53,58,49,38,67,45,58,86,39,96,78,37,58,90,37,69,99,100,74,84,71,33,95,44,84,53,84,86,70,69,53,39,54,64,46,53,63,72,88,47,36,90,70,83,69,33,67,88,69,36,44,33,37,99,35,56,71,31,95,34,40,55,75,96,43,39,77,35,99,68,74,91,62,52,54,40,72,85,96,31,64,99,36,89,36,42,49,82,52,98,99,73,94,42,54,70,43,38,49,50,60,87,76,82,68,52,77,31,36,43,53,39,71,73,55,61,73,58,55,96,64,74,30,97,66,87,34,40,83,94,90,42,81,89,51,39,66,67,79,78,95,62,65,61,65,32,77,71,34,83,30,67,98,53,31,81,78,46,96,35,50,63,61,65,69,43,55,69,32,69,30,48,43,31,65,82,54,91,70,98,49,43,85,89,75,78,88,54,96,47,85,40,37,66,64,84,56,70,93,46,91,62,88,37,92,97,79,66,65,95,94,89,34,38,99,40,48,85,32,58,32,88,60,36,82,42,42,48,60,52,64,45,56,75,85,32,56,63,78,60,61,97,93,64,72,42,44,94,34,48,45,95,50,60,93,32,74,47,84,37,91,32,53,84,62,38,82,68,93,34,49,50,67,68,49,90,54,61,58,77,85,63,60,70,87,65,45,70,87,36,62,37,36,87,94,70,92,58,80,46,60,93,48,85,98,38,87,53,91,34,31,33,84,47,48,93,36,35,62,65,84,32,69,79,95,38,48,52,86,86,37,31,73,81,87,64,60,82,100,58,73,87,56,60,38,37,39,56,45,60,94,88,95,59,87,79,77,48,56,32,95,94,45,55,97,52,88,41,55,86,96,60,32,65,75,93,90,39,56,43,67,76,32,92,39,73,87,87,58,57,64,85,42,77,47,65,42,46,91,91,36,74,77,61,40,61,76,60,70,59,58,79,53,74,42,89,70,74,48,73,65,95,100,70,88,84,80,79,]

res = []
l = len(temperatures)

for i,t in enumerate(temperatures):
    count = 0
    for j, next_t in enumerate(temperatures[i+1:]):
        if next_t > t:
            count +=1
            res.append(count)
            break
        elif j == len(temperatures[i+1:])-1 and next_t <= t:
            res.append(0)
            break
        else:
            count +=1

res.append(0)    
print(res)