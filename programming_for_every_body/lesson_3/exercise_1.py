eh = input('Enter Hours:')
er = input('Enter Rate:')
try:
    eh = float(eh)
    er = float(er)
    if eh > 40 :
        pay = 40 * er + 1.5 * (eh - 40)*er
    else:
        pay = eh * er
    print('pay:',pay)
except:
    print('please enter a number')