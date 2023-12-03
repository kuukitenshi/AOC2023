with open('input.txt') as f:
    lines = f.readlines()
    
    
all_saves = [] 
for l in lines:
    per_line = []
    for elem in l:
        if elem.isnumeric():
            per_line.append(elem)
    all_saves.append(int(per_line[0] + per_line[-1]))
    
print(sum(all_saves))