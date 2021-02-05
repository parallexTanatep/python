dic=[]
trn=[]
vb=[]
k=1
def menu():
    global choice
    print('\nพจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n 3) ลบคำศัพท์\n4) ออกจากโปรแกรม')
    choice = input('Input Choice')

def dictinary():
    dic.insert(0,input('เพิ่มคำศัพท์'))
    trn.insert(0,input('ชนิดคำศัพท์(n. ,v. ,adj. ,adv. :)'))
    vb.insert(0,input('ความหมาย'))
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')

def show():
    print('-'*10,'\nคำศัพท์มีทั้งหมด \n',len(dic),'-'*10)
    x=0
    while x < len(dic) :
        print(dic[x],' ',trn[x],' ',vb[x])
        x+=1

def ex():
    y=str(input('พิมพ์คำศัพท์ที่ต้องการลบ: '))
    v=str(input('ลบ'+y+'ใช่หรือไม่ (y/n) :'))
    if v=='y':
        a=0
        while a < len(dic) :
            if y==dic[a]:
                del trn[a]
                del vb[a]
            a+=1
        dic.remove(y)
        print('ลบ'+y+'เรียบร้อยแล้ว')
    else:
        print('ยกเลิกการลบ')
    
while True:
    menu()
    if choice =='1':
        dictinary()
    elif choice=='2':
        show()
    elif choice=='3':
        ex()
    else:
        l = str(input('ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) :'))
        if l=='y':
            print('ออกจากโปรแกรมเรียบร้อยแล้ว')
            break
        else:
            print('กลับเข้าสู่โปรแกรม')
            continue