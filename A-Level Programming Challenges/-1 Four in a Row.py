class Player():
    def __init__(self,name):
        self.__player_name = name
        self.__player_number = 10
    
    def player():
        #creates new player
        
    def getName(self):
        print (self.__player_name)
    
    def getNumber(self):
        print (self.__player_number)
    
    def makeMove(self):
        self.__player_number -= 1
        #now call board to make the move
        #ask user for column first
        
    def checkWinner(self):
        #returns player name if they have won
        # nobody if they havent
        
class Board():
    def __init__(self,columns,rows):
        self.__columns = columns
        self.__rows = rows
        self.__board = [[], []]
    
    def board(self):
        #creates new board
        
    def display(self):
        '''Printing the whole board'''
        for row in self.__board:
            for column in self.__board:
                print (board[row,column])
                
    def columnFull(self):
        if column = self.__columns:
            print ("Column Full")
            
    def boardFull(self):
        '''Checking to see if the columns are full by checking
            if the top of the column contains one of the 4 players
            then if the number of full columns = original number
            then its full'''
        columnsFull = 0:
        for column in self.__board:
            if board[[column][self.__rows]] in ["A","B","C","D"]:
                columnsFull +=1
        if columnsFull == self.__columns:
            print ("Board full")
            
    def getWidth(self):
        return self.__columns
    
    def addToken(self,column) #add the token from player here somehow
        '''Adding a players token to the next empty row'''
        #Iterates through in reverse (or should do at least)
        for row in range(len(self.board[column],1,-1)):
            if self.board[[column][row]] not in ["A","B","C","D"]
                emptyRow = row
            
        self.__board[column,emptyRow] = #token
        
r        