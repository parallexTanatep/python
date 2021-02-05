import time
name=[]
hit=[]
score=[]
tim=[]
def datetime():
    timelo=time.localtime()
    t=time.strftime('%d %B %Y, %H:%M:%S',timelo)
    print(t)
people=int(input('Enter amount :'))
for x in range (people):
    print('Enter data',1+x)
    n=input('Name :')
    sco=float(input('Score :'))
    ti=float(input('Timeleft :'))
    name.append(n)
    score.append(sco)
    tim.append(ti)
    hit.append(sco/ti)
for x in range(people):
    z=x
    for z in range(people):
        if hit[x]>hit[z]:
            a,b,c,d = hit[x],name[x],score[x],tim[x]
            hit[x],name[x],score[x],tim[x],=hit[z],name[z],score[z],tim[z]
            hit[z],name[z],score[z],tim[z],=a,b,c,d
timelo = time.localtime()
a=time.strftime('%A',timelo)
b=time.strftime('%Y',timelo)
print('Shotgun'+a+'Training'+b+'\nCondtion : 1')
datetime()
print('-'*75)
print('{0: <10}{1:<10}{2: <10}{3: <18}{4: <15}{5: <15}{6: <10}'.format('NO.','PTS','TIME','COMPETITOR# Name','HIT FACTOR','STATE POINTS'))
print('-'*75)
for x in range(people):
    target_1=(hit[x]/hit[0])*50
    target_2=(target_1/(hit[0]/hit[0]*50))*100
    print('{0: <10}{1: <10}{2: <10}{3: <18}{4: <15}{5: <15}{6: <10}'.format(x+1,int(score[x],int(tim[x],name[x],'%.4f'%hit[x],'%.4f'%target_1,'%.2f'%target_2))))