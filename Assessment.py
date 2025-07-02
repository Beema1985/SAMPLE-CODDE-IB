d={}
print('Welcome to bonus generator!\nEnter the number of employees below.')
z=int(input('Number of employees:  '))

for i in range(z):
    a=float(input('Enter their sales amount:   '))
    if a>=500000:
        print('Bonus amount for this sale is:' , a/5)
        c=a/5
    elif a<500000 and a>=100000:
        print('Bonus amount for this sale is:  ', a*15/100)
        c=a*15/100
    elif a<100000 and a>=75000:
        print('Bonus amount for this sale is:  ', a/10)
        c=a/10
    elif a<75000 and a>=50000:
        print('Bonus amount for this sale is:  ', a/20)
        c=a/20
    else : print('No bonus')
    d[a]=c

avgcomm=c/z
print('Average commision:',round(avgcomm,2))
    

 


##b=float(input('Enter your second sales amount:  '))
##nxt=
##if b>=500000:
##    print('Your bonus amount for this sale is:' , b/5)
##elif b<500000 and b>=100000:
##    print('Your bonus amount for this sale is:  ', b*15/100)
##elif b<100000 and b>=75000:
##    print('Your bonus amount for this sale is:  ', b/10)
##elif b<75000 and b>=50000:
##    print('Your bonus amount for this sale is:  ', b/20)
##elif
##else : print('Sorry no bonus')









