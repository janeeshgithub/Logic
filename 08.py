x=True
class Jan:
    def __init__(A,b,c):
        A.b=b
        A.c=c
    def Ok(A):
        return A.b+A.c

a=Jan(10,12)
print(a.Ok())