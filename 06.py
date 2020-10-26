def n_gram(s,n):    
    words_gram = []
    moji_gram = []
    s = s.replace(',', '')
    s = s.replace('.', '')
    #moji_s = s.replace(' ', '')    今回は空白も文字として考える
    for i in range(len(s)-n+1):
        moji_gram.append(s[i:i+n])
    list_s = s.split()
    for i in range(len(list_s)-n+1):
        words_gram.append(list_s[i:i+n])
    return words_gram, moji_gram

str1 = 'paraparaparadise'
str2 = 'paragraph'
N = 2
a,X = n_gram(str1, N)
b,Y = n_gram(str2, N)
X = set(X)
Y = set(Y)
wa_syugo = X | Y
seki_syugo = X & Y
sa_syugoX = X - Y
sa_syugoY = Y - X
print(wa_syugo)
print(seki_syugo)
print(sa_syugoX)
print(sa_syugoY)