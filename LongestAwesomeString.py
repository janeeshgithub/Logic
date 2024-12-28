def longestAwesome(s):
    d, m, a = {}, 0, 0
    d[0] = -1
    for i in range(len(s)):
        n = ord(s[i]) - ord('0')
        m = m ^ (1 << n)
        if m in d:
            a = max(a, i - d[m])
        else:
            d[m] = i
        for j in range(0, 10):
            t = m ^ (1 << j)
            if t in d:
                a = max(a, i - d[t])
    print("Final:",a)
longestAwesome("211234")
