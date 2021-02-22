#Tìm số lớn nhát trong mảng
a = []
max = 0
n = int(input(" Nhập vao n="))
for i in range(n):
    temp = int(input("mảng phần tử:" + str(i)))
    a.append(temp)
    if( a[i] > max):
        max = a[i]
print("\n\n\t\tMangr vừa nhạp là:=",a)
print("\nPhan tử lớn nhât trong mảng là:=", max)
