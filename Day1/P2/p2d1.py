with open('input.txt') as f:
    lines = f.readlines()
    
    
words = {'one': 'o1ne', 'two': 't2wo', 'three': 'th3ree', 'four': 'fo4ur', 'five': 'fi5ve', 'six': 'si6x', 'seven': 'sev7en', 'eight': 'eig8ht', 'nine':'ni9ne'} 
 
 
def word_to_num(line):
    # print(line)
    for k, v in words.items():
        line = line.replace(k, v)
    return str(line)
    
    
all_converted = [] 
for l in lines:
    res = word_to_num(l)
    all_converted.append(res)


all_saves = []
for l in all_converted:
    per_line = []
    for elem in l:
        if elem.isnumeric():
            per_line.append(elem)
    all_saves.append(int(per_line[0] + per_line[-1]))


print(sum(all_saves))





    