#Viet cuong trinh tinh cước taxi
# Km đâu là 5000
# 200 m tiep theo là 1000
#Neu lon hon 30km thi moi km se them 3000Đ
while True:
    km = int(input("nhap vao so km ma nguoi đi="))
    s1 = 5000

    if( km == 1):
        print(" sô tiền phải trả 1km là =",float(s1))
    elif( km >= 30):
        print("tong so tien >30km tiếp theo là=",float(s1 + 3000)*km)
    else:
        print("Số tiền phải trả cho đoạn đường đó la=", float(s1 + 1000)*km)
    hoi = input("bạn có muốn chạy lại không: ")
    if hoi is "a":
        break
print("Thôi nhé! Chúc bạn mạnh khỏe và bình an")
