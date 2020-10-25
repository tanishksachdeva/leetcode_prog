n=121
rev = 0
while(n > 0):  
    r = n %10    
    print(r)
    print(rev, 'rev')
    rev = (rev *10) + r
    n = n //10
    print(n)
print(rev)
