n = int(input("Nhập n: "))
dao = 0
temp = n
while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10
if n == 0:
    print("không")
while dao > 0:
    so = dao % 10
    if so == 0: print("không", end=" ")
    elif so == 1: print("một", end=" ")
    elif so == 2: print("hai", end=" ")
    elif so == 3: print("ba", end=" ")
    elif so == 4: print("bốn", end=" ")
    elif so == 5: print("năm", end=" ")
    elif so == 6: print("sáu", end=" ")
    elif so == 7: print("bảy", end=" ")
    elif so == 8: print("tám", end=" ")
    elif so == 9: print("chín", end=" ")
    dao //= 10
