from tkinter import Tk, Canvas

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.path = []
        self.found_exit = False
    
    def solve(self, start_row, start_col):
        self._explore(start_row, start_col)
    
    def _explore(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        
        if self.maze[row][col] == 'E':
            self.found_exit = True
            self.path.append((row, col))
            return True
        
        if self.maze[row][col] == '#' or self.visited[row][col]:
            return False
        
        self.visited[row][col] = True
        self.path.append((row, col))
        
        if self._explore(row, col + 1):  # Right
            return True
        if self._explore(row + 1, col):  # Down
            return True
        if self._explore(row, col - 1):  # Left
            return True
        if self._explore(row - 1, col):  # Up
            return True
        
        self.path.pop()
        return False


# Příklad bludiště
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['E', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]


# Vykreslení bludiště
def draw_maze(canvas):
    canvas.delete("all")
    rows = len(maze)
    cols = len(maze[0])
    cell_width = 40
    cell_height = 40

    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_width
            y1 = row * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            if maze[row][col] == '#':
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            elif maze[row][col] == 'E':
                canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            elif maze[row][col] == ' ':
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")

    canvas.pack()


# Vykreslení robota
def draw_robot(canvas, row, col):
    cell_width = 40
    cell_height = 40
    x1 = col * cell_width
    y1 = row * cell_height
    x2 = x1 + cell_width
    y2 = y1 + cell_height
    canvas.create_oval(x1, y1, x2, y2, fill="red")
    canvas.pack()


# Hlavní funkce
def main():
    root = Tk()
    root.title("Maze Solver")
    canvas = Canvas(root, width=400, height=360)
    canvas.pack()

    draw_maze(canvas)

    solver = MazeSolver(maze)
    start_row = 1
    start_col = 1
    solver.solve(start_row, start_col)
    path = solver.path

    for row, col in path:
        draw_robot(canvas, row, col)
        canvas.update()
        canvas.after(500)  # Zpoždění 0,5 sekundy

    root.mainloop()


if __name__ == "__main__":
    main()