wordlist={"a","b","c","d","bc","ab","cd"}
s="abcd"
r=[]
def backtrack(start,curr):
    if len(s)==start:
        r.append("-".join(curr))
        return
    for end in range(start+1,len(s)+1):
        w=s[start:end]
        if w in wordlist:
            backtrack(end,curr+[w])
backtrack(0,[])
print(r)

