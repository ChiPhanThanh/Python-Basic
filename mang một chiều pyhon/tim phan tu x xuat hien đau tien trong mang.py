
#Viết hàm tìm phần tử có giá trị x xuất hiện đàu tiên trong mảng
a = []
n = int(input(" Nhap vao phan tu mang"))

def timphantu(a, n, x):
    for i in range (n):     #Duyệt i chạy trong mảng
      if( x == a[i]):        # Gặp điều kiện và kiểm tra nó
        return i            # nếu đúng thì trả lại giá trị đúng đó và xuất tìm được
    return -1               #không tìm thấy giá trị vị trí đầu cua
  

for i in range(n):
    temp = int(input("xuât phan tu" + str(i)))
    a.append(temp)
print("Xuat mảng vừa nhap", a)
x  =int(input("Nhap vao giá trị x="))
print(" Phần tử xuất hiện ở cuối ",timphantu(a, n, x))



