print("""Bài tập nhập mỗi chuỗi bất kỳ, sau đó in ra số nguyên âm 
           phát hiện được trong chuỗi đó""")
print("-" * 55)
def NegativeNumberInString(your_str):
    negatives=[]
    i=0
    while i+1<len(your_str):
        if your_str[i]=='-' and your_str[i+1].isnumeric():
            negative=''
            while i+1<len(your_str) and your_str[i+1].isnumeric():
                negative+=your_str[i+1]
                i+=1
            else:
                negatives+=[-int(negative)]
        i+=1
    return negatives

while True:
     try:
          a = input("Nhập vào chuỗi bất kỳ có số âm : ")
          print(NegativeNumberInString(a))
     except ValueError:
          print("Nhập lại đi !")
          continue