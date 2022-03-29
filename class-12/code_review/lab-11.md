# Chess board


```python

def add_red(row, col):
    grid[row][col]=[1,0.2,0]
    self.red = [row, col]


def add_blue(row, col):
    grid[row][col]=[0,1,1]
    self.blue = [row, col]


# coloring the grid

"""
- initialize the board either 1's or 0's (either all cells are black or white)
- loop through the board in range of 64
- declare a count starting from 0 
- on each iteration increase count by one in each loop
- if count is even color the cell with white else color it with black

"""

"""
- initialize the board either 1's or 0's (either all cells are black or white)
- loop through the each row  in range of 8
- loop through the each col  in range of 8
- declare a count starting from 0 
- if count is even color the cell with white else color it with black

"""
def is_under_attack():
    # Horizontal
    if self.red[0] == self.blue[0]:
        return True
    elif self.red[1] == self.blue[1]:
        return True
    elif (abs(self.red[0]-self.blue[0])==abs(self.red[1]-self.blue[1])):
        return True
    
    return False


my_tuple = ()

```