S = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
list_S = S.split()
list_cnt = []
for i in list_S:
    list_cnt.append(len(i))
list_cnt[len(i) - 1] -= 1
print(list_cnt)