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

# part 2

def o(p):
    q = str(p)
    for r in range(1, len(q) - 2):
        if (q[r] == q[r+1]):
            if (q[r] != q[r + 2]) and (q[r] != q[r - 1]):
                return True
    if (q[-1] == q[-2]) and (q[-2] != q[-3]):
        return True
    if (q[0] == q[1]) and (q[1] != q[2]):
        return True
    return False
    # s = len(q) - 2
    # if ((q[s] == q[s + 1])):# and (q[s] != q[s - 1])):
    #     return True

t = []

def u(v):
    global t
    if(o(v) and g(v)):
        t.append(v)

for w in range (a, b + 1):
    u(w)

print len(t)
print t

print o(677789)
print g(677789)
