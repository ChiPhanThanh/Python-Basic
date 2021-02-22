print('chao phan thahchi')

x = 9;
y= 6;
z = x + y
u = x *y
q = x - y
z = x + y;
print("\t\t hien thi nha cua no la:\n", z)

if( x < y):
       print("so do lon nhat la day")
    
else:
      print("chap phan thanh chi")
    
    
print("\t\t hien thi tong cua no la:", z);
print("\t\t hien thi nha cua no la:", u);
print("\t\t hien thi tong cua no la:", q);


#Dung vong lap for de 
A = [1.5, '2','5','chi']
for a in A:
  print("Xuat vi tri mang la",type(a), a);

#CHo mot chuoi trong python" PHan thanh chi"
for i in 'Phan Thanh Chi':
     print("chao ", i)

#
p = 'thien chua la tinh yeu'
for i  in p:
    print('\t\t\tXuat ra tung ki tu',i)


count = 1
while( count <10):
    print("%d nho hon",count);
    count  = count + 1;
  
 
for i in range(1,20):

    #pass: bo qua khoi lenh do
    if( i %2 ==0):
        pass
    elif( i %2 != 0):
        if( i ==5):
           break
        print("so le la", i,"chao")


#Xu li chuoi tron Python
str = 'phanthanhchi'
print ('Xuat ra ngoai:',str[0:9])
print ('\nXuat ra ngoai:',str[6: -1])
print ('\nXuat ra ngoai:',str[4: ])

# tinh do dai chuoi tren
print('Tra ve do dai cua chuoi:',len(str))
# Tim va thay the noi dung // find and replace content
str = "chao xuan"
newstr = str.replace("chao", "Dam")
print(newstr)

#tim vị trí chuỗi con , bắt đầu vi trí 0 và không tim ra thì trả về -1
str = "van anh" 
print (str.find("yuy"))

#Tách chuỗi
s =  'phan 34 thanhchi'
print('tach chuoi',s.split(" "))


#trim ki tu khoang trang
st = 'phANthnahchi'
print(st.upper()) #bien đổi thnahf chữ hoa
print(st.lower()) #bien doi thanh chu thường
print(st.isalnum()) # kiểm tra xâu có kí tự chữ hoặc số hay không
print(st.isalpha()) # kiem tra xem chuỗi có chứa toàn các ký tự rỗng không

#phương thưc Join nói các thnahf phần trong mảng thành một
list = ['chao', 'phan', 'thanh','chi']
print('--'. join(list))

print("\n\n\n ------------------Python About List--------------------------------")

#Bai tập về list 
chi  = ['chi','hoang','xuan','sang','tuan']
print(" Xuat mang:",chi)
print ('Lay ra phan tu mang:',chi[0]) # trich ra các phần tử mảng
print ('Lay ra phan tu mang:',chi[-3])
print('so luong cua mang', len(chi)) # Độ dài của danh sách, hoặc số lượng phần tử trong danh sách

#kiem tra phần tử có toond tại trong List không sue dung in và not in => trả về true và false
chi  = ['chi','hoang','xuan','sang','tuan']
print ('chi' in chi)

#Trích xuất mảng con
chi  = ['chi','hoang','xuan','sang','tuan']
print (chi [:2])

#xóa phần tử của mảng use " del"
chi  = ['chi','hoang','xuan','sang','tuan']
del chi[3]
print("hien thi danh sach sau khi xoa", chi)

#Nối hai mảng
a = ['chi', 'hoang','bang']
b = ['xuan','thuy','tuan']
c = a + b
print(" phep noi mang hien thi la:", c)

#Them phần tử vào mảng
chi  = ['chi','hoang','xuan','sang','tuan',]
new = chi.append('ha')
print (new)

numbers = [1, 2, 3]
numbers.append(4)
print (' Thm phan tu vào  mang',numbers)

#Lấy phần tử ở cuối mảng
chi  = ['chi','hoang','xuan','sang','tuan']
new = chi.pop()
print (new)

#Tìm một giá trị trong mảng
chi  = ['chi','hoang','xuan','sang','tuan']
print ("Tìm thấy trả về index", chi.index('hoang'))

#Đảo ngược giá trị của mảng
lst = [4, 5, 3, 7, 6, 1]
lst.reverse()
print('Mang dao nguoc',lst)
print("So lon nhat trong mang:",max(lst)) # tìm gia tri lon nhat trong mang

#Đếm số lần xuất hiện phan ftuwr trogn mang
lst = [4, 5, 4, 7, 6, 1]
print(' Sô lan xuat hieen cua 4 la:',lst.count(4))

#HAm sort để sắp xếp
lst = [4, 5, 4, 7, 6, 1]
lst.sort()
print("sap xep tang dan",lst)

lst.sort(reverse=True)
print(" Sap xep giam",lst)

print("Xuan a sao cho nhau trong khong gian thay đoi và thay thế cho nhau trong tịnh sao sao phai thay ")









  


