import random
def batDau():
    a = random.randrange(0, 50)
    i = 0
    # Muốn thay bao nhiêu lượt đoán thì thế vào biến luot_doan
    luot_doan = 5
    luot = 0
    while i < luot_doan:
        luot = luot_doan - i
        try:
            doan = int(input("Hãy nhập vào số bạn đoán : "))
            if doan == a:
                print("Bạn đã đoán đúng số {0} xin chúc mừng".format(doan))
                break
            else:
                print("Bạn đã đoán sai !")
                i += 1
                if doan < a:
                    print("Số {0} bạn đã đoán nhỏ hơn đáp án".format(doan))
                    if luot == 0:
                        print("Bạn đã hết lượt đoán")
                    else:
                        print("Bạn còn lại", luot, "đoán nữa !")
                        print("----------------------------------------")
                    continue
                else:
                    print("Số {0} bạn đã đoán lớn hơn đáp án".format(doan))
                    if luot == 0:
                        print("Bạn đã hết lượt đoán")
                    else:
                        print("Bạn còn lại", luot, "đoán nữa !")
                        print("----------------------------------------")
                    continue
        except ValueError:
            print("Chỉ cần nhập số thôi anh trai !")
            continue
    print("\nĐáp án là :", a,"\n")
    play_score(luot,luot_doan)

#----------------------------
def play_score(luot,luot_doan):
    diem_so = (luot*100)/luot_doan
    print("Điểm của bạn là :",round(diem_so),"%")

#----------------------------
def play_again():
    print("============================================")
    response = input("\nMuốn chơi lại không (C/K)?")
    response = response.upper()
    if response == "C":
        return True
    else:
        return False


batDau()

while play_again():
    batDau()
print("Bye, thank you !")