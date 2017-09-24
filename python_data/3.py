import math
a=0
b=1
L=[]
def sushu(b):
    for x in range(1,int(math.sqrt(b)+1)):
        if x!=1 and b%x==0:
            return False
    return True
while True:
    if(a==5):
        break
    if sushu(b):
        c=2**b-1
        if sushu(c) and b!=c:
            L.append(c)
            a=a+1
    b=b+1
print (L)