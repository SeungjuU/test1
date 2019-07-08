try:
    num=int(input('Enter: '))
    res=10/num
    print (res)
except ZeroDivisionError:
    print ('Enter except zero!')
except ValueError:
    print ('Enter a number!')
