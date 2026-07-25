size = 50
draw_symbol = "@"
triangle_view = ""
rows = {}

for i in range(0, size):
    rows[i] = []
    if i > 2: del rows[i-2]

    triangle_view += (size - i) * " "
    
    for j in range(i):
        triangle_view += " "
        if i < 2 or i == size - 1 or j == 0 or j == i - 1: val = 1
        elif i > 1: val = rows[i-1][j-1] + rows[i-1][j] 
        triangle_view += draw_symbol if val % 2 == 1 else " "
        rows[i].append(val)
    triangle_view += "\n"

print(triangle_view)