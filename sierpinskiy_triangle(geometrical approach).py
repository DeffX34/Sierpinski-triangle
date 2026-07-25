from math import *

draw_symbol = "@"
empty_symbol = "."
draw_canvas = {}
canvas_view = ""
r = 30
n = 3
canvas_size = 70

def get_S(r):
    return 3*sqrt(3)*r**2

def get_points(x,y,r):
    a = pi/2 if n % 2 != 0 else 0
    points = []
    for i in range(n):
        point = (round((x + r * cos(2*pi*i/n + a) )* 2) , round(y + r * sin(2*pi*i/n + a)))
        points.append(point)
    return points

def brezenhemalgorythm(points):
    edges = []
    for p in range(len(points)):

        endx, endy = points[p+1 if p != len(points)-1 else 0][0], points[p+1 if p != len(points)-1 else 0][1]
        cx, cy = points[p][0], points[p][1]
        dx, dy = abs(endx - cx), abs(endy - cy)
        sx, sy = 1 if cx < endx else -1, 1 if cy < endy else -1

        if dx > dy:
            err = 2 * dy - dx
        else:
            err = 2 * dx - dy

        while True:
            if (cx, cy) == (endx, endy):
                break
            if dx > dy:
                edges.append((cx, cy))
                if err >= 0:
                    cx, cy = cx + sx, cy + sy
                    err = err + 2 * dy - 2 * dx
                    edges.append((cx, cy))
                elif err < 0:
                    cx += sx
                    err = err + 2 * dy
                    edges.append((cx, cy))
            else:
                edges.append((cx, cy))
                if err >= 0:
                    cx, cy = cx + sx, cy + sy
                    err = err + 2 * dx - 2 * dy
                    edges.append((cx, cy))
                elif err < 0:
                    cy += sy
                    err = err + 2 * dx
                    edges.append((cx, cy))

    return edges

def drawserpinskiytriangle():
    draw_points = []
    expt = 0
    tcoords = None
    allpoints = {}
    points = 0
    radius = r

    for i in range(4):
        if i == 0:
            allpoints[i] = []
            points = get_points(0,-10, r)
            edges = brezenhemalgorythm(points)
            allpoints[i].append(points)
            for p in points:
                draw_points.append(p)
            for e in edges:
                draw_points.append(e)
            expt = 3
        else:
            allpoints[i] = []
            iterator = 0
            for t in range(expt):

                ind = t % 3

                area = radius/2.0

                xc = allpoints[i-1][iterator][ind][0] / 2 + (area/1.12 if ind == 1 else -area/1.12 if ind == 2 else 0)
                yc = allpoints[i-1][iterator][ind][1] + (-area/1.05 if ind == 0 else area/2)
            
                points = get_points(xc, yc, area)

                edges = brezenhemalgorythm(points)
                allpoints[i].append(points)
                for p in points:
                    draw_points.append(p)
                for e in edges:
                    draw_points.append(e)

                if ind == 2:
                    iterator += 1

        radius = radius / 2 if i != 0 else radius
        expt = 3**(i+1) if i != 0 else expt

    for y in range(canvas_size//2, -canvas_size//2, -1):
        for x in range(-canvas_size, canvas_size):
            if (x,y) in draw_points:
                draw_canvas[x,y] = draw_symbol

for y in range(canvas_size//2, -canvas_size//2, -1):
    for x in range(-canvas_size, canvas_size):
        draw_canvas[x,y] = empty_symbol

drawserpinskiytriangle()

for yV in range(canvas_size//2, -canvas_size//2, -1):
    for xV in range(-canvas_size, canvas_size):
        canvas_view += draw_canvas[xV,yV]

    canvas_view += "\n"

print(canvas_view)