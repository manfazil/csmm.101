import Queue as Q

import time

import resource

import sys

import math

#### SKELETON CODE ####

## The Class that Represents the Puzzle

class PuzzleState(object):

    """docstring for PuzzleState"""

    def __init__(self, config, n, parent=None, action="Initial", cost=0):

        if n*n != len(config) or n < 2:

            raise Exception("the length of config is not correct!")

        self.n = n

        self.cost = cost

        self.parent = parent

        self.action = action

        self.dimension = n

        self.config = config

        self.children = []

        for i, item in enumerate(self.config):

            if item == 0:

                self.blank_row = i / self.n

                self.blank_col = i % self.n

                break

    def display(self):

        for i in range(self.n):

            line = []

            offset = i * self.n

            for j in range(self.n):

                line.append(self.config[offset + j])

            print line

    def move_left(self):

        if self.blank_col == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):

        if self.blank_col == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):

        if self.blank_row == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):

        if self.blank_row == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):

        """expand the node"""

        # add child nodes in order of UDLR

        if len(self.children) == 0:

            up_child = self.move_up()

            if up_child is not None:

                self.children.append(up_child)

            down_child = self.move_down()

            if down_child is not None:

                self.children.append(down_child)

            left_child = self.move_left()

            if left_child is not None:

                self.children.append(left_child)

            right_child = self.move_right()

            if right_child is not None:

                self.children.append(right_child)

        return self.children

# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters

def writeOutput():

    ### Student Code Goes here

def bfs_search(initial_state):

    """BFS search"""

    frontier=Q.Queue()
    frontier.put(initial_state)
    explored = set()

    path_to_goal=[]
    cost_of_path=len(path_to_goal)
    res={}
    search_depth=max_search_depth=running_time=max_ram_usage=0
    
    while frontier:
        state = frontier.get()
        explored.add(state)
        if test_goal(state):
            res["path_to_goal"]=path_to_goal
			res["cost_of_path"]=cost_of_path
			res["nodes_expanded"]=nodes_expanded
			res["search_depth"]=search_depth
			res["max_search_depth"]=max_search_depth
			
            return res

        for neighbor in state.expand():
			nodes_expanded+=len(state.expand)
			search_depth+=1
			if search_depth > max_search_depth: max_search_depth=search_depth		
            if neighbor not in frontier and neighbor not in explored:
                frontier.put(neighbor)
	return False
    
    

    ### STUDENT CODE GOES HERE ###

def dfs_search(initial_state):

    """DFS search"""

    ### STUDENT CODE GOES HERE ###

def A_star_search(initial_state):

    """A * search"""

    ### STUDENT CODE GOES HERE ###

def calculate_total_cost(state):

    """calculate the total estimated cost of a state"""

    ### STUDENT CODE GOES HERE ###

def calculate_manhattan_dist(state):

    """calculatet the manhattan distance of a tile"""

    posIdeal=[(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    n=3
    distancia=0
    for i,item in enumerate(state):
        if item !=0:
            curX=i/n
            curY=i%n
            offset= abs(curX-posIdeal[item-1][0])+abs(curY-posIdeal[item-1][1])
            distancia+=offset            
    return distancia
                        

def test_goal(puzzle_state):

    """test the state is the goal state or not"""

    ### STUDENT CODE GOES HERE ###
    return puzzle_state==[0,1,2,3,4,5,6,7,8]

# Main Function that reads in Input and Runs corresponding Algorithm

def main():

    sm = sys.argv[1].lower()

    beg

in_state = sys.argv[2].split(",")

    begin_state = tuple(map(int, begin_state))

    size = int(math.sqrt(len(begin_state)))

    hard_state = PuzzleState(begin_state, size)

    if sm == "bfs":

        bfs_search(hard_state)

    elif sm == "dfs":

        dfs_search(hard_state)

    elif sm == "ast":

        A_star_search(hard_state)

    else:

        print("Enter valid command arguments !")

if __name__ == '__main__':

    main()


