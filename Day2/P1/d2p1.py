with open('input.txt') as f:
    lines = f.readlines()


delimiters = [':', ",",";"]
 
ids = set()   
for line in lines:
    line = line.split(':')
    game= line[0]
    game_num = int(game.split()[1])
    for slot in line:
        line = slot.split(';')
    # print(line)
    # print(game_num)

    isAvalible = True
    false = True
    for slots_comma in line:
        slot = slots_comma.split(',')
        count_red = 0
        count_blue = 0
        count_green = 0
        # print('Comma', slots_comma)
        # print('slots', slot)
        for s in slot:
            # print('s', s)
            if 'red' in s:
                num = int(s.split()[0])
                count_red += num
            if 'green' in s:
                num = int(s.split()[0])
                count_green += num  
            if 'blue' in s :
                num = int(s.split()[0])
                count_blue += num 
            if count_red > 12 or count_green > 13 or count_blue > 14:
                false = False
                break
        if isAvalible and false == False:
            if game_num in ids:
                ids.remove(game_num)
            break
        else:
            ids.add(game_num)
            
print(ids)
print(sum(ids))        
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 #--------------------------
 
 

# splited_lines = []    
# for line in lines:
#     for delimiter in delimiters:
#         line = "#".join(line.split(delimiter))
#     res = line.split("#")
#     splited_lines.append(res)
    
    
# ids = []


# for sl in splited_lines:
#     count_red = 0
#     count_blue = 0
#     count_green = 0
#     game_num = int(sl[0].split()[-1])
#     for s in sl[1:]:
#         if 'red' in s:
#             num = int(s.split()[0])
#             count_red += num
#         if 'green' in s:
#             num = int(s.split()[0])
#             count_green += num  
#         if 'blue' in s :
#             num = int(s.split()[0])
#             count_blue += num 
#     if count_red <= 12 and count_green <= 13 and count_blue <= 14:
#         ids.append(game_num)
            
# print(ids)
# print(sum(ids))
        
    





# splited_lines = []    
# for line in lines:
#     sl = line.split(':')[-1].split(';')
    
    
    
#     for elem in sl:
#         ssl = elem.split(',')
#         splited_lines.append(ssl)
# print(splited_lines)