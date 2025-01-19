def Josephus(n, k):
    i = 1
    ans = 0
    while(i <= n):
        ans = (ans + k) % i
        i += 1
    return ans + 1


def josephus1(n, k):

    if (n == 1):
        return 1
    else:

        # The position returned by
        # josephus(n - 1, k) is adjusted
        # because the recursive call
        # josephus(n - 1, k) considers
        # the original position
        # k%n + 1 as position 1
        return (josephus1(n - 1, k) + k-1) % n + 1
    
print(Josephus(10,4))
print(josephus1(10,4))