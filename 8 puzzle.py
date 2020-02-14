# =============================================================================
# @author Shubham Sonawane
# @brief BFS algorithm for 8 puzzle problem
# =============================================================================
import numpy as np

class Node:
    def __init__(self,puz, level):
        #puzzle is the arrangement of the digits
        #children is the frontier or the nodes to be explored
        #parent is the current node
        #pos is the position of the tile containing 0
        self.puzzle = puz[:]
        self.children = []  
        self.parent = None
        self.pos = 0
        self.level = 0
    
    def TakeInput():
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
            child = Node(puz, self.level + 1)
            #append to frontier/children list
            self.children.append(child)
            #self.level = self.level + 1
            #make parent node as current node
            child.parent = self
    
    def SlideRight(self):
        if(self.pos%3 < 2):
            puz = self.puzzle[:]
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos+1]
            puz[self.pos+1] = temp
            child = Node(puz, self.level + 1)
            self.children.append(child)
            #self.level = self.level + 1
            child.parent = self
    
    def SlideDown(self):
        if(self.pos!=6 and self.pos!=7 and self.pos!=8):
            puz = self.puzzle[:]
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos+3]
            puz[self.pos+3] = temp
            child = Node(puz, self.level + 1)
            self.children.append(child)
            #self.level = self.level + 1
            child.parent = self
    
    def SlideLeft(self):
        if(self.pos%3 != 0):
            puz = self.puzzle[:]
            temp = puz[self.pos]
            puz[self.pos] = puz[self.pos-1]
            puz[self.pos-1] = temp
            #child = Node(puz)
            child = Node(puz, self.level + 1)
            self.children.append(child)
            #self.level = self.level + 1
            child.parent = self
    
    def PuzzleIteration(self):
        self.pos = self.CheckZero(self.puzzle)        
        self.SlideUp()
        self.SlideRight()
        self.SlideDown()
        self.SlideLeft()
        #print("iter")
    
    def h_score(self):
        hs = 0
        goal = [1,2,3,4,5,6,7,8,0]
        for i in range(0,9):
            if self.puzzle[i] != goal[i] and self.puzzle[i] != 0:
                hs = hs + 1
        return hs
    
    def f_score(self):
        fs = 0
        fs = self.h_score() + self.level
        return fs
         
    def PrintScore(self):
        print("F-score = "+str(self.f_score))
    
        
def BFSalgo(rooot):
    visited_nodes = []
    frontier = []
    visited_nodes.append(rooot.puzzle )
    frontier.append(rooot)
    #return 0
    while True:
        CurrentPuzzle = frontier.pop(0)
        #CurrentPuzzle = frontier[0]
        #print("pop")        
        if CurrentPuzzle.CheckGoal():
                #print(Node.f_score())
                solution = []
                solution.append(CurrentPuzzle)
                while CurrentPuzzle.parent != None:
                    CurrentPuzzle = CurrentPuzzle.parent
                    solution.append(CurrentPuzzle)                    
                return solution
        CurrentPuzzle.PuzzleIteration()
        for i in range(len(CurrentPuzzle.children)):
            ToBeExplored = CurrentPuzzle.children[i]
            if(not ToBeExplored.puzzle in visited_nodes):
                frontier.append(ToBeExplored)
                visited_nodes.append(ToBeExplored.puzzle) 
        #print(len(visited_nodes))

def NodesVisited(root): 
    visited_nodes = []
    frontier = []
    visited_nodes.append(root.puzzle )
    frontier.append(root)
    #return 0
    while True:
        CurrentPuzzle = frontier.pop(0)
        #CurrentPuzzle = frontier[0]
        #print("pop")        
        if CurrentPuzzle.CheckGoal():
            pass                
        CurrentPuzzle.PuzzleIteration()
        for i in range(len(CurrentPuzzle.children)):
            ToBeExplored = CurrentPuzzle.children[i]
            if(not ToBeExplored.puzzle in visited_nodes):
                frontier.append(ToBeExplored)
                visited_nodes.append(ToBeExplored.puzzle) 
        #return(len(visited_nodes))
        return visited_nodes
    
            

if __name__ == "__main__":
    level = 0
    #fx = []
    #fx = Node.f_score()
    visited = []
    count = 0
    puzzle = Node.TakeInput()
    root = Node(puzzle,level)
    #check solvabiity
    for i in range(0,8):
        for j in range(i,9):
            if(puzzle[i] > puzzle[j] and puzzle[j] != 0):
                count = count + 1
    if count % 2 == 1:
        print("No solution exists")
    else:
        #root = Node(puzzle)
        print("Solution exists")
        #print(root.puzzle)
        #print(root.level)
        #f = BFSalgo(root)
        sol = BFSalgo(root)
        visited = NodesVisited(root)
        sol.reverse()
        #print(visit_num)
        #trial = sol[root.puzzle[0]]
        #print(sol[root.puzzle[0]])
        #fx = sol[0].f_score()
        #arr1 = np.asarray(sol[0].puzzle)
        #print(arr1)
        
            #sol[i].level
            #fx = sol[i].f_score()
    
           
"""if __name__ == "__main__":
    main() """    
    
            
        