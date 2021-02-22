#SAU MOI LAN T6HI THI CAN THUC HIEN KIEM TRA DCHUWONG TRINH SAU DE KHAO KAHT CHUONG TRINH
print('================= KIEM TRA HOC LUC CUA HOC SINH===================');
diem = float(input("nhap vao diem cua hoc sinh="))
# kiem tra dieu kiemn d hoc sinh do dau hau trat hay thi lai chuing ta su dung if else
if(diem >=8):
    print(diem,"Hoc sinh do dat duoc hanh kiem tot va hoc sinh sinh gioi")
elif(diem == 7):
    print("\nHoc sinh do dat hanh kiem kha va hoxc sinh tien tien")
elif( diem <7 and diem >=5):
    print("\nHoc sinh do hanh kiem trung binh và khong co danh hieu")
elif(diem == 4 or diem == 3):
    print("\nPhu huynh nen xem lai cach hoc cua hoc sinh");
else:
    print("\nHoc sinh so thi lai hoăc nghi hoc")