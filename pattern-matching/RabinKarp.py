def rabinKarp(T,P,d,q) :
    m = len(P)
    n = len(T)
    h = (d ** (m-1))%q
    p,t,hit,sp_hit=0,0,0,0
    for i in range(m):
        p = (d * p + ord(P[i])) % q
        t = (d * t + ord(T[i])) % q

    for s in range(n-m+1) :
        if(p == t):
            sp_hit += 1
            if(P == T[s:s+m]) :
                print("Pattern occurs with shift {}".format(s))
                hit += 1
                sp_hit -= 1

        if(s < n-m):
            t = (d * (t - ord(T[s])*h) + ord(T[s+m])) % q
    
    print("Hits:{}".format(hit))
    print("Spurious hits:{}".format(sp_hit))

if __name__ == "__main__":
    T = input("Enter Main String:")
    P = input("Enter Pattern:")
    d = 256
    q = 11
    rabinKarp(T,P,d,q)

