# manipulating 2-dimensional arrays of size 4x4
#Liyabona Mpapela
#26 September 2022
def create_grid(grid):
 
    
    for i in range(4):
        col = []
        for j in range(4):
            col.append(0)
        grid.append(col) 


def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+'+'-'*20+'+')
    for i in range(len(grid)):
        print('|',end='')
        for l in range(len(grid[i])):
            if grid[i][l]==0:
                print(' '*5,end="")
            else:
                print("{0:<5}".format(grid[i][l]),end= "")
        print('|',end='')
        print()
    print('+'+'-'*20+'+')

def check_lost (grid):
    """return True if there are no 0 values and there are no
    adjacent values that are equal; otherwise False"""
    for i in range(len(grid)):
        for l in range(len(grid[i])):
            if grid[i][l]==0:
                return False
            if l+1<len(grid[i]) and grid[i][l]==grid[i][l+1]:
                return False
            if i+1<len(grid) and grid[i][l] == grid[i+1][l]:
                return False
    return True
   
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise
    False"""
    ans=False
    for i in range(len(grid)):
        for l in range(len(grid[i])):
            if grid[i][l]>=32 :
                ans = True
    return ans 

def copy_grid (grid):
    """return a copy of the given grid"""
    gridcopy=[]
    for i in grid:
        col=[]
        for l in i:
            col.append(l)
        gridcopy.append(col)
    return gridcopy
 
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""  
    for i in range(len(grid1)):
        for l in range(len(grid1[i])): 
            if grid1[i][l]!=grid2[i][l]:
                return False
    return True