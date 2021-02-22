#Tinh tong s = 1 -2 + 3 - 4.....n
print("===============s = 1 -2 + 3 - 4.....n====================")
n1 = int(input("nhap vao n1="))
i = 1
d = 1
sum1  = 0
for  i in range (n1):
    print('Thu tu so=', i)
    i =i+1
    sum1 +=  d*i # tinh tong va gan gia tri d ban đầu vs i chạy 
    d *= -1  # Gan d = d* -1 để vòng chạy thứ 2 sẽ gan lên gia tri tong
print("Tong cua day so la", sum1)
