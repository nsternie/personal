def factorial(k):
    s = 1
    for i in range(1,k+1):
        s *= i
    return s

for m in range(1, 100):
    e = 1
    for n in range(1, m):
        e += 1/(factorial(n))
    print(str(m)+" -> "+str(e))