from collections import defaultdict


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


neig_freq = defaultdict(list)
for i in range(l):
    j = 0
    while j < c:
        if not grid[i][j].isdigit():
            j += 1
            continue
        j2 = j + 1
        while j2 < c and grid[i][j2].isdigit():
            j2 += 1
        adjs = adjacents(i, j, j2)
        for neig_i, neig_j in adjs:
            if grid[neig_i][neig_j] == '*':
                numb = int(grid[i][j:j2])
                neig_freq[(neig_i, neig_j)].append(numb)  
        j = j2

# print(neig_freq)
sum_exctly2 = 0
for freq in neig_freq.values():
    if len(freq) == 2:
        sum_exctly2 += (freq[0]*freq[1])
print(sum_exctly2)