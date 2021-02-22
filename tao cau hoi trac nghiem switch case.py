
print("==============Chuong trinh cau hoi trac nghiem===================")

def switch_funcion(choice):
  chi = {
    1: "Ban tra loi đung",
    2: "ban tra loi sai",
    }
  return chi.get(choice,"Moi ban chon lai")
print (switch_funcion(1))


print("===========cAU HOI TRAC NGHIE=======")
print("==Chua Gie su sinh ra o dau=====")
print("cau1: Nazzaret\n")
print("cau2: Campiuchi\n")
print("cau3: Thailan\n")
print("cau4: American\n")


a = int(input("Moi ban chon cau hoi="))
def switch(a):
    return{
            1:"Hoan ho ban, Ban da dung",
            2:"Cau vua roi ban nhap sai",
            3:" Sai luon",
            4:"Xem lai nao",
        }.get(a,"moi chon lai")
print(switch(a))



