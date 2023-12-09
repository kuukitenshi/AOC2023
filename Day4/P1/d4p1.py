with open('input.txt') as f:
    lines = f.readlines()

delimiters = [':', '|']


splited_lines = []    
for line in lines:
    for delimiter in delimiters:
        line = "#".join(line.split(delimiter))
    res = line.split("#")
    splited_lines.append(res)

points_per_card = []
for card in splited_lines:
    win_values = [int(x) for x in card[1].split()]
    has_win = []
    values = [int(x) for x in card[-1].split()]
    for all_value in values:
        if all_value in win_values:
            has_win.append(all_value)
    points = pow(2, len(has_win)-1) if len(has_win) > 0 else 0
    points_per_card.append(points)
    
print(sum(points_per_card))
        
 

