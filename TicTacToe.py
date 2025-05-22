l = list([
    [" "," "," "],
     [" "," "," "],
     [" "," "," "]
    ])

option = list([1,2,3,4,5,6,7,8,9])
print(option)
count = 0 
while(count<9):
    
    print(option)
    x = int(input("choose "))
    if x in(option):
        option.remove(x)
        num = 1

        
        
        for i in range(3):
            for j in range(3):
                if(num==x and count%2==0):
                    l[i][j] = 'O'
                elif (num==x ):
                     l[i][j] = 'X'
                num+=1
        count+=1
        
        for i in range(3):
            print("_"*22)
            for j in range(3):
                print(f"|  {l[i][j]}  ", end = " ")
            print("|")
        win =  [
            [l[0][0],l[1][1],l[2][2]],
            [l[0][2],l[1][1] ,l[2][0]],
            [l[0][0],l[0][1] ,l[0][2]],
            [l[1][0],l[1][1] ,l[1][2]],
            [l[2][0],l[2][1] ,l[2][2]],
            [l[0][1],l[1][1] ,l[2][1]],
            [l[0][2],l[1][2] ,l[2][2]],
            [l[0][0],l[1][0] ,l[2][0]] 
        ]
        
        found = False
        for lin in win:
            
            if lin[0]==lin[1]==lin[2] and lin[0]!=' ':
                if lin[0]=='O':
                    print("Player 1 win")
                else:
                    print("Player 2 win")
                found =True
        if found:
            break
        
    else:
        print("chose from option")
    
   


