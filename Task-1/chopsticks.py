player1 = [1,1]
player2 = [1,1]
count = 0
def attack1(opponent1,opponent2,player1,player2):
    if opponent1 == 'L' and opponent2 == 'L':
        player2[0] += player1[0]
    else:
        player1[1] += player2[0]
    if opponent1 == 'R' and opponent2 == 'L':
        player2[0] += player1[1]
    else:
        player1[1] += player2[1]
        

def attack2(opponent1,opponent2,player1,player2):
    if opponent1 == 'L' and player1 != 0 and opponent2 == 'R':
        player2[1] += player1[0]
    else:
        player2[0] += player1[0]
    if opponent1 == 'R'and player1[1] != 0 and opponent2 == 'L':
        player2[0] += player1[1]
    else:
        player2[1] += player1[1]
    
    if player1[0] == 0 and player1[1] == 0:
        return
def split(player,x,y):
    if player[0]+player[1] == x+y:
        player[0] = x
        player[0] = y
    else:
        print("Invalid Move")
        
        
while(True):
    print("Enter Move For "+"Player"+str(count+1))
    move = input()
    if move =='A':
        Attack1,Attack2 = input("Enter Move Combination ").split()
        if player1[0]*player1[1]*player2[0]*player2[1] != 0:
            
            if count == 0:
                attack1(Attack1,Attack2,player1,player2)
            else:
                attack1(Attack1,Attack2,player2,player1)
        else:
            if count == 0:
                attack1(Attack1,Attack2,player1,player2)
            else:
                attack1(Attack1,Attack2,player2,player1)
    
    elif move == 'S':
        player,x,y = input("Enter the split combination ").split()
        if count == 0:
            split(player1,int(x),int(y))
        else:
            split(player2, int(x),int(y))
    
    if player1[0] >= 5:
        player1[0] = 0
    if player1[1] >= 5:
        player1[1] = 0
    if player2[0] >= 5:
        player2[0] = 0
    if player2[1] >= 5:
        player2[1] = 0
    print("Current Status")
    print("Player:1 " +str(player1), "Player:2 "+ str(player2))
    if player1[0]==0 and player1[1]==0:
        print("Player 2 won")
        break
    elif player2[0]==0 and player2[1]==0:
        print("Player 1 won")
        break
    count = 1-count
    
                
                  
    
        
        
    

        
