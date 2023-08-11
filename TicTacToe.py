def board(play):
    print(" %c | %c | %c " % (play[1],play[2],play[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (play[4],play[5],play[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (play[7],play[8],play[9]))    
    print("   |   |   ")    

def insertPos(play,symbol):
      print('\n\n--USER1 TURN--\n\nplease enter position number to place X:')
      position=input()

      if 1 <= int(position) <= 9 and play[int(position)] == ' ':
          play[int(position)] = symbol


      
print("----Welcome to TicTacToe----")
play=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
symbol1='x'
symbol2='o'

        
while 1:
    while 1:
        insertPos(play,symbol1)
        board(play)
        break
    
    if (play[1] == 'x' and play[2] == 'x' and play[3] == 'x' or
    play[4] == 'x' and play[5] == 'x' and play[6] == 'x' or
    play[7] == 'x' and play[8] == 'x' and play[9] == 'x' or
    play[1] == 'x' and play[5] == 'x' and play[9] == 'x' or
    play[3] == 'x' and play[5] == 'x' and play[7] == 'x' or
    play[2] == 'x' and play[5] == 'x' and play[8] == 'x' or
    play[3] == 'x' and play[6] == 'x' and play[9] == 'x' or
    play[1] == 'x' and play[4] == 'x' and play[7] == 'x'
):
      print("\n\n---USER 1 WON---\n\n")
      break
    
     
    while 1:
        print('\n\n--USER2 TURN--\n\nplease enter position number to place o:')
        position=input()
        if 1 <= int(position) <= 9 and play[int(position)] == ' ':
          play[int(position)] = symbol2
          board(play)
        
        break
    if (play[1] == 'x' and play[2] == 'x' and play[3] == 'x' or
    play[4] == 'x' and play[5] == 'x' and play[6] == 'x' or
    play[7] == 'x' and play[8] == 'x' and play[9] == 'x' or
    play[1] == 'x' and play[5] == 'x' and play[9] == 'x' or
    play[3] == 'x' and play[5] == 'x' and play[7] == 'x' or
    play[2] == 'x' and play[5] == 'x' and play[8] == 'x' or
    play[3] == 'x' and play[6] == 'x' and play[9] == 'x' or
    play[1] == 'x' and play[4] == 'x' and play[7] == 'x'
):
      print("\n\n---USER 2 WON---\n\n")
      break 




    
    






    
    