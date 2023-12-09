with open('input.txt') as f:
    lines = f.readlines()

delimiters = [':', ",",";"]

splited_lines = []    
for line in lines:
    for delimiter in delimiters:
        line = "#".join(line.split(delimiter))
    res = line.split("#")
    splited_lines.append(res)
    
ids = []
for sl in splited_lines:
    max_red = 0
    max_blue = 0
    max_green = 0
    game_num = int(sl[0].split()[-1])
    for s in sl[1:]:
        if 'red' in s:
            num = int(s.split()[0])
            max_red = max(max_red, num)
        if 'green' in s:
            num = int(s.split()[0])
            max_blue = max(max_blue, num)
        if 'blue' in s:
            num = int(s.split()[0])
            max_green = max(max_green, num)
    ids.append(max_red * max_blue * max_green)       
print(ids)
print(sum(ids))
        
    