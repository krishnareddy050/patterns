def numpat5(n):
    
    for row in range(1,n+1):
        for spaces in range(0,n-row):
            print(end=" ")
            
        for col in range(row,0,-1):
            
            print(col,end="")
            
                
        for col in range(2,row+1):
                    
            print(col,end="")
                    
                    
        print()
        
        
numpat5(5)
    
    