with open('input.txt', 'r') as f:
    lines = f.readlines()
    
cards = []
for line in lines:
    line_splited = line.split()[1:]
    card_num = int(line_splited[0].split(':')[0])
    row = line_splited[1:]
        
    i = row.index('|')
    win_set = set(row[:i])
    all_values = set(row[i+1:])
        
    matches_num = 0
    for elem in all_values:
        if elem in win_set:
            matches_num += 1
    cards.append((card_num, matches_num))

# print(cards)
freq = [1 for _ in range(len(lines))]

for ic, matches_num in cards:
    print(ic, matches_num)
    for m in range(matches_num):
        freq[ic + m] += freq[ic-1]
print(freq)
print(sum(freq))