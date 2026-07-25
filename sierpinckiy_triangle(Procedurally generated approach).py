size = 40
draw_symbol = "@"
triangle_view = ""
rows = {}

for i in range(1, size):
    rows[i] = []

    for j in range(i):
        if i < 2 or i == size or j == 0 or j == i - 1: rows[i].append(1)    
        elif i > 2: rows[i].append(rows[i-1][j-1] + rows[i-1][j])

    triangle_view += (size - i) * " "

    for k in rows[i]:
        triangle_view += " " 
        triangle_view += draw_symbol if k % 2 == 1 else " "

    triangle_view += "\n"

print(triangle_view)