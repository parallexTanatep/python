print('ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม')
i=0
foodlist=[]
while(True):
    i+=1
    f=input('อาหารโปรดอันดับที่ {} : '.format(i))
    foodlist.append(f)
    if f=='exit':
        break
print('อาหารโปรดของคุณมีดังนี้ : ')
for n in range(1,i) :
    print(n,'.',foodlist[n-1],end='')
