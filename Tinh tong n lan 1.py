# tinh tong s  = 1 + 3 + 5 + 7.....(2*n + 1)
print("=============s  = 1 + 3 + 5 + 7.....(2*n + 1)======================")
n = int(input("nhap vao n="))
s = 0
count = 1
while(count <= 2*n + 1):
     print("Suat hien so lan la", count)
     count = count + 2;
     s = s + count
print("tong", s)


print("==================Dung vong lap for====================")
i = 1
sum = 0
for i in range (2*n+1):
    print('xuat hien chay',i)
    i = i+ 1
    sum = sum + i
print("Tong la=",sum)


