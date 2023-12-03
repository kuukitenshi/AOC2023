with open('test.txt') as f:
    lines = f.readlines()
    
 
words = ['on', 'w', 'hre', 'ou', 'iv', 'ix', 'eve', 'igh', 'in']
# one two three four five six seven eight nine  
 
def word_to_num(line):
    # print(line)
    for w in words:
        line = line.replace(w, str(words.index(w)+1))
    # print(line)
    # print('-'*40)
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





    