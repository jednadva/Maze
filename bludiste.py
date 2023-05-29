from tkinter import Tk, Canvas

# Velikost bludiště (počet řádků a sloupců)
ROWS = 10
COLS = 10

# Bludiště (0 = volná cesta, 1 = překážka)
maze = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0]
]

# Velikost jednotlivých buněk
CELL_SIZE = 30

# Počáteční pozice robota
start_x = 0
start_y = 0

# Cílová pozice robota
target_x = COLS - 1
target_y = ROWS - 1

def draw_maze(canvas):
    # Vykreslení bludiště
    for row in range(ROWS):
        for col in range(COLS):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if maze[row][col] == 0:
                canvas.create_rectangle(x1, y1, x2, y2, fill='white')
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill='black')

def draw_robot(canvas, x, y):
    # Vykreslení robota
    x1 = x * CELL_SIZE
    y1 = y * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE
    canvas.create_oval(x1, y1, x2, y2, fill='red')

def move_robot(event):
    # Pohyb robota po bludišti
    global start_x, start_y

    if event.keysym == 'Up' and start_y > 0 and maze[start_y - 1][start_x] == 0:
        start_y -= 1
    elif event.keysym == 'Down' and start_y < ROWS - 1 and maze[start_y + 1][start_x] == 0:
        start_y += 1
    elif event.keysym == 'Left' and start_x > 0 and maze[start_y][start_x - 1] == 0:
        start_x -= 1
    elif event.keysym == 'Right' and start_x < COLS - 1 and maze[start_y][start_x + 1] == 0:
        start_x += 1

    canvas.delete('all')
    draw_maze(canvas)
    draw_robot(canvas, start_x, start_y)

# Inicializace okna
root = Tk()
root.title('Robot Maze')
canvas = Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
canvas.pack()

# Vykreslení bludiště a robota
draw_maze(canvas)
draw_robot(canvas, start_x, start_y)

# Reakce na stisk kláves
canvas.bind_all('<KeyPress-Up>', move_robot)
canvas.bind_all('<KeyPress-Down>', move_robot)
canvas.bind_all('<KeyPress-Left>', move_robot)
canvas.bind_all('<KeyPress-Right>', move_robot)

# Spuštění hlavní smyčky
root.mainloop()