def star_triangle(rows):
    for i in range(1, rows + 1):
        line = ""
        for j in range(i):
            line = line + "* "
        print(line)

height = 5
star_triangle(height)