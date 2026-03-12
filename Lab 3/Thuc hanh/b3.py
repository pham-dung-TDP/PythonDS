n = int(input("Nhập n: "))
nt = True 
if n < 2:
    nt = False
else:
    for i in range(2, n):
        if n % i == 0:
            nt = False
            break
