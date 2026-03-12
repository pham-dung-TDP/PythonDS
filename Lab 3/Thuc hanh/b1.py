n = int(input("Nhập n: "))
s = 1
tu = 2 
mau = 3 
for i in range (1 , n+1):
    s = s + tu / mau
    tu = tu + 2
    mau = mau + 2
print("S= ", s )