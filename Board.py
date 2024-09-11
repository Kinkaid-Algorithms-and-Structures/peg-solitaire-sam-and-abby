class Board:
    def __init__(self):
        self.board=[]
        for i in range(0,4):
            new_row=[]
            self.board.append(new_row)
        blank=[0,False]
        self.board[0]=[blank,blank,blank,blank,[1,False],blank,blank,blank,blank]
        self.board[1]=[blank,blank,blank,[2,True],blank,[3,True],blank,blank,blank]
        self.board[2]=[blank,blank,[4,True],blank,[5,True],blank,[6,True],blank,blank]
        self.board[3]=[blank,[7,True],blank,[8,True],blank,[9,True],blank,[10,True],blank]
        self.board[4]=[[11,True],blank,[12,True],blank,[13,True],blank,[14,True],blank,[15,True]]
    def move(self, x1,y1, direction):
        #assumes the move has already been checked by check_if_legal
        point1 = self.board[y1][x1]
        point2= self.check_if_legal(x1,y1, direction)[2]
        midpoint = self.check_if_legal(x1, y1, direction)[1]
        point1[1]=False
        point2[1]=True
        midpoint[1]=False



    def check_if_legal(self,x1,y1,direction):
        point1=self.board[y1][x1]
        blank = (0,0)
        if point1[1]:
            if direction=="right":
                if x1>=5 :
                    return False, blank, blank
                point2=self.board[y1][x1+4]
                midpoint=self.board[y1][x1+2]
            elif direction=="left":
                if x1<=3:
                    return False, blank, blank
                point2 = self.board[y1][x1 - 4]
                midpoint = self.board[y1][x1 - 2]
            elif direction=="top right":
                if x1>=7 and y1<=1 :
                    return False, blank, blank
                point2 = self.board[y1-2][x1 +2]
                midpoint = self.board[y1-1][x1 +1]
            elif direction=="top left":
                if x1<=1 and y1<=1:
                    point2 = self.board[y1-2][x1 - 2]
                    midpoint = self.board[y1-1][x1 - 1]
            elif direction=="bottom right":
                if x1>=7 and y1<=3 :
                    return False, blank, blank
                point2 = self.board[y1+2][x1 +2]
                midpoint = self.board[y1+1][x1 +1]
            elif direction=="bottom left":
                if x1 <= 1 and y1 <= 3:
                    return False, blank, blank
                point2 = self.board[y1 + 2][x1 - 2]
                midpoint = self.board[y1 + 1][x1 - 1]
            else:
                return False, blank, blank
            if point2[0] == 0:
                return False, blank, blank
            elif point2[1]:
                return False, blank, blank
            elif not midpoint[1]:
                return False, blank, blank
            else:
                return True, midpoint, point2
    def count_pegs(self):
        counter= 0
        for row in self.board:
            for column in row:
                if self.board[row][column][1]:
                    counter+=1
        return counter

    def draw(self):
        for row in self.board:
            print(' '.join(['o' if col[1] else '.' for col in row]))







