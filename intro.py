import math

# 1.
for i in range(20, 9, -1):
    print(i)

# 2.
def build_reverse(): return [x for x in range(20,9,-1)]

# 3.
for i in range(20,9,-1):
    if i % 2 == 0:
        print(i)

# 4.
def build_reverse_even(): return [x for x in range(20,9,-1) if x%2 ==0]

# 5.

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
for i in range(1, 21):
    if i % 5 == 0:
        print('Good:', i)
    if is_prime(i):
        print('Job:', i)

# 8.
import math

def gomp(a,b,c,t):
    return a*math.exp(-b*math.exp(-c*t))

# 9.
if __name__ == '__main__':
    def bocks(width, height):
        print('*'*width)
        for i in range(height-2):
            print('*' + ' '*height + '*')
        print('*'*width)

# 10
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 11
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self,x2,y2):
        return math.sqrt((x2-self.x)**2 + (y2-self.y)**2)

# 12.
class Line:
    def __init__ (self, point1, point2):
