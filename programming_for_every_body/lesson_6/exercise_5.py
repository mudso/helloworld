str = 'X-DSPAM-Confidence:0.8475'
a = str.find(':')
print(a)
b = str[a+1:-1]
c = float(b)
print(c)