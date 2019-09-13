def diamond():
    n=3
    for i in range(1,n+1):
        c=0
        for j in range(i,n):
            c+=1

        print " "*c,
        print "*"*(2*i-1)


    for i in range(n-1,0,-1):
        c=0
        for j in range(n,i,-1):
            c+=1

        print " "*c,
        print "*"*(2*i-1)
