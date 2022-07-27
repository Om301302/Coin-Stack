def solve(grid):
    row=len(grid)
    col=len(grid[0])
    total_coin = 0

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
    
#loop for arranging descending order in column       
    for j in range(col):

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

    return total_coin
        
    
