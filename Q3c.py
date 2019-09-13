def diamond(n,c):
    p=n/2+1
    for i in range(1,p+1):
        for j in range(i,p):
            print " ",

        for k in range(1,2*i):
            print c,

        print "\n"

    for i in range(p-1,0,-1):
        for j in range(p,i,-1):
            print " ",

        for k in range(1,2*i):
            print c,

        print "\n"

diamond()        
