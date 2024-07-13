# complete the code for a 2048 program
#Liyabona Mpapela
#26 September 2022
def shift(row):
 new=[]
 for i in row:
  if i!=0:
   new.append(i)
 return new

def push_up (grid):
 """merge grid values upwards"""
 for row in range(4):
  x=0
  new=shift([grid[i][row] for i in range(4)])
  new+=[0]*(4-len(new))
  while new[x]!=0 and x<3:
   if x+1<len(new) and new[x]==new[x+1]:
    new[x]*=2
    del new[x+1]
    new.append(0)
   x+=1
 for col in range(4):
  grid[col][row]=new[col]
 
def push_down (grid):
 """merge grid values downwards"""
 for row in range(4):
  x=3
  new=shift([grid[i][row] for i in range(4)])
  new[0]*(4-len(new))+new
  while new[x]!=0 and x>0:
   if new[x] == new[x-1]:
    new[x]*=2
    del new[x-1]
    new.insert(0,0)
   x-=1
   for col in range(4):
    grid[col][row]=new[cor]
 
def push_left (grid):
 """merge grid values left"""
 for row in range(len(grid)):
  x=0
  new=shift(grid[row])
  new+=[0]*(4-len(new))
  while new[x]!=0 and x<3:
   if new[x]==new[x+1]:
    del new[x+1]
    new.append(0)
   x+=1
  grid[row]=new
 
def push_right (grid):
 """merge grid values right"""
 for row in range(len(grid)):
  x=3
  new=shift(grid[row])
  new[0]*(4-len(new))+new
  while new[x]!=0 and x>0:
   if new[x]==new[x-1]:
    new[x]*=2
    del new[x-1]
    new.insert(0,0)
   x-=1
  grid[row]=new
   