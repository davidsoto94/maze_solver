from cell import Cell
import time


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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
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
            time.sleep(0.05)