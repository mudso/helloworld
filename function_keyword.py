#关键字参数
def func(a,b=1,c=3):
    print(a,'is a','and b is',b,'and c is',c)

func(2)

func(2,3)
func(c=9,b=7,a=5)
func(25,c=24)