from __future__ import print_function

class Connect4:
    def __init__(self, row = 6, column = 7):
      self.row = row 
      self.column = column 
      self.moves_left = row * column
      self.board = [['O' for i in range(column)] for j in range(row)]
      self.player = 0
      # self.player1name = raw_input('What is your name, Player 1?')
      # self.player2name = raw_input("What is your name, Player 2?")
      # print self.player1name + " is Player 1, [R]ed."
      # print self.player2name + " is Player 2, [B]lue."
      # while self.moves_left > 0:
      #   self.print_board()
      #   if self.make_move():
      #     self.win_message()  
      #     break
      # if self.moves_left == 0:
      #   self.draw_message()
  
    def change_players(self):
      self.player = (self.player + 1) % 2 
    
    # def read_move(self):
    #   if self.player == 0:
    #   #   move = raw_input("What is your move, " + self.player1name + '?')
    #   # elif self.player == 1:
    #   #   move = raw_input("What is your move, " + self.player2name + '?')
    #   if not self.is_legal(move):
    #     print "That is not a legal move!"
    #     move = self.read_move()
    #   return move 
    
    def make_move(self,move):
      move = int(move)
      row = self.row-1 
      while self.board[row][move]!='O':
        row-=1 
      if self.player == 0:
        self.board[row][move] = 'R'
      else:
        self.board [row][move] = 'B'
      self.moves_left -= 1 
      if self.check_win(row,move):
        return True 
      self.change_players()
      
    def is_legal(self,move):
      try:
        move = int(move)
      except ValueError:
        return False
      if move < 0 or move >= self.column:
        return False
      elif self.board[0][int(move)]!='O':
        return False
      else:
        return True 
    
    def print_board(self):
      self.print_board2()
      #for row in self.board:
      #  print row 
    
    def print_board2(self):
      for row in self.board:
        print ('|'.join(row))
    
    def check_win(self,row,move):
      # Future work: Refactor everything with metaprogramming so this section doesn't have so much repeated code. 
      if self.player ==0:
        correct = 'R'
      else:
        correct = 'B'
      horizontal = 0 
      c = (row,move)
      current = list(c)
      
      while self.on_board(current):
        if self.board[current[0]][current[1]] == correct:
          horizontal += 1
          current[1] += 1
        else:
          break 
      current = list(c)
      current = [current[0],current[1]-1]
      
      while self.on_board(current):
        if self.board[current[0]][current[1]]==correct:
          horizontal+=1
          current[1]-=1 
        else:
          break
        
      vertical = 0
      current = list(c)
      while self.on_board(current):
        if self.board[current[0]][current[1]]==correct:
          vertical+=1
          current[0]+=1 
        else:
          break
      if horizontal>=4 or vertical>=4:
        return True
      
      if self.check_win_diagonal(correct, c):
        return True 
        
    def check_win_diagonal(self, correct, c):
      #downleft -- upright
      current = list(c)
      diag1  = -1 
      while self.on_board(current): #downleft 
        if self.board[current[0]][current[1]] == correct:
          diag1 += 1
          current[0] += 1 
          current[1] -= 1  
        else:
          break 
      
      current = list(c) 
      while self.on_board(current): #upright 
        if self.board[current[0]][current[1]] == correct:
          diag1 += 1 
          current[0] -= 1 
          current[1] += 1 
        else:
          break 
      
      # downright -- upleft 
      current = list(c)
      diag2 = -1 
      while self.on_board(current): #downright
        if self.board[current[0]][current[1]] == correct:
          diag2 += 1 
          current[0] += 1 
          current[1] += 1 
        else:
          break
      
      current = list(c)
      while self.on_board(current): #upleft
        if self.board[current[0]][current[1]] == correct:
          diag2 += 1 
          current[0] -= 1 
          current[1] -= 1 
        else:
          break
      
      if diag1 >= 4 or diag2 >= 4:
        return True 
      
    def win_message(self):
      self.print_board()
      print ('Victory!')
      if self.player==0:
        print (self.player1name + " Wins!")
      else:
        print (self.player2name + ' Wins!')
    
    def draw_message(self):
      self.print_board()
      print ("Draw!")
    
    def on_board(self,s):
      y, x = s[0], s[1]
      if y < 0 or y >= self.row:
        return False 
      if x < 0 or x >= self.column:
        return False
      return True 

    def stringify(self):
      """
      Returns a 42 character string representation of the board,
      starting with the top row and ending with the bottom row.
      """
      string=''
      for r in self.board:
        string += ''.join(r)
        #string += '\n'
      #answer = "\n".join('|'.join(row) for row in self.board)
      #return answer
      return string


if __name__=="__main__":
  x = Connect4()

