def numpat5(n):
    
    for row in range(1,2*n+1):
        
        c=2*n-row if row>n else row
        for spaces in range(0,n-c):
            print(end=" ")
            
        for col in range(c,0,-1):
            
            print(col,end="")
            
                
        for col in range(2,c+1):
                    
            print(col,end="")
                    
                    
        print()
        
        
numpat5(4)