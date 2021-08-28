print("Dinh Quy Pham")
print("Một bài toán hay về tam giác vuông cân góc phải dưới")
print("-"*35)

nhap_cao = None
while True :
    try:
        nhap_cao = int(input("Nhập vào chiều cao tam giác : "))
        for a in range(nhap_cao):
            for b in range(nhap_cao):
                # Chỗ này là bài toán hơi ngược, vẽ ra giấy sẽ thấy
                if b < (nhap_cao - 1) - a:
                    print("   ",end="")
                else:
                    print(" * ",end="")
            print()
        # Cần lệnh break để thoát chương trình, không cần nhập lại dữ liệu
        break
    except ValueError:
        print("Má nó nhập số thôi cũng sai hả thằng đầu buồi ?")
        continue



