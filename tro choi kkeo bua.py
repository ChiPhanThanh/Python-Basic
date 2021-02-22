print(" -=================Mo  phong tro choi Kéo Búa=========================")
#thanh phan nhap vao đó là 0 , 2 , 5

taytrai = int(input(" Tay trai gio="))
tayphai = int(input(" Tay phai gio="))

if(taytrai == 0 and tayphai == 2):
    print("tay phai thang")
elif( taytrai ==2 and tayphai == 5):
    print("tay phai thang")
elif( taytrai ==5 and tayphai == 2):
    print("tay trai  thang")
elif(taytrai ==0 and tayphai == 5):
    print("tay phai thang")
else:
    print("ca hai tay ot lai")


