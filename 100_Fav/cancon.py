def canConstruct(t,wb,memo={}):
    if t in memo:
        return memo[t]
    if t=='':
        return True
    for i in wb:
        if t.startswith(i):
            s=t[len(i):]
            if(canConstruct(s,wb,memo)):
                memo[t]=True
                return True
    memo[t]=False
    return False

def countConstruct(t,wb,memo={}):
    if t in memo:
        return memo[t]
    if t=='':
        return 1
    tc=0
    for i in wb:
        if t.startswith(i):
            nw=canConstruct(t[len(i):],wb,memo)
            tc+=nw
    memo[t]=tc
    return tc


def allConstruct(t, wb, memo={}):
    if t in memo:
        return memo[t]
    if t == '':
        return [[]]  # Base case: one way to construct an empty string

    res = []
    for i in wb:
        if t.startswith(i):
            suffix = t[len(i):]
            suffix_ways = allConstruct(suffix, wb, memo)  # Recursive call
            target_ways = [[i] + way for way in suffix_ways]  # Add `i` in front of each way
            res.extend(target_ways)  # Add these ways to our result list

    memo[t] = res
    return res


# Example call
print(allConstruct("janeesh", ["jan","jane","ja","ee","sh","esh"]["jan","jane","ja","ee","sh","esh"]))  # Expected to return [['jan', 'ee', 'sh']]

print(canConstruct("janeesh",["jan","jane","ja","ee","sh"],{}))
print(countConstruct("janeesh",["jan","jane","ja","ee","sh","esh"],{}))
