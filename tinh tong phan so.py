#tinh tong sum1 = 1/1+ 1/2+ 1/3+ 1/4
print("==============sum1 = 1/1+ 1/2+ 1/3+ 1/4=====================")
v = int(input("nhap vao n="))
i = 1
sum = 0
for i in range (v):
    print('xuat hien chay',i)
    i = i+ 1
    sum = sum + 1/i
print("Tong la=",sum)

