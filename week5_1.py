class nisit :
    def __init__(self,name,year,dep,sex,fm):
        self.name = name
        self.year = year
        self.dep = dep
        self.sex = sex
        self.fm = fm

    def showdata(self):
        print('-'*10,'แนะนำตัว','-'*10)
        if self.sex=='ชาย':
            print('สวัสดีครับ ผมชื่อ ',self.name,'นักศึกษาชั้นปีที่ ',self.year,'สาขา ',self.dep,'เพศ ',self.sex,'มาจากจังหวัด ',self.fm)
        elif self.sex=='หญิง':
            print('สวัสดีค่ะ ฉันชื่อ ',self.name,'นักศึกษาชั้นปีที่ ',self.year,'สาขา ',self.dep,'เพศ ',self.sex,'มาจากจังหวัด ',self.fm)
x = nisit(name=input('ชื่อ'),year=input('ชั้นปี'),dep=input('สาขา'),sex=input('เพศ'),fm=input('จังหวัด'))
x.showdata()