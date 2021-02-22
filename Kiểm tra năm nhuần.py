
while True:# Năm nhuần là năm chia hết cho 4 và không chia hết cho 100 hoawch chia hết cho 400
    year = int(input(" Nhập và năm để kiểm tra:="))
    if(( year % 4 == 0 and year % 100 !=0) and year % 400 ==0):
        print(year," Năm bạn nhập là năm nhuận")
    else:
        print(year,"Năm bạn vừa nhập không phải là năm nhuận đâu nhé")
    choice = input(" Nhap vao a/c")
    if choice =='a':
        break
