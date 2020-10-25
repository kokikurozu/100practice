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

S = 'I am an NLPer'
N = 1
x = n_gram(S,N)
print(x)