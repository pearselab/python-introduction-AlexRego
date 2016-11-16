# 1.
for i in range(20,9,-1):
    print(i)

# 2.
def build_reverse(): return [x for x in range(20,9,-1)]

# 3.
for i in range(20,9,-1):
    if (i % 2 == 0):
        print(i)

# 4.
def build_reverse_even(): return [x for x in range(20,9,-1) if x%2 ==0]

# 5.
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for d in range(2, int(math.sqrt(n))+1):
        if n % d == 0:
            return False
    return True

# 6.
with open('file_name') as handle:
    for line in handle:
        print(line[5])

# 7.
for i in range(1,21):
    if i % 5 == 0:
        print('Good:', i)
    if is_prime(i):
        print('Job:', i)

# 8.
import math

def gomp(a,b,c,t):
    return a*math.exp(-b*math.exp(-c*t))

# 9.
