import math
big = 600851475143
for i in range (3, 150000000000):
    factor = big/i
    if (math.floor(factor) * i == big and math.ceil(factor) * i == big):
        for j in range (3, i+1):
            factor2 = i/j
            if (math.floor(factor2) *j == i and math.ceil(factor2) * j == i):
                print("Not Perfect", j)
            elif(j == i):
                print("Perfect", i)

# Requires reentering large factors to check for 'primeness', but it works
