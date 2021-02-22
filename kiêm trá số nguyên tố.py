# Số nguyên tố ladf số ,à chia hết cho chính nó và chia hết cho 1
# Để kiểm tra chúng ta chung ta dùng một biến đếm
while True:
    n = int(input(" Nhập vào n="))
    dem = 0
    for i in range(1,n+1):
        if( n% i == 0):
            dem  = dem + 1
    if ( dem == 2): #đây chỉ là chỉ hai ước số 1 và chính nó để kiểm tra
        print(n,"Số đó là số nguyên tố")
    else:
        print(n,"Số đó không phải là số nguyên tố")
    hoi = input("Có muốn tiếp tục không(c/k)")
    if hoi is "k":
        break
print("Tạm Biệt")
