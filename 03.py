S = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
S = S.replace(',', '')
S = S.replace('.', '')
list_S = S.split()
list_cnt = []
for i in list_S:
    list_cnt.append(len(i))
print(list_cnt)