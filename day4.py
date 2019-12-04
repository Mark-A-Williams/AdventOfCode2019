a = 153517
b = 630395

def c(d):
    e = str(d)
    for f in range(len(e)-1):
        if e[f] == e[f+1]:
            return True
    return False
    
def g(h):
    i = str(h)
    for j in range(len(i)-1):
        if (int(i[j+1]) < int(i[j])):
            return False
    return True

k = []

def l(m):
    global k
    if(c(m) and g(m)):
        k.append(m)


for n in range (a, b + 1):
    l(n)

print len(k)
