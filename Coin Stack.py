# I have put the whole project in solve(grid) function
# I do have the sample example at last 


def solve(grid):
    row=len(grid)
    col=len(grid[0])
    total_coin = 0
    # I am dividing the project by doing the rows first and then columns


    for i in range(row):                # what it will do is will go through each rows and will detact the max number then according it will-
        max=0                           # -add the coins and again check the row that it is hill from both side 
        for j in range(col):
            if max<=grid[i][j]:
                max=grid[i][j]
                t1=i
                t2=j
        
        temp=grid[t1][t2]

        for j in range(t2-1,-1,-1):
            
            while grid[i][j]>temp:
                total_coin += 1
                grid[i][j+1]=grid[i][j+1]+1
                temp=grid[i][j+1]
            else:
                temp=grid[i][j]
    
        for j in range(1,t2,1):
            while grid[i][j]<temp:
                total_coin += 1
                grid[i][j]=grid[i][j]+1
        
            else:
                temp=grid[i][j]


        temp=grid[t1][t2]

        if(col>1):  
            
            for j in range(t2+1,col,1):

                while grid[i][j]>temp:
                    total_coin += 1
                    grid[i][j-1]=grid[i][j-1]+1
                    temp=grid[i][j-1]

                else:
                    temp=grid[i][j]
            
            for j in range(col-1,t2,-1):

                while grid[i][j]<temp:
                    total_coin += 1
                    grid[i][j]=grid[i][j]+1
                       
                else:
                    temp=grid[i][j]
    
#loop for arranging descending order in column       
    for j in range(col):        # here it will do the same thing as rows as will loop through each colums and will see the max nmber then follows the rules accordingly.

        max=0
        for i in range(row):
            
            if max<=grid[i][j]:
                max=grid[i][j]
                t1=i
                t2=j
        
        temp=grid[t1][t2]

        for i in range(t1-1,-1,-1):
            
            while grid[i][j]>temp:
                total_coin += 1
                grid[i+1][j]=grid[i+1][j]+1
                temp=grid[i+1][j]

            else:
                temp=grid[i][j]

        for i in range(1,t1,1):
        
            while grid[i][j]<temp:
                total_coin += 1
                grid[i][j]=grid[i][j]+1

            else:
                temp=grid[i][j]

        temp=grid[t1][t2]
        
        if(row>1):  
            
            for i in range(t1+1,row,1):
    
                while grid[i][j]>temp:
                    total_coin += 1
                    grid[i-1][j]=grid[i-1][j]+1
                    temp=grid[i-1][j]
                    
                else:
                    temp=grid[i][j]
            
            for i in range(row-1,t1,-1):

                while grid[i][j]<temp:
                    total_coin += 1
                    grid[i][j]=grid[i][j]+1
                      
                else:
                    temp=grid[i][j]
        for i in range(row):

                max=0
                for j in range(col):
                    
                    if max<=grid[i][j]:
                        max=grid[i][j]
                        t1=i
                        t2=j
                
                temp=grid[t1][t2]

                for j in range(t2-1,-1,-1):
                    
                    while grid[i][j]>temp:
                        total_coin += 1
                        grid[i][j+1]=grid[i][j+1]+1
                        temp=grid[i][j+1]

                    else:
                        temp=grid[i][j]
            
                for j in range(1,t2,1):
                
                    while grid[i][j]<temp:
                        total_coin += 1
                        grid[i][j]=grid[i][j]+1
                
                    else:
                        temp=grid[i][j]


                temp=grid[t1][t2]

                if(col>1):  
                    
                    for j in range(t2+1,col,1):

                        while grid[i][j]>temp:
                            total_coin += 1
                            grid[i][j-1]=grid[i][j-1]+1
                            temp=grid[i][j-1]

                        else:
                            temp=grid[i][j]
                    
                    for j in range(col-1,t2,-1):

                        while grid[i][j]<temp:
                            total_coin += 1
                            grid[i][j]=grid[i][j]+1
                           
                        else:
                            temp=grid[i][j]

    return total_coin  #will return th total number of coins that was needed to make king/Queen hill. 


#sample example 

ex1 = [[2,3,1,5,4],[1,3,5,2,4],[5,2,1,3,4],[4,2,3,1,5],[1,3,5,4,2]]

a = solve(ex1)
print("Total coins are", a, ".")


    
