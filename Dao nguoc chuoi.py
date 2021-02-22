a = input(" nhap vao chuoi:")
print("chuoi duoc dao la:", a[:: -1])

#cách 2
b = input(" nhap vao ten bat ki:")
for i in range(1,len(b) + 1):
    print(b[-i], end=' ')
