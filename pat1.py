def pat1(n):
    for row in range(0,2*n):
        totalcol=2*n-row if row>n else row     #this condition is for when the row is greater than n """
                                               #else the nof rows equal to col no of of stars will be printed"""
        for col in range(totalcol):
            print("*",end="")
            
        print()
        
        
        
pat1(5)