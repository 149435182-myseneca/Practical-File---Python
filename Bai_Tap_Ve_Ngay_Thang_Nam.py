chao_mung = ("Chương trình ngày tháng năm của Phạm Đình Quý")
print(chao_mung.center(50))
print("----------------------------------------------------")

lst1 = [1,3,5,7,8,10]
lst2 = [4,6,9,11]
dict = {1:"Tháng một", 2:"Tháng hai", 3:"Tháng ba", 4:"Tháng tư",
        5:"Tháng năm", 6:"Tháng sáu", 7:"Tháng bảy", 8:"Tháng tám",
        9:"Tháng chín", 10:"Tháng mười", 11:"Tháng mười một", 12:"Tháng mười hai"}
while True:
    try:
        nhap_ngay  = int(input("Hãy nhập vào ngày : "))
        nhap_thang = int(input("Hãy nhập vào tháng : "))
        nhap_nam   = int(input("Hãy nhập vào năm : "))
        if nhap_thang in lst1:
            if nhap_ngay == 31:
                nhap_ngay  = 1
                nhap_thang += 1
                print("Ngày tiếp theo sẽ là", str(nhap_ngay),dict[nhap_thang],nhap_nam)
            elif 0 < nhap_ngay < 31:
                nhap_ngay += 1
                print("Ngày tiếp theo sẽ là", str(nhap_ngay), dict[nhap_thang], nhap_nam)
            else:
                print("Làm gì có ngày đó cha nội !")
                continue

        elif nhap_thang in lst2:
            if nhap_ngay == 30:
                nhap_ngay = 1
                nhap_thang += 1
                print("Ngày tiếp theo sẽ là", str(nhap_ngay), dict[nhap_thang], nhap_nam)
            elif 0 < nhap_ngay < 30:
                nhap_ngay += 1
                print("Ngày tiếp theo sẽ là", str(nhap_ngay), dict[nhap_thang], nhap_nam)
            else:
                print("Làm gì có ngày đó cha nội !")
                continue

        elif nhap_thang == 2:
            if (nhap_nam % 4 == 0) and (nhap_nam % 100 != 0):
                if nhap_ngay == 29:
                    nhap_ngay = 1
                    nhap_thang = 3
                    print("Ngày tiếp theo sẽ là", str(nhap_ngay), dict[nhap_thang], nhap_nam)
                elif 0 < nhap_ngay < 29:
                    nhap_ngay += 1
                    print("Ngày tiếp theo sẽ là", str(nhap_ngay), dict[nhap_thang], nhap_nam)
                else:
                    print("Làm gì có ngày đó cha nội !")
                    continue
            else:
                if nhap_ngay == 28:
                    nhap_ngay  = 1
                    nhap_thang = 3
                    print("Ngày tiếp theo sẽ là", str(nhap_ngay), dict[nhap_thang], nhap_nam)
                elif 0 < nhap_ngay < 28:
                    nhap_ngay += 1
                    print("Ngày tiếp theo sẽ là", str(nhap_ngay), dict[nhap_thang], nhap_nam)
                else:
                    print("Làm gì có ngày đó cha nội !")
                    continue

        elif nhap_thang == 12:
            if nhap_ngay == 31:
                nhap_ngay  = 1
                nhap_thang = 1
                nhap_nam  += 1
                print("Ngày tiếp theo sẽ là", str(nhap_ngay), dict[nhap_thang], nhap_nam)
            elif 0 < nhap_ngay < 31:
                nhap_ngay += 1
                print("Ngày tiếp theo sẽ là", str(nhap_ngay), dict[nhap_thang], nhap_nam)
            else:
                print("Làm gì có ngày đó cha nội !")
                continue
        else:
            print("Làm gì có tháng "+str(nhap_thang),"cha nội !")
            continue
    except ValueError:
        print("Nhập cái ngày tháng cũng đéo nổi. Lại đi mày !")
        continue
    else:
        break
