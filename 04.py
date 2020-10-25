S = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
S = S.replace(',', '')
S = S.replace('.', '')
list_S = S.split()
dict_S = {}
num_list = [0,5,6,7,8,9,15,16,19]
for i in range(1,len(list_S) + 1,1):
    now_S = list_S[i-1]
    if i in num_list:
        dict_S[now_S[0]] = i
    else:
        dict_S[now_S[0:2]] = i
print(dict_S)