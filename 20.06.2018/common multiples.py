n1=12
n2=18
cf={i for i in range(1,min(n1+1,n2+1))
    if n1%i==0 and n2%i==0}
print(cf) #{1, 2, 3, 6}
