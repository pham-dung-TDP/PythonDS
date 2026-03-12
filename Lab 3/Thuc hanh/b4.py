n = int(input("Nhập n: "))
for i in range (2 , n+1):
    nt = True
    for j in range(2, i):
        if i % j == 0:
            nt = False
            break
    if nt:
        print(i)