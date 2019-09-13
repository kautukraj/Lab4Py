def diamond():
    n=3
    for i in range(1,n+1):
        for j in range(i,n):
            print " ",

        for k in range(1,2*i):
            print "*",

        print "\n"

    for i in range(n-1,0,-1):
        for j in range(n,i,-1):
            print " ",

        for k in range(1,2*i):
            print "*",

        print "\n"        
