#Tìm số lớn nhát trong mảng
a = []
n = int(input(" Nhập vao n="))
for i in range(n):
    temp = int(input("mảng phần tử:" + str(i+1)))
    a.append(temp)
print("\n\t\tMang vừa nhạp là:=",a)
 
min = a[0]
for i in range (n):
    if( a[i] < min):
        min = a[i]
print(min)
