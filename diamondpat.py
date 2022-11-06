def pat1(n):
    for row in range(0,2*n):
        totalcol=2*n-row if row>n else row     
        noOfSpaces=n-totalcol                   #when the no.of spaces in row1 is totalcol-n this will tell you how many spaces is to leave
        for i in range(noOfSpaces):
            print(end=" ")                  
        for col in range(totalcol):
            print("*",end=" ")
            
        print()
        
        
        
pat1(5)