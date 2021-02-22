
a = []
n = int(input(" Nhập vao n="))
for i in range(n):
    temp = int(input("mảng phần tử:" + str(i+1)))
    a.append(temp)
print("\n\t\tMang vừa nhạp là:=",a)
 
for i in range (n):
    for j in range(i):
        if( a[i] < a[j]):
                tem = a[i]
                a[i] = a[j]
                a[j] = tem
print("Mảng sau khi nhap và sap xếp là be -> lon:",a)

for i in range (n):
    for j in range(i):
        if( a[i] > a[j]):
            tem = a[i]
            a[i] = a[j]
            a[j] = tem
print("Mảng sau khi nhap và sap xếp lon -> bé là:",a)

