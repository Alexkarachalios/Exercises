l=[]
a=[1,2,3,4,5,6,7,8,9,11,12,15,24,36]
for num in range(1,1000):
    ath=0
    p=(num/100)
    p1=(num%100)
    p2=(p1/10)
    p3=(p1%10)
    ath=(p+p2+p3)
    gin=(p*p2*p3)
    if (num%ath)==0:
        l.append(num)
    if gin!=0:
        if (num%gin)==0:
           a.append(num)
l.append(1000)
print "Harshad numbers from 1-1000 : ",l
print "Other numbers: ",a


#written with python 2.7
