def numpat(n):
    for row in range(1,n+1):
        
        for col in range(1,row+1):    #why row+1 means the range function will exclude last value
            print(col,end=" ")
            
            
        print()
        
        
        
numpat(5)         #calling the function