def convert(s):
    ch = list(s)
    for i in range(len(s)):
        if (i == 0 and ch[i] != ' ' or ch[i] != ' ' and ch[i - 1] == ' '):
            if (ch[i] >= 'a' and ch[i] <= 'z'):
                ch[i] = chr(ord(ch[i]) - ord('a') +
                            ord('A'))
        elif (ch[i] >= 'A' and ch[i] <= 'Z'):
            ch[i] = chr(ord(ch[i]) + ord('a') -
                        ord('A'))
    st = "".join(ch)
    return st;


strout = "hello good morning every one"
print(convert(strout))