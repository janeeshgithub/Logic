def jan(a, b, c, i, j, k):
    while k < len(c):
        if i < len(a) and j < len(b) and a[i] == b[j] and a[i] == c[k]:
            if jan(a, b, c, i + 1, j, k + 1):
                return True
            else:
                return jan(a, b, c, i, j + 1, k + 1)
        elif i < len(a) and a[i] == c[k]:
            i += 1
            k += 1
        elif j < len(b) and b[j] == c[k]:
            j += 1
            k += 1
        else:
            return False
    return True


s1 = str(input().strip())
s2 = str(input().strip())
s3 = str(input().strip())
if len(s1) + len(s2) != len(s3):
    print("NO")
    exit()
vm = jan(s1, s2, s3, 0, 0, 0)
if vm:
    print("YES")
else:
    print("NO")