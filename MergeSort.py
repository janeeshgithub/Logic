def merge(arr,m,l,h):
    t=[]
    left=l
    right=m+1
    while (left<=m and right<=h):
        if arr[left]<=arr[right]:
            t.add(arr[left])
            left+=1
        else:
            t.add(arr[right])
            right+=1

    while(left<=m):
        t.append(arr[left])
        left+=1
    while (right <= h):
        t.append(arr[right])
        right += 1
    for i range(l,h):
        arr[i]=t[i-l]

    print(arr)
