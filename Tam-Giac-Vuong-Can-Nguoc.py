print("Dinh Quy Pham")
print("Một bài toán hay về tam giác vuông cân góc phải dưới")
print("-" * 35)

nhap_dai = None
while True:
    try:
        nhap_dai = int(input("Nhập vào chiều cao tam giác : "))
        for a in range(nhap_dai):
            for b in range(nhap_dai):
                # Chỗ này là bài toán hơi ngược, vẽ ra giấy sẽ thấy
                if b < (nhap_dai - 1) - a:
                    print("   ", end="")
                else:
                    print(" * ", end="")
            print()
        # Cần lệnh break để thoát chương trình, không cần nhập lại dữ liệu
        break
    except ValueError:
        print("Má nó nhập số thôi cũng sai hả thằng đầu buồi ?")
        continue

print("\n")
print("Một bài toán hay về hình VS-Studio")
print("-" * 35)

nhap_cao = None
while True:
    try:
        nhap_cao = int(input("Nhập vào chiều cao hình : "))
        for a in range(nhap_cao):
            for b in range(nhap_cao):
                # In ra cái đường chéo xuống và in ra cái đường ngang
                if a == b or a == len(range(nhap_cao)) // 2:
                    print(" * ", end="")
                # In ra cái đoạn * bên cột trái
                elif a in range(nhap_cao // 2) and b == 0:
                    print(" * ", end="")
                # In ra cái đoạn * bên cột phải
                elif a in range(nhap_cao // 2, nhap_cao) and b == nhap_cao - 1:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()
    except ValueError:
        print("Má nó nhập số thôi cũng sai hả thằng đầu buồi ?")
        continue
    else:
        break
