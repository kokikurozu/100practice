def cipher(S):
    x = ''
    for i in S:
        if ord('a') <= ord(i) <= ord('z'):
            s = chr(219 - ord(i))
        else:
            s = i
        x = x + s
    return x

S = 'rx2gg4'
print(cipher(S))