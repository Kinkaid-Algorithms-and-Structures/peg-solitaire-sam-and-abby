class Board:
    def __init__(self):
        self.board=[]
        for i in range(0,4):
            new_row=[]
            self.board.append(new_row)
        blank=(0,False)
        self.board[0]=[blank,blank,blank,blank,(1,False),blank,blank,blank,blank]
        self.board[1]=[blank,blank,blank,(2,True),blank,(3,True),blank,blank,blank]
        self.board[2]=[blank,blank,(4,True),blank,(5,True),blank,(6,True),blank,blank]
        self.board[3]=[blank,(7,True),blank,(8,True),blank,(9,True),blank,(10,True),blank]
        self.board[4]=[(11,True),blank,(12,True),blank,(13,True),blank,(14,True),blank,(15,True)]
    def move(self,id1,id2):
        pass


