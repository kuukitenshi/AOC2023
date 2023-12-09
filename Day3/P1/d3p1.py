grid = []


with open('input.txt') as f:
    for line in f.readlines():
        grid.append(line.strip())


l = len(grid)
c = len(grid[0])    
        
        
def is_symbol(elem):
    return elem != '.' and not elem.isdigit()


def adjacents(i, j_num_start, j_num_end):
    adjacent = set()
    for j in range(j_num_start, j_num_end):
        for ci in [-1, 0, 1]:
            for cj in [-1, 0, 1]:
                if (ci, cj) == (0, 0):
                    continue
                neig_i, neig_j = i + ci, j + cj
                if 0 <= neig_i < l and 0 <= neig_j < c:
                    adjacent.add((neig_i, neig_j))
    return adjacent


num_total = 0
for i in range(l):
    j = 0
    while j < c:
        if not grid[i][j].isdigit():
            j += 1
            continue
        j2 = j + 1
        while j2 < c and grid[i][j2].isdigit():
            j2 += 1
        if any(is_symbol(grid[neig_i][neig_j]) for neig_i, neig_j in adjacents(i, j, j2)):
            num = int(grid[i][j:j2])
            num_total += num
        j = j2
print(num_total)