t = int(input("Nhập vào số giây:="))
giờ = (t // 3600) % 24
phút  =  ( t % 3600) // 60
giay = (t % 3600)%60   # ta chia lấy nguyên cho 3600 sau đó chia 60 giây để lấy số giây
print("Số gờ hiện tại la:", giờ,":",phút,":",giay)
