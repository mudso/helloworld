#类的对象实例化立即运行
class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print('hello ,my name is',self.name)

p = Person('mudso')
p.say_hi()

