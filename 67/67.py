grid = []

for line in open('p067_triangle.txt'):
    grid.append(list(map(int,line.split())))

for i in range(1, len(grid)):
    for j in range(len(grid[i])):
        if j == 0:
            grid[i][j] += grid[i-1][j]
        elif j == len(grid[i-1]):
            grid[i][j] += grid[i-1][j-1]
        else:
            grid[i][j] += max(grid[i-1][j-1], grid[i-1][j])

print(max(grid[-1]))