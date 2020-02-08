class Node:
    def __init__(self,puz,level):
        #puzzle is the arrangement of the digits
        #children is the frontier or the nodes to be explored
        #parent is the current node
        #x is the position of the tile
        self.puzzle = puz[:]
        self.children = []  
        self.parent = None
        self.pos = 0
        self.level = 0
    
    def TakeInput(self):
        new_puzzle = [int(x) for x in input().split()]
        return new_puzzle
        
    def CheckZero(self,puz):
        for i in range(0,9):
            if puz[i] == 0:
                return i
    
    def CheckGoal(self):
        GoalFlag = True
        goal = [1,2,3,4,5,6,7,8,0]
        if goal != self.puzzle:
            GoalFlag = False
            return GoalFlag
        return GoalFlag
    
    
    def SlideUp(self):
        if(self.pos!=0 and self.pos!=1 and self.pos!=2):
            puz = self.puzzle[:]
            #swap the digits
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos-3]
            puz[self.pos-3] = temp
            child = Node(puz, self.level+1)
            #append to frontier/children list
            self.children.append(child)
            #make parent node as current node
            child.parent = self
    
    def SlideRight(self):
        if(self.x%3 < 2):
            puz = self.puzzle[:]
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos+1]
            puz[self.pos+1] = temp
            child = Node(puz, self.level+1)
            self.children.append(child)
            child.parent = self
    
    def SlideDown(self):
        if(self.pos!=6 and self.pos!=7 and self.pos!=8):
            puz = self.puzzle[:]
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos+3]
            puz[self.pos+3] = temp
            child = Node(puz, self.level+1)
            self.children.append(child)
            child.parent = self
    
    def SlideLeft(self):
        if(self.pos%3 != 0):
            puz = self.puzzle[:]
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos-1]
            puz[self.pos-1] = temp
            child = Node(puz, self.level+1)
            self.children.append(child)
            child.parent = self
    
    def PuzzleIteration(self):
        self.x = self.CheckZero(self.puzzle)        
        self.SlideUp()
        self.SlideRight()
        self.SlideDown()
        self.SlideLeft()
            
        