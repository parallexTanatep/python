stlist=[0,0,0,0,0,0]
scorelist=['90-100 :','80-89  :','70-79  :','60-69  :','50-59  :','0-49   :']
s=int(input('ป้อนจำนวนนักเรียน :'))
k=1
while(k<=s):
    sc=int(input('คะแนนคนที่ '+ str(k) +' ได้ :'))
    stlist.append(sc)
    k+=1
    if sc<=100 and sc>=90:
        stlist[0]+=1
    elif sc<=90 and sc>=80:
        stlist[1]+=1
    elif sc<=80 and sc>=70:
        stlist[2]+=1
    elif sc<=70 and sc>=60:
        stlist[3]+=1
    elif sc<=60 and sc>=50:
        stlist[4]+=1
    elif sc<=50 and sc>=0:
        stlist[5]+=1
for x in range(0,6):
    print(scorelist[x],'*'*stlist[x])
