# coding=UTF-8
class SchoolMember:
    '''代表学校里所有成员'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('initialized schoolmember : {}'.format(self.name))

    def tell(self):
        '''告诉我所有细节'''
        print('name : {}.age : ()'.format(self.name,self.age,end=' '))

class Teacher:
    '''代表一位老师'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('initialized teacher : {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))
class Student(SchoolMember):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# 打印一行空白行
print()
members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()
