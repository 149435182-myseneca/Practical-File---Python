# Dinh Quy Pham
# -*- coding: utf-8 -*-
print("Chương trình nhập vào một số tự nhiên có hai chữ số, và in ra cách đếm chữ số đó")
print("--------------------------------------------------------------------------------")

dic1 = {1: "Mười", 2: "Hai mươi", 3: "Ba mươi",
        4: "Bốn mươi", 5: "Năm mươi", 6: "Sáu mươi",
        7: "Bảy mươi", 8: "Tám mươi", 9: "Chín mươi"}
dic2 = {1:"mốt", 2:"hai", 3:"ba",
        4:"bốn", 5:"lăm", 6:"sáu",
        7:"bảy", 8:"tám", 9:"chín"}

# Mở vòng lặp While để lặp lại hành động nếu nhập sai dữ liệu
while True:
     try:
          so = int(input("Nhập vào số N có hai chữ số : "))
          # Gán a là kết quả hàng chục
          a = so // 10
          # Gán b là kết quả hàng đơn vị
          b = so % 10
          if 9 < int(so) < 100:
               if b == 0:
                    print(dic1[a])
               elif (b != 0) and (int(so) == 11):
                    print("Mười một")
               else:
                    print(dic1[a], dic2[b])
          else:
               print("Số N phải lớn hơn 9 và bé hơn 100. Hãy nhập lại !")
               # Câu lệnh continue để lặp lại vòng lặp, buộc người dùng phải nhập đúng dữ liệu
               continue
     except ValueError:
          print("Mày có biết viết chữ số không thằng ngu ?")
          continue
     else:
          break




