from time import sleep

print("Vẽ 4 hình mỗi hình xuất hiện sau 3 giây")
print("---------------------------------------")
# --------------------Hàm hình 1--------------------

def so_le_hinh1(a,b):
    # In ra cái tam giác ở dưới
    if a in range(nhap_cao // 2,nhap_cao) and b in range(nhap_cao//2 +1):
        if a + b <= nhap_cao - 1:
            print(" * ", end="")
        else:
            print("   ", end="")
    # In ra cái tam giác ở trên
    elif a in range(nhap_cao // 2 + 1) and b in range(nhap_cao // 2, nhap_cao):
        if b - a <= nhap_cao // 2:
            print(" * ", end="")
        else:
            print("   ", end="")
    else:
        print("   ", end="")


def so_chan_hinh1(a,b):
    # In ra cái tam giác ở dưới
    if a in range(nhap_cao // 2 - 1, nhap_cao) and b in range(nhap_cao // 2 + 1):
        if a + b <= nhap_cao - 1:
            print(" * ", end="")
        else:
            print("   ", end="")
    # In ra cái tam giác ở trên
    elif a in range(nhap_cao // 2) and b in range(nhap_cao // 2, nhap_cao):
        if b - a <= nhap_cao // 2:
            print(" * ", end="")
        else:
            print("   ", end="")
    else:
        print("   ", end="")




# --------------------Hàm hình 2--------------------

def so_le_hinh2(a,b):
    # In ra cái tam giác ở dưới
    if a in range(nhap_cao2 // 2, nhap_cao) and b in range(nhap_cao2 // 2 + 1):
        if a + b == nhap_cao2 - 1:
            print(" * ", end="")
        elif b == 0 or a == nhap_cao2 // 2:
            print(" * ", end="")
        else:
            print("   ", end="")
    # In ra cái tam giác ở trên
    elif a in range(nhap_cao2 // 2 + 1) and b in range(nhap_cao2 // 2, nhap_cao2):
        if b - a == nhap_cao2 // 2:
            print(" * ", end="")
        elif a == nhap_cao2 // 2 or b == nhap_cao2 // 2:
            print(" * ", end="")
        else:
            print("   ", end="")
    else:
        print("   ", end="")


def so_chan_hinh2(a,b):
    # In ra cái tam giác ở dưới
    if a in range(nhap_cao2 // 2 -1, nhap_cao2) and b in range(nhap_cao2 // 2 + 1):
        if a + b == nhap_cao2 - 1:
            print(" * ", end="")
        elif b == 0 or a == nhap_cao2 // 2 -1 :
            print(" * ", end="")
        else:
            print("   ", end="")
    # In ra cái tam giác ở trên
    elif a in range(nhap_cao2 // 2) and b in range(nhap_cao2 // 2, nhap_cao2):
        # In đường chéo
        if b - a == nhap_cao2 // 2:
            print(" * ", end="")
        elif a == nhap_cao2 // 2 - 1 or b == nhap_cao2 // 2:
            print(" * ", end="")
        else:
            print("   ", end="")
    else:
        print("   ", end="")




# --------------------Hàm hình 3--------------------

def so_le_hinh3(a,b):
    # In ra cái tam giác bên trên
    if b in range(nhap_cao3 // 2,nhap_cao3) and a in range(nhap_cao3//2 + 1):
        if b + a <= nhap_cao3 - 1:
            print(" * ", end="")
        else:
            print("   ", end="")
    # In ra cái tam giác bên dưới
    elif b in range(nhap_cao3 // 2 + 1) and a in range(nhap_cao3 // 2,nhap_cao3):
        if b + a >= nhap_cao3 - 1:
            print(" * ", end="")
        else:
            print("   ", end="")
    else:
        print("   ", end="")

def so_chan_hinh3(a,b):
    # In ra cái tam giác bên trên
    if b in range(nhap_cao3 // 2,nhap_cao3) and a in range(nhap_cao3//2):
        if b + a <= nhap_cao3 - 1:
            print(" * ", end="")
        else:
            print("   ", end="")
    # In ra cái tam giác bên dưới
    elif b in range(nhap_cao3 // 2 + 1) and a in range(nhap_cao3//2 - 1,nhap_cao3):
        if b + a >= nhap_cao3 - 1:
            print(" * ", end="")
        else:
            print("   ", end="")
    else:
        print("   ", end="")




# --------------------Hàm hình 4--------------------

def so_le_hinh4(a,b):
    # In ra cái tam giác bên trên
    if b in range(nhap_cao4//2,nhap_cao4) and a in range(nhap_cao4//2 + 1):
        if b + a == nhap_cao4 - 1:
            print(" * ", end="")
        elif a == 0:
            print(" * ", end="")
        elif b == nhap_cao4 // 2:
            print(" * ", end="")
        else:
            print("   ", end="")
    # In ra cái tam giác bên dưới
    elif b in range(nhap_cao4 // 2 + 1) and a in range(nhap_cao4 // 2,nhap_cao4):
        if b + a == nhap_cao4 - 1:
            print(" * ", end="")
        elif a == nhap_cao4 - 1:
            print(" * ", end="")
        elif b == nhap_cao4 // 2:
            print(" * ", end="")
        else:
            print("   ", end="")
    else:
        print("   ", end="")

def so_chan_hinh4(a,b):
    if b in range(nhap_cao4 // 2, nhap_cao4) and a in range(nhap_cao4 // 2 + 1):
        if b + a == nhap_cao4 - 1:
            print(" * ", end="")
        elif a == 0:
            print(" * ", end="")
        elif b == nhap_cao4 // 2:
            print(" * ", end="")
        else:
            print("   ", end="")
    # In ra cái tam giác bên dưới
    elif b in range(nhap_cao4 // 2 + 1) and a in range(nhap_cao4 // 2 - 1, nhap_cao4):
        if b + a == nhap_cao4 - 1:
            print(" * ", end="")
        elif a == nhap_cao4 - 1:
            print(" * ", end="")
        elif b == nhap_cao4 // 2:
            print(" * ", end="")
        else:
            print("   ", end="")
    else:
        print("   ", end="")

#---------------Hàm khởi chạy tạo hình---------------
def chay1():
    print("\nĐây là hình số 1 !")
    for a in range(nhap_cao):
        for b in range(nhap_cao):
            if nhap_cao % 2 != 0:
                so_le_hinh1(a, b)
            else:
                so_chan_hinh1(a, b)
        print()
    sleep(3)

def chay2():
    print("\nĐây là hình số 2 !")
    for a in range(nhap_cao2):
        for b in range(nhap_cao2):
            if nhap_cao2 % 2 != 0:
                so_le_hinh2(a, b)
            else:
                so_chan_hinh2(a, b)
        print()
    sleep(3)

def chay3():
    print("\nĐây là hình số 3 !")
    for a in range(nhap_cao3):
        for b in range(nhap_cao3):
            if nhap_cao3 % 2 != 0:
                so_le_hinh3(a, b)
            else:
                so_chan_hinh3(a, b)
        print()
    sleep(3)

def chay4():
    print("\nĐây là hình số 4 !")
    for a in range(nhap_cao4):
        for b in range(nhap_cao4):
            if nhap_cao4 % 2 != 0:
                so_le_hinh4(a, b)
            else:
                so_chan_hinh4(a, b)
        print()


# Bắt đầu tạo hình
while True:
    try:
        nhap_cao = int(input("Nhập vào chiều cao hình 1 : "))

        nhap_cao2 = int(input("Nhập vào chiều cao hình 2: "))

        nhap_cao3 = int(input("Nhập vào chiều cao hình 3: "))

        nhap_cao4 = int(input("Nhập vào chiều cao hình 4: "))

        chay1()
        chay2()
        chay3()
        chay4()
    except ValueError:
        print("Má nó nhập số thôi cũng sai hả thằng đầu buồi ?")
        continue
    else:
        break