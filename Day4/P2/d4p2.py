with open('input.txt') as f:
    lines = f.readlines()


cards_copies = dict()
candidatos_queue = []
for i in range(1, len(lines)+1):
    cards_copies[i] = 1
    candidatos_queue.append(i)



def splitt(lines):
    delimiters = [':', '|']
    splited_lines = []    
    for line in lines:
        for delimiter in delimiters:
            line = "#".join(line.split(delimiter))
        res = line.split("#")
        splited_lines.append(res)
    # print(splited_lines)
    return splited_lines


cards_matches = dict()
splited_lines = splitt(lines)
for card in splited_lines:
    win_values = [int(x) for x in card[1].split()]
    has_win = []
    all_value = [int(x) for x in card[-1].split()]
    for value in all_value:
        if value in win_values:
            has_win.append(value)
    card_num = int(card[0].split()[1])
    matches_num = len(has_win)
    range_ad = []
    for i in range(matches_num):
        # print('MATCHES',matches_num)
        # print(card_num+i+1)
        range_ad.append(card_num+i+1)
    cards_matches[card_num] = (matches_num, range_ad)
    
    
# print('MATCHES', cards_matches)
# print('QUEUE', candidatos_queue)
# print('_'*20)

while candidatos_queue:
    num_card = candidatos_queue.pop(0)
    # print('NUM_CARD_QUEUE', num_card)
    if cards_matches[num_card] != 0:
        matches_num = cards_matches[num_card][0]
        for index_cp in cards_matches[num_card][1]:
            cards_copies[index_cp] += 1
            candidatos_queue.append(index_cp)
            # print(candidatos_queue)
    # print('-'*20)


print(sum(cards_copies.values()))

    

#--------------------------------------------

# while candidatos_queue is not []:
#     for card in splited_lines:
#         win_values = [int(x) for x in card[1].split()]
#         has_win = []
#         all_value = [int(x) for x in card[-1].split()]
#         for value in all_value:
#             if value in win_values:
#                 has_win.append(value)

#         card_num = int(card[0].split()[1])
#         matches_num = len(has_win)
#         candidatos_queue.pop(0)
#         for i in range(card_num+1, matches_num+1):
#             cards_copies[i] += 1
#             candidatos_queue.append(i)



#--------------------------------
# delimiters = [':', '|']


# splited_lines = []    
# for line in lines:
#     for delimiter in delimiters:
#         line = "#".join(line.split(delimiter))
#     res = line.split("#")
#     splited_lines.append(res)
    
    
# points_per_card = []
# numb_win_per_card = []
# for card in splited_lines:
#     win_values = [int(x) for x in card[1].split()]
#     has_win = []
#     values = [int(x) for x in card[-1].split()]
#     for all_value in values:
#         if all_value in win_values:
#             has_win.append(all_value)
#     points = pow(2, len(has_win)-1) if len(has_win) > 0 else 0
    
    

# copies = [1 for i in len(splited_lines)]

# # for i in len(points_per_card):
# #     if points_per_card > 0:

        
        
        
# print(sum(points_per_card))
        