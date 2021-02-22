a = []
n = int(input(" Nhập vao n="))
for i in range(n):
    temp = int(input("mảng phần tử:" + str(i+1)))
    a.append(temp)
print("\n\t\tMang vừa nhạp là:=",a)

for i  in range(n - 1):
    if (a[i] % 2 ==0):
      a[i] = a[i + 1]
print("mang da xoa phan tu lẻ  la",a)