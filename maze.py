import random
from cell import Cell
import time

from graphics import Line, Point


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed=seed
        if seed != None:
            self.seed=random.seed(seed)
        self._create_cells()
        
    
    def _create_cells(self):
        self._cells = []
        for i in range(0,self.num_cols):
            rows = []
            for j in range(0,self.num_rows):
                cell = Cell(self.win)
                rows.append(cell)
            self._cells.append(rows)
            
        for i in range(0,self.num_cols):
            for j in range(0,self.num_rows):
                self._draw_cell(i,j)
        self._break_entrance_and_exit()
        self.break_walls_r(0,0)
    
    def _draw_cell(self,i,j):
        x_start = i * self.cell_size_x + self.x1
        y_start = j * self.cell_size_y + self.y1
        x_end = i * self.cell_size_x + self.x1 + self.cell_size_x
        y_end = j * self.cell_size_y + self.y1 + self.cell_size_y
        if self.win != None:
             self._cells[i][j].draw(x_start,y_start,x_end,y_end)
        self._animate()

    def _animate(self):
        if self.win != None:
            self.win.redraw()
            time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def break_walls_r(self, i, j):
        self._cells[i][j].visited=True
        while True:
            posible_directions = []
            if i-1 > 0:
                if self._cells[i-1][j].visited == False:
                    posible_directions.append(('left'))
            if i+1 < self.num_cols:
                if self._cells[i+1][j].visited == False:
                    posible_directions.append('rigth')
            if j-1 > 0:
                if self._cells[i][j-1].visited == False:
                    posible_directions.append('up')
            if j+1 < self.num_rows:
                if self._cells[i][j+1].visited == False:
                    posible_directions.append('down')
            if len(posible_directions) == 0:
                return
            selected = ''
            if self.seed == None:
                selected = random.choice(posible_directions)
            else:
                selected = self.seed.choice(posible_directions)
            
            if selected == 'left':
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i,j)
                self._cells[i-1][j].has_right_wall = False
                self._draw_cell(i-1,j)
                self.break_walls_r(i-1,j)
            if selected == 'rigth':
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i,j)
                self._cells[i+1][j].has_left_wall = False
                self._draw_cell(i+1,j)
                self.break_walls_r(i+1,j)
            if selected == 'up':
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i,j)
                self._cells[i][j-1].has_bottom_wall = False
                self._draw_cell(i,j-1)
                self.break_walls_r(i,j-1)
            if selected == 'down':
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i,j)
                self._cells[i][j+1].has_top_wall = False
                self._draw_cell(i,j+1)
                self.break_walls_r(i,j+1)

            
