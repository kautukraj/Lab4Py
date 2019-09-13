def ndiamond():
    num=5/2+1
    for i in range(1,num+1):
        for j in range(num-i,0,-1):
            print " ",
        for k in range (1,i+1):
            print k,
        for k in range(i-1,0,-1):
            print k,
        print '\n'
        
    for i in range(1,num+1):
        for j in range(i,0,-1):
            print " ",
        for k in range(1,num-i+1):
            print k,
        for k in range(num-i-1,0,-1):
            print k,

        print '\n'      
