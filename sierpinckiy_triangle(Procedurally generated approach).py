size = 50
draw_symbol = "@"
triangle_view = ""
rows = {}

for i in range(0, size):
    rows[i] = []

    if i > 2: del rows[i-2]

    triangle_view += (size - i) * " "
    
    for j in range(i):
        value = None
        triangle_view += " "

        if i < 2 or i == size - 1 or j == 0 or j == i - 1: 
            rows[i].append(1) 
            triangle_view += draw_symbol
            
        elif i > 1: 
            value = rows[i-1][j-1] + rows[i-1][j]
            rows[i].append(rows[i-1][j-1] + rows[i-1][j])

        if value != None: triangle_view += draw_symbol if value % 2 == 1 else " "
        
    triangle_view += "\n"

print(triangle_view)