import math
n = int(input("Nhập n: "))
i = 1
s= 0
while i<=n:
    if i % 2 == 1:
        s += 1/i 
    else:
        s -= 1/i
    i += 1
print("S= ",s)

n =int(input("Nhập n: "))
i = 1 
s = 0 
while i <= n:
    s += 1/(i*(i+1))
    print(1,"/",(i*(i+1)))
    i+=1
print ("s= ",s)


n =int(input("Nhập n: "))
i = 2
s = 0
while i <= n:
    s += 1 / math.sqrt(i)
    i += 1
print("s= ",s)