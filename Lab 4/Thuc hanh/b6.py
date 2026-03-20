a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
bcnn = a if a > b else b
while True:
    if bcnn % a == 0 and bcnn % b == 0:
        print("BCNN là:", bcnn)
        break
    bcnn += 1