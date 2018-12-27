def median(l):
    l = sorted(l)
    l_len = len(l)
    if l_len < 1:
        return None
    if l_len % 2 == 0 :
        return ( l[(l_len-1)/2] + l[(l_len+1)/2] ) / 2.0
    else:
        return l[(l_len-1)/2]

l = [1]
print median(l)

l = [3,1,2]
print median(l)

l = [1,2,3,4]
print median(l)
