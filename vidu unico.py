#'''viet chương trin in ra hình chữ nhật có ích thước m x n'''

# m: chieu ngang - n la chieu doc

#In ra tam giac
n= int(input("nhap vao n="))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end = "")
    print()

 #in ra hinh chu nhât
n1= int(input("nhap vao n1="))
m= int(input("nhap vao m="))
for e in range( n1):
    for r in range(m):
         e = e+1
         r = r+1
         print("*", end ="")
    print()

      

