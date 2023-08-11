
print("----Welcome to TicTacToe----")
play=['0','1','2','3','4','5','6','7','8']
symbol1='x'
symbol2='o'

while 1:
    while 1:
        print('\n\n--USER1 TURN--\n\nplease enter position number to place X:')
        position=input()
        for i in play:
            if(position==i):
                play[int(position)]=symbol1
        for i in range(0,3):
         print(play[i],end='  ')
        print("\n")
        for i in range(3,6):
            print(play[i],end='  ')
        print("\n")
        
        for i in range(6,9):
         print(play[i],end='  ')


        break
    if(play[0]=='x' and play[1]=='x' and play[2]=='x' or play[3]=='x' and play[4]=='x' and play[5]=='x' 
     or play[6]=='x' and play[7]=='x' and play[8]=='x' or play[0]=='x' and play[4]=='x' and play[8]=='x'
     or play[2]=='x' and play[4]=='x' and play[6]=='x' or play[1]=='x' and play[4]=='x' and play[7]=='x'
       or play[2]=='x' and play[5]=='x' and play[8]=='x' or play[0]=='x' and play[3]=='x' and play[6]=='x'
     ):
      print("\n\n---USER 1 WON---\n\n")
      break
    
     
    while 1:
        print('\n\n--USER2 TURN--\n\nplease enter position number to place o:')
        position=input()
        for i in play:
          if(position==i):
                play[int(position)]=symbol2
        for i in range(0,3):
         print(play[i],end='  ')
        print("\n")
        for i in range(3,6):
            print(play[i],end='  ')
        print("\n")
        
        for i in range(6,9):
         print(play[i],end='  ')

        break
    if(play[0]=='o' and play[1]=='o' and play[2]=='o' or play[3]=='o' and play[4]=='o' and play[5]=='o' 
     or play[6]=='o' and play[7]=='o' and play[8]=='o' or play[0]=='o' and play[4]=='o' and play[8]=='o'
     or play[2]=='o' and play[4]=='o' and play[6]=='o' or play[1]=='o' and play[4]=='o' and play[7]=='o'
       or play[2]=='o' and play[5]=='o' and play[8]=='o' or play[0]=='o' and play[3]=='o' and play[6]=='o' 
     ):
      print("\n\n---USER 2 WON---\n\n")
      break 




    
    






    
    